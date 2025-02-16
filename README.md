# PMP
Панель мониторинга питанием для трех PZEM-016 220В 100А
## Установка
Вы можете установить это дополнение через магазин Home Assistant Community Store (HAS).
configuration.yaml
# Настройки для вашего аддона
```
pmp:
  options:
    mqtt_host: "mqtt://localhost"
    mqtt_port: 1883
    mqtt_user: ""
    mqtt_password: ""
    modbus_hosts:
      L1:
        host: ""
        unit_id: 1
      L2:
        host: "
        unit_id: 2
      L3:
        host: ""
        unit_id: 3
```
