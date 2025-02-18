import os
import json
# Настройки MQTT
MQTT_BROKER = os.getenv("MQTT_BROKER", "")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
MQTT_USERNAME = os.getenv("MQTT_USERNAME", "")
MQTT_PASSWORD = os.getenv("MQTT_PASSWORD", "")
MQTT_TOPICS = {
    "full_kWh": "home/PM/full_kWh",
    "total_kWh": "home/PM/total_kWh",
    "Full_data_L1": "home/PM/Full_data_L1",
    "Full_data_L2": "home/PM/Full_data_L2",
    "Full_data_L3": "home/PM/Full_data_L3",
    "General-W": "home/PM/General-W",
    "overflow_error": "home/PM/overflow_error"
}

# Настройки Modbus
MODBUS_HOSTS = {
    "L1": {
        "host": os.getenv("MODBUS_HOST_L1", ""),
        "unit_id": int(os.getenv("MODBUS_UNIT_ID_L1", 1))
    },
    "L2": {
        "host": os.getenv("MODBUS_HOST_L2", ""),
        "unit_id": int(os.getenv("MODBUS_UNIT_ID_L2", 2))
    },
    "L3": {
        "host": os.getenv("MODBUS_HOST_L3", ""),
        "unit_id": int(os.getenv("MODBUS_UNIT_ID_L3", 3))
    }
}

# Описание регистров
MODBUS_REGISTER_MAP = {
    "Voltage": (0, "uint16be", 0.1),  # Напряжение (V)
    "CurrentLow": (1, "uint16be", 0.001),  # Ток (A) - младшие 16 бит
    "PowerLow": (3, "uint16be", 1),  # Мощность (W) - младшие 16 бит
    "EnergyLow": (5, "uint16be", 1),  # Энергия (Wh) - младшие 16 бит
    "EnergyHigh": (6, "uint16be", 1),  # Энергия (Wh) - старшие 16 бит
    "Frequency": (7, "uint16be", 0.1),  # Частота (Hz)
    "PowerFactor": (8, "uint16be", 0.001),  # Коэффициент мощности
    "AlarmStatus": (9, "int16be", 1)  # Статус тревоги
}

# Настройки SQLite
SQLITE_DB = "power_manager.db"

# Глобальная переменная для управления логированием
LOGGING_ENABLED = True

# Глобальные переменные для сохранения предыдущих значений энергии
PREVIOUS_ENERGY = {"L1": 0, "L2": 0, "L3": 0}