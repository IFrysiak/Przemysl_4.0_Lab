import pygame
import time
import ctypes
# from sensor import sensor_init, read_sensor

# Inicjalizacja czujnika
vl = ctypes.CDLL("/home/pi/Desktop/wt_Igor_Stefan/vl6180_pi/libvl6180_pi.so")
vl.vl6180_initialise.argtypes = [ctypes.c_int]
vl.vl6180_initialise.restype = ctypes.c_void_p
vl.get_distance.argtypes = [ctypes.c_void_p]
vl.get_distance.restype = ctypes.c_int
vl.get_ambient_light.argtypes = [ctypes.c_void_p, ctypes.c_int]
vl.get_ambient_light.restype = ctypes.c_float

dev = vl.vl6180_initialise(0)
GAIN = 6

# Inicjalizacja Pygame
pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("VL6180X Distance Visualization")
font = pygame.font.SysFont("Arial", 36)
clock = pygame.time.Clock()

# Główna pętla programu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    try:
        distance = vl.get_distance(dev)
        light = vl.get_ambient_light(dev, GAIN)
        time.sleep(0.35)
    except Exception:
        distance = 255
        light = 255


    radius1 = max(10, 250 - distance)
    color1 = (max(0, min(255, 255 - distance)), 100, max(0, min(255, distance)))

    radius2 = max(10, int(light))
    color2 = (100, 100, min(255, int(light * 10)))

    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, color1, (WIDTH // 3, HEIGHT // 2), radius1)
    text1 = font.render(f"{distance} mm", True, (255, 255, 255))
    screen.blit(text1, (WIDTH // 3 - text1.get_width() // 2, 50))

    pygame.draw.circle(screen, color2, (2 * WIDTH // 3, HEIGHT // 2), radius2)
    text2 = font.render(f"{light:.2f}", True, (255, 225, 255))
    screen.blit(text2, (2 * WIDTH // 3 - text2.get_width() // 2, 50))

    pygame.display.flip()
    clock.tick(3)

pygame.quit()
