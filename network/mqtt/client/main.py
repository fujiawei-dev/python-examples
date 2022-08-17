import json

import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    client.subscribe("topic")


def on_message(client: mqtt.Client, userdata, msg):
    payload = json.loads(msg.payload)


client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set("root", "123456")
client.connect("127.0.0.1", 4321, 60)

client.loop_forever()
