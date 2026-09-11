# ESPHome Sensors

Six configs with MQTT topics and room-aware substitutions where applicable.

- `co2_sensor.yaml`: ESP32-C6 (Seeed XIAO), SCD4x CO2/temperature/humidity over I2C, MQTT topics under `zigbee2mqtt/sensors/<room>/...`.
- `light_sensor.yaml`: ESP8266 D1 Mini, A0 ADC light level (0-100%), MQTT topic under `zigbee2mqtt/sensors/<room>/illuminance`.
- `presence_sensor.yaml`: ESP32-C3 SuperMini (esp-idf), HLK-LD2410 24GHz mmWave presence over UART (GPIO3/GPIO4, 256000 baud), MQTT only with discovery off, occupancy also published to `zigbee2mqtt/sensors/<room>/occupancy`, tuned through the built-in web server instead of Home Assistant.
- `filotas-bedtime.yaml`, `thessaloniki-bedtime.yaml`: ESP8266 D1 Mini with 240x240 ST7789V display, shows time/date and MQTT-sourced sensor/switch data on synthwave background, automatic brightness adjustment, share `bedtime.common.yaml`.
- `printer-fan-switch.yaml`: ESP8266 D1 Mini, GPIO fan switch, MQTT only.

All use Wi-Fi secrets from `secrets.yaml`, OTA, and a fallback AP.

## Deploy (terse)

```bash
./deploy <room> <config.yml> [esphome args...]
```

Rooms: `livingroom`, `office`, `bedroom`. Example:

```bash
./deploy bedroom co2_sensor.yaml
```
