import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 2
GREEN = (34, 156, 130)
BLUE = (20, 67, 200)
LIGHTRED = (255, 70, 55)
LIGHTBLUE = (55, 70, 255)
GREY = (30, 30, 30)

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
rect_pos = pygame.Rect(100, 100, 200, 350)
flipping = False
flip_progress = 0
flip_count = 0

while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if rect_pos.collidepoint(event.pos) and not flipping:
                flipping = True
                flip_progress = 0

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(BLUE)

    # Draw the circle
    pygame.draw.circle(screen, GREEN, player_pos, 40)

    # Draw the rectangle and handle flipping
    if flipping:
        flip_progress += dt * 2  # Control the speed of the flip
        if flip_progress >= 1:
            flip_progress = 0
            flip_count += 1
            if flip_count == 2:
                flipping = False
                flip_count = 0

        scale = abs(flip_progress - 0.5) * 2
        new_width = rect_pos.width * scale
        new_rect = pygame.Rect(rect_pos.centerx - new_width / 2, rect_pos.y, new_width, rect_pos.height)
        
        if flip_count == 0:
            pygame.draw.rect(screen, GREY, new_rect)
        else:
            pygame.draw.rect(screen, LIGHTBLUE, new_rect)
            
    else:
        pygame.draw.rect(screen, LIGHTRED, rect_pos)

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    dt = clock.tick(60) / 1000

pygame.quit()
