import RPi.GPIO as GPIO  # biblioteka niezbędna do kontrolowania stanu pinów
import time  # biblioteka odpowiedzialna za reprezentację czasu

if __name__ == "__main__":
    GPIO.setwarnings(False)  # ignorowanie ostrzeżeń
    GPIO.setmode(GPIO.BCM)  # WAŻNY KROK -- ustawiamy jaką numerację pinów wykorzystamy
    GPIO.setup(19, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)

    for i in range(0, 3):
        GPIO.output(19, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(19, GPIO.LOW)

        GPIO.output(18, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(18, GPIO.LOW)

        GPIO.output(13, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(13, GPIO.LOW)

        GPIO.output(12, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(12, GPIO.LOW)

        GPIO.output(19, GPIO.HIGH)
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(12, GPIO.HIGH)

        time.sleep(2)
        GPIO.output(19, GPIO.LOW)
        GPIO.output(18, GPIO.LOW)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(12, GPIO.LOW)


    GPIO.cleanup()  # na koniec programu -- sprzątanie
