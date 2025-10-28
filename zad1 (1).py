import time
import pigpio  # http://abyz.co.uk/rpi/pigpio/python.html
import RPi.GPIO as GPIO  # biblioteka niezbędna do kontrolowania stanu pinów

GPIO.setwarnings(False)  # ignorowanie ostrzeżeń
GPIO.setmode(GPIO.BCM)  # WAŻNY KROK -- ustawiamy jaką numerację pinów wykorzystamy
GPIO.setup(19, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

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
        print("{:.2f}".format(temp))

        if temp <= 23:
            GPIO.output(19, GPIO.LOW)
            GPIO.output(18, GPIO.LOW)
            GPIO.output(13, GPIO.LOW)
            GPIO.output(12, GPIO.LOW)
        if (temp > 23) and (temp <= 24):
            GPIO.output(19, GPIO.HIGH)
            GPIO.output(18, GPIO.LOW)
            GPIO.output(13, GPIO.LOW)
            GPIO.output(12, GPIO.LOW)
        if (temp > 24) and (temp <= 25):
            GPIO.output(19, GPIO.HIGH)
            GPIO.output(18, GPIO.HIGH)
            GPIO.output(13, GPIO.LOW)
            GPIO.output(12, GPIO.LOW)
        if (temp > 25) and (temp <= 26):
            GPIO.output(19, GPIO.HIGH)
            GPIO.output(18, GPIO.HIGH)
            GPIO.output(13, GPIO.HIGH)
            GPIO.output(12, GPIO.LOW)
        if temp > 26:
            GPIO.output(19, GPIO.HIGH)
            GPIO.output(18, GPIO.HIGH)
            GPIO.output(13, GPIO.HIGH)
            GPIO.output(12, GPIO.HIGH)

    time.sleep(0.25)  # Odczyt nie częściej niż 4 razy na sekundę

GPIO.cleanup()  # na koniec programu -- sprzątanie
pi.spi_close(sensor)
pi.stop()
