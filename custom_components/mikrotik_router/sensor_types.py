"""Definitions for Mikrotik Router sensor entities."""
from dataclasses import dataclass, field
from typing import List
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC
from homeassistant.helpers.entity import EntityCategory
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorStateClass,
    SensorEntityDescription,
)
from homeassistant.const import (
    TEMP_CELSIUS,
    ELECTRIC_POTENTIAL_VOLT,
    POWER_WATT,
    PERCENTAGE,
    DATA_BYTES,
)
from .const import DOMAIN

DEVICE_ATTRIBUTES_IFACE = [
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
]

DEVICE_ATTRIBUTES_IFACE_ETHER = [
    "status",
    "auto-negotiation",
    "rate",
    "full-duplex",
    "default-name",
    "poe-out",
]

DEVICE_ATTRIBUTES_IFACE_SFP = [
    "status",
    "auto-negotiation",
    "advertising",
    "link-partner-advertising",
    "sfp-temperature",
    "sfp-supply-voltage",
    "sfp-module-present",
    "sfp-tx-bias-current",
    "sfp-tx-power",
    "sfp-rx-power",
    "sfp-rx-loss",
    "sfp-tx-fault",
    "sfp-type",
    "sfp-connector-type",
    "sfp-vendor-name",
    "sfp-vendor-part-number",
    "sfp-vendor-revision",
    "sfp-vendor-serial",
    "sfp-manufacturing-date",
    "eeprom-checksum",
]

DEVICE_ATTRIBUTES_CLIENT_TRAFFIC = [
    "address",
    "mac-address",
    "host-name",
    "authorized",
    "bypassed",
]
DEVICE_ATTRIBUTES_GPS = [
    "valid",
    "latitude",
    "longitude",
    "altitude",
    "speed",
    "destination-bearing",
    "true-bearing",
    "magnetic-bearing",
    "satellites",
    "fix-quality",
    "horizontal-dilution",
]


@dataclass
class MikrotikSensorEntityDescription(SensorEntityDescription):
    """Class describing mikrotik entities."""

    ha_group: str = ""
    ha_connection: str = ""
    ha_connection_value: str = ""
    data_path: str = ""
    data_attribute: str = ""
    data_name: str = ""
    data_name_comment: bool = False
    data_uid: str = ""
    data_reference: str = ""
    data_attributes_list: List = field(default_factory=lambda: [])
    func: str = "MikrotikSensor"


