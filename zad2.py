import RPi.GPIO as GPIO  # Biblioteka niezbędna do kontrolowania stanu pinów
import time              # Biblioteka odpowiedzialna za reprezentację czasu

if __name__ == "__main__":
    GPIO.setwarnings(False)              # Ignorowanie ostrzeżeń
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(19, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)              # WAŻNY KROK — ustawiamy, jaką numerację pinów wykorzystamy

    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Wejście na pinie 17 z podciągnięciem do plusa
    GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)  

    dioda1 = 0
    dioda2 = 0
    dioda3 = 0
    dioda4 = 0

    while True:
        if GPIO.input(17) == 0:
            time.sleep(0.5)
            if dioda1 == 0:
                dioda1 = 1
                GPIO.output(19, GPIO.HIGH)
            else: 
                dioda1 = 0
                GPIO.output(19, GPIO.LOW)

        if GPIO.input(4) == 0:
            time.sleep(0.5)
            if dioda2 == 0:
                dioda2 = 1
                GPIO.output(18, GPIO.HIGH)
            else: 
                dioda2 = 0
                GPIO.output(18, GPIO.LOW)
        
        if GPIO.input(3) == 0:
            time.sleep(0.5)
            if dioda3 == 0:
                dioda3 = 1
                GPIO.output(13, GPIO.HIGH)
            else: 
                dioda3 = 0
                GPIO.output(13, GPIO.LOW)
        
        if GPIO.input(2) == 0:
            time.sleep(0.5)
            if dioda4 == 0:
                dioda4 = 1
                GPIO.output(12, GPIO.HIGH)
            else: 
                dioda4 = 0
                GPIO.output(12, GPIO.LOW)
                break


    GPIO.cleanup()  # Na koniec programu — sprzątanie
