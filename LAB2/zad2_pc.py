import paho.mqtt.client as mqtt

broker_address = "10.104.32.238"
broker_port = 1883
topic = "sensor/data"

def on_message(client, userdata, message):
    payload = message.payload.decode("utf-8")
    temp, hum = map(float, payload.split(" "))
    print(f"Temperature: {temp:.2f} °C | Humidity: {hum:.2f} %")

client = mqtt.Client()
client.on_message = on_message

client.connect(broker_address, broker_port)
client.subscribe(topic)

print(f"Subscribed to topic '{topic}' on broker {broker_address}:{broker_port}")
client.loop_forever()