SENSOR_TYPES = {
    "system_temperature": MikrotikSensorEntityDescription(
        key="system_temperature",
        name="Temperature",
        icon="mdi:thermometer",
        native_unit_of_measurement=TEMP_CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="System",
        data_path="health",
        data_attribute="temperature",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    "system_voltage": MikrotikSensorEntityDescription(
        key="system_voltage",
        name="Voltage",
        icon="mdi:lightning-bolt",
        native_unit_of_measurement=ELECTRIC_POTENTIAL_VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="health",
        data_attribute="voltage",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    "system_cpu-temperature": MikrotikSensorEntityDescription(
        key="system_cpu-temperature",
        name="CPU temperature",
        icon="mdi:thermometer",
        native_unit_of_measurement=TEMP_CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="System",
        data_path="health",
        data_attribute="cpu-temperature",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    "system_board-temperature1": MikrotikSensorEntityDescription(
        key="system_board-temperature1",
        name="Board temperature",
        icon="mdi:thermometer",
        native_unit_of_measurement=TEMP_CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="System",
        data_path="health",
        data_attribute="board-temperature1",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    "system_power-consumption": MikrotikSensorEntityDescription(
        key="system_power-consumption",
        name="Power consumption",
        icon="mdi:transmission-tower",
        native_unit_of_measurement=POWER_WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="System",
        data_path="health",
        data_attribute="power-consumption",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    "system_fan1-speed": MikrotikSensorEntityDescription(
        key="system_fan1-speed",
        name="Fan1 speed",
        icon="mdi:fan",
        native_unit_of_measurement="RPM",
        device_class=None,
        state_class=None,
        entity_category=None,
        ha_group="System",
        data_path="health",
        data_attribute="fan1-speed",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    "system_fan2-speed": MikrotikSensorEntityDescription(
        key="system_fan2-speed",
        name="Fan2 speed",
        icon="mdi:fan",
        native_unit_of_measurement="RPM",
        device_class=None,
        state_class=None,
        entity_category=None,
        ha_group="System",
        data_path="health",
        data_attribute="fan2-speed",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    "system_uptime": MikrotikSensorEntityDescription(
        key="system_uptime",
        name="Uptime",
        icon=None,
        native_unit_of_measurement=None,
        device_class=SensorDeviceClass.TIMESTAMP,
        state_class=None,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="resource",
        data_attribute="uptime",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    "system_cpu-load": MikrotikSensorEntityDescription(
        key="system_cpu-load",
        name="CPU load",
        icon="mdi:speedometer",
        native_unit_of_measurement=PERCENTAGE,
        device_class=None,
        state_class=None,
        entity_category=None,
        ha_group="System",
        data_path="resource",
        data_attribute="cpu-load",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    "system_memory-usage": MikrotikSensorEntityDescription(
        key="system_memory-usage",
        name="Memory usage",
        icon="mdi:memory",
        native_unit_of_measurement=PERCENTAGE,
        device_class=None,
        state_class=None,
        entity_category=None,
        ha_group="System",
        data_path="resource",
        data_attribute="memory-usage",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    "system_hdd-usage": MikrotikSensorEntityDescription(
        key="system_hdd-usage",
        name="HDD usage",
        icon="mdi:harddisk",
        native_unit_of_measurement=PERCENTAGE,
        device_class=None,
        state_class=None,
        entity_category=None,
        ha_group="System",
        data_path="resource",
        data_attribute="hdd-usage",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    "system_clients-wired": MikrotikSensorEntityDescription(
        key="system_clients-wired",
        name="Wired clients",
        icon="mdi:lan",
        native_unit_of_measurement=None,
        device_class=None,
        state_class=None,
        entity_category=None,
        ha_group="System",
        data_path="resource",
        data_attribute="clients_wired",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    "system_clients-wireless": MikrotikSensorEntityDescription(
        key="system_clients-wireless",
        name="Wireless clients",
        icon="mdi:wifi",
        native_unit_of_measurement=None,
        device_class=None,
        state_class=None,
        entity_category=None,
        ha_group="System",
        data_path="resource",
        data_attribute="clients_wireless",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    "system_captive-authorized": MikrotikSensorEntityDescription(
        key="system_captive-authorized",
        name="Captive portal clients",
        icon="mdi:key-wireless",
        native_unit_of_measurement=None,
        device_class=None,
        state_class=None,
        entity_category=None,
        ha_group="System",
        data_path="resource",
        data_attribute="captive_authorized",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    "system_gps-latitude": MikrotikSensorEntityDescription(
        key="system_gps-latitude",
        name="Latitude",
        icon="mdi:latitude",
        native_unit_of_measurement=None,
        device_class=None,
        state_class=None,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="gps",
        data_attribute="latitude",
        data_name="",
        data_uid="",
        data_reference="",
        data_attributes_list=DEVICE_ATTRIBUTES_GPS,
    ),
    "system_gps-longitude": MikrotikSensorEntityDescription(
        key="system_gps-longitude",
        name="Longitude",
        icon="mdi:longitude",
        native_unit_of_measurement=None,
        device_class=None,
        state_class=None,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="gps",
        data_attribute="longitude",
        data_name="",
        data_uid="",
        data_reference="",
        data_attributes_list=DEVICE_ATTRIBUTES_GPS,
    ),
    "traffic_tx": MikrotikSensorEntityDescription(
        key="traffic_tx",
        name="TX",
        icon="mdi:upload-network-outline",
        native_unit_of_measurement="data__tx-attr",
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="data__default-name",
        ha_connection=CONNECTION_NETWORK_MAC,
        ha_connection_value="data__port-mac-address",
        data_path="interface",
        data_attribute="tx",
        data_name="default-name",
        data_uid="",
        data_reference="default-name",
        data_attributes_list=DEVICE_ATTRIBUTES_IFACE,
        func="MikrotikInterfaceTrafficSensor",
    ),
    "traffic_rx": MikrotikSensorEntityDescription(
        key="traffic_rx",
        name="RX",
        icon="mdi:download-network-outline",
        native_unit_of_measurement="data__rx-attr",
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="data__default-name",
        ha_connection=CONNECTION_NETWORK_MAC,
        ha_connection_value="data__port-mac-address",
        data_path="interface",
        data_attribute="rx",
        data_name="default-name",
        data_uid="",
        data_reference="default-name",
        data_attributes_list=DEVICE_ATTRIBUTES_IFACE,
        func="MikrotikInterfaceTrafficSensor",
    ),
    "total_tx": MikrotikSensorEntityDescription(
        key="tx-total",
        name="TX total",
        icon="mdi:upload-network",
        native_unit_of_measurement=DATA_BYTES,
        device_class=None,
        state_class=SensorStateClass.TOTAL_INCREASING,
        entity_category=None,
        ha_group="data__default-name",
        ha_connection=CONNECTION_NETWORK_MAC,
        ha_connection_value="data__port-mac-address",
        data_path="interface",
        data_attribute="tx-current",
        data_name="default-name",
        data_uid="",
        data_reference="default-name",
        data_attributes_list=DEVICE_ATTRIBUTES_IFACE,
        func="MikrotikInterfaceTrafficSensor",
    ),
    "total_rx": MikrotikSensorEntityDescription(
        key="rx-total",
        name="RX total",
        icon="mdi:download-network",
        native_unit_of_measurement=DATA_BYTES,
        device_class=None,
        state_class=SensorStateClass.TOTAL_INCREASING,
        entity_category=None,
        ha_group="data__default-name",
        ha_connection=CONNECTION_NETWORK_MAC,
        ha_connection_value="data__port-mac-address",
        data_path="interface",
        data_attribute="rx-current",
        data_name="default-name",
        data_uid="",
        data_reference="default-name",
        data_attributes_list=DEVICE_ATTRIBUTES_IFACE,
        func="MikrotikInterfaceTrafficSensor",
    ),
    "client_traffic_lan_tx": MikrotikSensorEntityDescription(
        key="client_traffic_lan_tx",
        name="LAN TX",
        icon="mdi:upload-network",
        native_unit_of_measurement="data__tx-rx-attr",
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="",
        ha_connection=CONNECTION_NETWORK_MAC,
        ha_connection_value="data__mac-address",
        data_path="client_traffic",
        data_attribute="lan-tx",
        data_name="host-name",
        data_uid="",
        data_reference="mac-address",
        data_attributes_list=DEVICE_ATTRIBUTES_CLIENT_TRAFFIC,
        func="MikrotikClientTrafficSensor",
    ),
    "client_traffic_lan_rx": MikrotikSensorEntityDescription(
        key="client_traffic_lan_rx",
        name="LAN RX",
        icon="mdi:download-network",
        native_unit_of_measurement="data__tx-rx-attr",
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="",
        ha_connection=CONNECTION_NETWORK_MAC,
        ha_connection_value="data__mac-address",
        data_path="client_traffic",
        data_attribute="lan-rx",
        data_name="host-name",
        data_uid="",
        data_reference="mac-address",
        data_attributes_list=DEVICE_ATTRIBUTES_CLIENT_TRAFFIC,
        func="MikrotikClientTrafficSensor",
    ),
    "client_traffic_wan_tx": MikrotikSensorEntityDescription(
        key="client_traffic_wan_tx",
        name="WAN TX",
        icon="mdi:upload-network",
        native_unit_of_measurement="data__tx-rx-attr",
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="",
        ha_connection=CONNECTION_NETWORK_MAC,
        ha_connection_value="data__mac-address",
        data_path="client_traffic",
        data_attribute="wan-tx",
        data_name="host-name",
        data_uid="",
        data_reference="mac-address",
        data_attributes_list=DEVICE_ATTRIBUTES_CLIENT_TRAFFIC,
        func="MikrotikClientTrafficSensor",
    ),
    "client_traffic_wan_rx": MikrotikSensorEntityDescription(
        key="client_traffic_wan_rx",
        name="WAN RX",
        icon="mdi:download-network",
        native_unit_of_measurement="data__tx-rx-attr",
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="",
        ha_connection=CONNECTION_NETWORK_MAC,
        ha_connection_value="data__mac-address",
        data_path="client_traffic",
        data_attribute="wan-rx",
        data_name="host-name",
        data_uid="",
        data_reference="mac-address",
        data_attributes_list=DEVICE_ATTRIBUTES_CLIENT_TRAFFIC,
        func="MikrotikClientTrafficSensor",
    ),
    "client_traffic_tx": MikrotikSensorEntityDescription(
        key="client_traffic_tx",
        name="TX",
        icon="mdi:upload-network",
        native_unit_of_measurement="data__tx-rx-attr",
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="",
        ha_connection=CONNECTION_NETWORK_MAC,
        ha_connection_value="data__mac-address",
        data_path="client_traffic",
        data_attribute="tx",
        data_name="host-name",
        data_uid="",
        data_reference="mac-address",
        data_attributes_list=DEVICE_ATTRIBUTES_CLIENT_TRAFFIC,
        func="MikrotikClientTrafficSensor",
    ),
    "client_traffic_rx": MikrotikSensorEntityDescription(
        key="client_traffic_rx",
        name="RX",
        icon="mdi:download-network",
        native_unit_of_measurement="data__tx-rx-attr",
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="",
        ha_connection=CONNECTION_NETWORK_MAC,
        ha_connection_value="data__mac-address",
        data_path="client_traffic",
        data_attribute="rx",
        data_name="host-name",
        data_uid="",
        data_reference="mac-address",
        data_attributes_list=DEVICE_ATTRIBUTES_CLIENT_TRAFFIC,
        func="MikrotikClientTrafficSensor",
    ),
    "environment": MikrotikSensorEntityDescription(
        key="environment",
        name="",
        icon="mdi:clipboard-list",
        native_unit_of_measurement="",
        device_class=None,
        state_class=None,
        entity_category=None,
        ha_group="Environment",
        ha_connection=DOMAIN,
        ha_connection_value="Environment",
        data_path="environment",
        data_attribute="value",
        data_name="name",
        data_uid="name",
        data_reference="name",
    ),
}

SENSOR_SERVICES = {}
