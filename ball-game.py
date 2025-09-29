import pygame
import serial
import sys

# Connect to Arduino (change COM3 to your port, e.g. /dev/ttyUSB0 on Linux)
arduino = serial.Serial('COM3', 9600, timeout=1)

pygame.init()

# Game window
window_size = (800, 600)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("MPU6050 Tilt Game")

# Background
background = pygame.image.load("bg.png")
background = pygame.transform.scale(background, window_size)

# Sounds
bounce_sound = pygame.mixer.Sound("bounce.mp3")

# Ball
ball = pygame.image.load("ball.png")  # make a small image like a ball/character
ball = pygame.transform.scale(ball, (50, 50))
ball_x, ball_y = 400, 300
ball_speed = 5

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Read Arduino data
    try:
        line = arduino.readline().decode('utf-8').strip()
        if "," in line:
            pitch, roll = map(float, line.split(","))
            
            # Map pitch/roll to movement
            if pitch < 0:   # tilt forward
                ball_y -= ball_speed
            elif pitch > 1: # tilt backward
                ball_y += ball_speed
            if roll < 0:    # tilt left
                ball_x -= ball_speed
            elif roll > 1:  # tilt right
                ball_x += ball_speed
    except:
        pass

    # Boundary check + sound
    if ball_x < 0: 
        ball_x = 0
        bounce_sound.play()
    if ball_x > window_size[0]-50: 
        ball_x = window_size[0]-50
        bounce_sound.play()
    if ball_y < 0: 
        ball_y = 0
        bounce_sound.play()
    if ball_y > window_size[1]-50: 
        ball_y = window_size[1]-50
        bounce_sound.play()

    # Draw
    window.blit(background, (0, 0))
    window.blit(ball, (ball_x, ball_y))
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
