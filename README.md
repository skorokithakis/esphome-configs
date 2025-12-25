# ESPHome Sensors

Three sensor configs with room-aware substitutions and MQTT topics.

- `co2_sensor.yaml`: ESP32-C6 (Seeed XIAO), SCD4x CO2/temperature/humidity over I2C, MQTT topics under `esphome/<room>/...`.
- `light_sensor.yaml`: ESP8266 D1 Mini, A0 ADC light level (0-100%), MQTT broker `mqtt.home.stavros.io`.
- `ultratv.yaml`: ESP8266 D1 Mini with 240x240 ST7789V display, shows time/date/temperature/humidity/CO2 on synthwave background, subscribes to sensor data via MQTT, automatic brightness adjustment.

All use Wi-Fi secrets from `secrets.yaml`, Home Assistant API, OTA, and a fallback AP.

## Deploy (terse)

```bash
./deploy <room> <config.yml> [esphome args...]
```

Rooms: `livingroom`, `office`, `bedroom`. Example:

```bash
./deploy bedroom co2_sensor.yaml
```
