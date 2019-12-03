"""Support for the Mikrotik Router switches."""
import logging

from homeassistant.components.switch import SwitchDevice
from homeassistant.core import callback
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC
from homeassistant.helpers.dispatcher import async_dispatcher_connect
from homeassistant.helpers.restore_state import RestoreEntity

from homeassistant.const import (
    CONF_NAME,
    ATTR_ATTRIBUTION,
)
from .const import (
    DOMAIN,
    DATA_CLIENT,
    ATTRIBUTION,
)

_LOGGER = logging.getLogger(__name__)

DEVICE_ATTRIBUTES = [
    "running",
    "enabled",
    "comment",
    "client-ip-address",
    "client-mac-address",
    "port-mac-address",
    "last-link-down-time",
    "last-link-up-time",
    "link-downs",
    "actual-mtu",
    "type",
    "name",
    "default-name",
]


# ---------------------------
#   async_setup_entry
# ---------------------------
async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up switches for Mikrotik Router component."""
    name = config_entry.data[CONF_NAME]
    mikrotik_controller = hass.data[DOMAIN][DATA_CLIENT][config_entry.entry_id]
    switches = {}
    
    @callback
    def update_controller():
        """Update the values of the controller."""
        update_items(name, mikrotik_controller, async_add_entities, switches)
    
    mikrotik_controller.listeners.append(
        async_dispatcher_connect(hass, mikrotik_controller.signal_update, update_controller)
    )
    
    update_controller()
    return


# ---------------------------
#   update_items
# ---------------------------
@callback
def update_items(name, mikrotik_controller, async_add_entities, switches):
    """Update device switch state from the controller."""
    new_switches = []
    
    for uid in mikrotik_controller.data['interface']:
        if mikrotik_controller.data['interface'][uid]['type'] == "ether":
            item_id = name + "-" + mikrotik_controller.data['interface'][uid]['default-name']
            if item_id in switches:
                if switches[item_id].enabled:
                    switches[item_id].async_schedule_update_ha_state()
                continue
            
            switches[item_id] = MikrotikControllerPortEnableSwitch(name, uid, mikrotik_controller)
            new_switches.append(switches[item_id])
    
    if new_switches:
        async_add_entities(new_switches)
    
    return


# ---------------------------
#   MikrotikControllerPortEnableSwitch
# ---------------------------
class MikrotikControllerPortEnableSwitch(SwitchDevice, RestoreEntity):
    """Representation of a network port switch."""
    
    def __init__(self, name, uid, mikrotik_controller):
        """Set up tracked port."""
        self._name = name
        self._uid = uid
        self.mikrotik_controller = mikrotik_controller
        
        self._attrs = {
            ATTR_ATTRIBUTION: ATTRIBUTION,
        }
    
    async def async_added_to_hass(self):
        """Port entity created."""
        _LOGGER.debug("New port switch %s (%s)", self._name, self.mikrotik_controller.data['interface'][self._uid]['port-mac-address'])
        return
    
    async def async_update(self):
        """Synchronize state with controller."""
        # await self.mikrotik_controller.async_update()
        return
        
    @property
    def name(self) -> str:
        """Return the name of the port."""
        return self.mikrotik_controller.data['interface'][self._uid]['default-name']
    
    @property
    def unique_id(self) -> str:
        """Return a unique identifier for this port."""
        return f"{self._name.lower()}-enable_switch-{self.mikrotik_controller.data['interface'][self._uid]['port-mac-address']}"
    
    @property
    def available(self) -> bool:
        """Return if controller is available."""
        return self.mikrotik_controller.connected()
    
    @property
    def icon(self):
        """Return the icon."""
        if self.mikrotik_controller.data['interface'][self._uid]['running']:
            icon = 'mdi:lan-connect'
        else:
            icon = 'mdi:lan-pending'
        
        if not self.mikrotik_controller.data['interface'][self._uid]['enabled']:
            icon = 'mdi:lan-disconnect'
        
        return icon
    
    @property
    def device_info(self):
        """Return a port description for device registry."""
        info = {
            "connections": {(CONNECTION_NETWORK_MAC, self.mikrotik_controller.data['interface'][self._uid]['port-mac-address'])},
            "manufacturer": self.mikrotik_controller.data['resource']['platform'],
            "model": "Port",
            "name": self.mikrotik_controller.data['interface'][self._uid]['default-name'],
        }
        return info
    
    @property
    def device_state_attributes(self):
        """Return the port state attributes."""
        attributes = self._attrs
        
        for variable in DEVICE_ATTRIBUTES:
            if variable in self.mikrotik_controller.data['interface'][self._uid]:
                attributes[variable] = self.mikrotik_controller.data['interface'][self._uid][variable]
        
        return attributes

    async def async_turn_on(self):
        """Turn on the switch."""
        path = '/interface'
        param = 'default-name'
        value = self.mikrotik_controller.data['interface'][self._uid][param]
        mod_param = 'disabled'
        mod_value = False
        self.mikrotik_controller.set_value(path, param, value, mod_param, mod_value)
        await self.mikrotik_controller.force_update()
        return

    async def async_turn_off(self):
        """Turn on the switch."""
        path = '/interface'
        param = 'default-name'
        value = self.mikrotik_controller.data['interface'][self._uid][param]
        mod_param = 'disabled'
        mod_value = True
        self.mikrotik_controller.set_value(path, param, value, mod_param, mod_value)
        await self.mikrotik_controller.async_update()
        return

    @property
    def is_on(self):
        """Return true if device is on."""
        return self.mikrotik_controller.data['interface'][self._uid]['enabled']