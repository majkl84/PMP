# PMP
Панель мониторинга питанием для трех PZEM-016 220В 100А
## Установка
Вы можете установить это дополнение через магазин Home Assistant Community Store (HAS).
configuration.yaml
# Настройки для вашего аддона
```
PMP:
  environment:
    MQTT_HOST: mqtt.shmv.su
    MQTT_PORT: 1883
    MQTT_USER: mqttvps
    MQTT_PASSWORD: mqttvps
    MODBUS_HOSTS: '{"host1": {"host": "10.0.6.84", "unit_id": 1}, "host2": {"host": "10.0.6.84", "unit_id": 2}, "host3": {"host": "10.0.6.84", "unit_id": 3}}'
```
