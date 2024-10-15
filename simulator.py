from ball import Ball
import pygame
import sys
import math

# Initialize Pygame
pygame.init()
Sx, Sy = 800, 600
screen = pygame.display.set_mode((Sx, Sy))
clock = pygame.time.Clock()

# Initialize font
font = pygame.font.SysFont(None, 24)

# Reset function
def reset():
    global t, ball
    t = 0
    # x0, y0, v_x, v_y, a_x, a_y, radius, color
    ball = Ball(Sx/2, Sy/2, 10, 0, 0, 9.81, 2, [255, 0, 0])

t = 0
dt = 1

reset()

# Simulation loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if reset_button.collidepoint(mouse_pos):
                reset()
    
    t += dt

    # Calculate new vectors
    ball.update_velocity(dt)
    ball.update_position(dt, Sx, Sy)

    # Render position and velocity text
    pos_text = f'Position: ({int(ball.x)}, {int(ball.y)})'
    vel_text = f'Velocity: ({int(ball.v_x)}, {int(ball.v_y)})'
    pos_surface = font.render(pos_text, True, (255, 255, 255))
    vel_surface = font.render(vel_text, True, (255, 255, 255))

    x0_text = f'x0: ({ball.x0})'
    y0_text = f'y0: ({ball.y0})'
    x0_surface = font.render(x0_text, True, (255, 255, 255))
    y0_surface = font.render(y0_text, True, (255, 255, 255))

    pygame.draw.rect(screen, (0, 0, 0), (10, 10, 200, 50))
    pygame.draw.rect(screen, (0, 0, 0), (700, 50, 100, 40))
    
    # Blit text surfaces onto the screen
    screen.blit(pos_surface, (10, 10))
    screen.blit(vel_surface, (10, 30))
    screen.blit(x0_surface, (700, 50))
    screen.blit(y0_surface, (700, 70))

    # Draw reset button
    reset_button = pygame.draw.rect(screen, (255, 0, 0), (700, 10, 80, 30))
    reset_text = font.render('Reset', True, (255, 255, 255))
    screen.blit(reset_text, (715, 15))

    # Update display
    if ball.x+ball.radius > 0+1 and ball.x+ball.radius < 800-1 and ball.y-ball.radius> 0+1 and ball.y+ball.radius < 600-1:
        ball.draw(screen)
    pygame.display.flip()
    clock.tick(10)

pygame.quit()
