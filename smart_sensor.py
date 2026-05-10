"""
MQTT Smart temperature Sensor
"""

import time
import json

import paho.mqtt.client as mqtt
from faker import Faker

# let's connect to the MQTT broker
MQTT_BROKER_URL    = "localhost"
MQTT_PUBLISH_TOPIC = "paper_wifi/test/"

mqttc = mqtt.Client()
mqttc.connect(MQTT_BROKER_URL)

# Init faker our fake data provider
fake = Faker()

# Infinite loop of fake data sent to the Broker
while True:
    humidity = fake.random_int(min=90, max=100)
    temperature = fake.random_int(min=25, max=30)
    battery_voltage_mv = fake.random_int(min=2900, max=3100)
    data = {
        "humidity": humidity,
        "temperature": temperature,
        "battery_voltage_mv": battery_voltage_mv,
    }
    payload = json.dumps(data)
    mqttc.publish(MQTT_PUBLISH_TOPIC, payload)
    print(f"Published JSON payload: {payload}")
    time.sleep(1)