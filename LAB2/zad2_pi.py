import paho.mqtt.client as mqtt
import time
import random
import pigpio  # http://abyz.co.uk/rpi/pigpio/python.html

broker_address = "10.104.32.238"
broker_port = 1883
topic = "sensor/data"

def read_sensor():
    pi = pigpio.pi()
    if not pi.connected:
        exit(0)

    # Otwórz SPI na CE1 z prędkością 1 Mbps (SPI channel 1, 1 Mbps, mode 0)
    sensor = pi.spi_open(1, 1000000, 0)

    stop = time.time() + 600  # działaj przez 10 minut

    while time.time() < stop:
        count, data = pi.spi_read(sensor, 2)
        if count == 2:
            sign = (data[0] & 0x80) >> 7
            value = (((data[0] & 0x7F) << 8) | data[1]) >> 5
            temp = value * 0.125
            if sign == 1:
                temp = -temp
            #print("{:.2f}".format(temp))

        time.sleep(0.25)  # Odczyt nie częściej niż 4 razy na sekundę

        pi.spi_close(sensor)
        pi.stop()
        return random.randint(500, 999) / 10, temp

def publish_data(client):
    humidity, temperature = read_sensor()
    if humidity is not None and temperature is not None:
        payload = f"{temperature:.2f} {humidity:.2f}"
        client.publish(topic, payload)
        print(f"Published: {payload}")
    else:
        print("Read error!")

client = mqtt.Client()
client.connect(broker_address, broker_port, 60)

while True:
    publish_data(client)
    time.sleep(5)
