#!/usr/bin/with-contenv bash
export MQTT_BROKER="$MQTT_BROKER"
export MQTT_PORT="$MQTT_PORT"
export MQTT_USERNAME="$MQTT_USERNAME"
export MQTT_PASSWORD="$MQTT_PASSWORD"
export MODBUS_HOST_L1="$MODBUS_HOST_L1"
export MODBUS_UNIT_ID_L1="$MODBUS_UNIT_ID_L1"
export MODBUS_HOST_L2="$MODBUS_HOST_L2"
export MODBUS_UNIT_ID_L2="$MODBUS_UNIT_ID_L2"
export MODBUS_HOST_L3="$MODBUS_HOST_L3"
export MODBUS_UNIT_ID_L3="$MODBUS_UNIT_ID_L3"
# Запуск приложения
# python /app/app/app.py --port=${FLASK_PORT:-5000}
python3 /usr/src/app/app.py --port=${FLASK_PORT}
