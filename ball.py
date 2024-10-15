import pygame
import sys
import math

class Ball:
    def __init__(self, x0, y0, v_x, v_y, a_x, a_y, radius, color):
        self.x0 = x0
        self.y0 = y0
        self.x = x0
        self.y = y0
        self.v_x = v_x
        self.v_y = v_y
        self.a_x = a_x
        self.a_y = a_y
        self.radius = radius
        self.color = color

    def update_position(self, dt, sx, sy):
        self.x += self.v_x * dt + 0.5 * self.a_x * dt**2
        self.y += self.v_y * dt + 0.5 * self.a_y * dt**2

        # Collision with ground
        if self.y + self.radius > sy:
            self.y = sy - self.radius

        # Collision with ceiling
        if self.y - self.radius < 0:
            self.y = 0 + self.radius

        # Collision with right wall
        if self.x + self.radius > sx:
            self.x = sx - self.radius

        # Collision with left wall
        if self.x - self.radius < 0:
            self.x = 0 + self.radius

    def update_velocity(self, dt):
        self.v_x += self.a_x * dt
        self.v_y += self.a_y * dt

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
