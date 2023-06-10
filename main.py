import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the display window
width, height = 1000, 750
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Universe")

# Define colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GRAY = (128, 128, 128)
ORANGE = (255, 165, 0)
LIGHT_BLUE = (135, 206, 250)
DARK_GRAY = (169, 169, 169)
CYAN = (0, 255, 255)
BROWN = (139, 69, 19)

# Set up celestial bodies' properties
sun_radius = 50
sun_x, sun_y = width // 2, height // 2

planet_radius = [5, 10, 12, 20, 18, 16, 14]  # Radius of each planet
planet_distance = [100, 140, 180, 220, 280, 320, 360]  # Distance from the sun
planet_angle = [0, 0, 0, 0, 0, 0, 0]  # Initial angle for each planet
planet_colors = [GRAY, ORANGE, BLUE, RED, DARK_GRAY, CYAN, LIGHT_BLUE]  # Color for each planet
rotation_speeds = [0.5, 0.3, 0.2, 0.15, 0.1, 0.08, 0.05]  # Rotation speed for each planet

# Increase planet speeds by a factor of 10
rotation_speeds = [speed * 10 for speed in rotation_speeds]

# Set up asteroid belt properties
asteroid_belt_radius = 250  # Radius of the asteroid belt
asteroid_belt_thickness = 5  # Thickness of the asteroid belt
asteroid_belt_color = BROWN  # Color of the asteroid belt
asteroid_belt_angle = 0  # Initial angle for the asteroid belt
asteroid_belt_speed = 0.02  # Rotation speed for the asteroid belt

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)  # Limit the frame rate to 60 FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Draw the sun
    pygame.draw.circle(screen, YELLOW, (sun_x, sun_y), sun_radius)

    # Draw the planets
    for i in range(len(planet_radius)):
        # Calculate planet's position
        planet_x = sun_x + math.cos(math.radians(planet_angle[i])) * planet_distance[i]
        planet_y = sun_y + math.sin(math.radians(planet_angle[i])) * planet_distance[i]

        # Draw the planet
        pygame.draw.circle(screen, planet_colors[i], (int(planet_x), int(planet_y)), planet_radius[i])

        # Update the angle for the next frame
        planet_angle[i] += rotation_speeds[i]

    # Draw the asteroid belt
    for angle in range(0, 360, 10):
        belt_x = sun_x + math.cos(math.radians(angle + asteroid_belt_angle)) * asteroid_belt_radius
        belt_y = sun_y + math.sin(math.radians(angle + asteroid_belt_angle)) * asteroid_belt_radius
        pygame.draw.circle(screen, asteroid_belt_color, (int(belt_x), int(belt_y)), asteroid_belt_thickness)

    # Update the angle for the next frame
    asteroid_belt_angle += asteroid_belt_speed

    # Update the display
    pygame.display.flip()

# Quit the program
pygame.quit()