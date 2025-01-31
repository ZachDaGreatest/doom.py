import pygame
from map import map, find_num_matrix
from player import player

walls = []
find_num_matrix(1,walls)
print(walls)
guy = player()

pygame.init()

skybox = pygame.image.load('sky.png')
skybox = pygame.transform.scale(skybox, (800,300))

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("caster")

running = True
while running:
    #Draw background
    screen.fill((88,57,39))
    screen.blit(skybox, (0, 0))
    

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                guy.move_forward()
            if event.key == pygame.K_a:
                guy.move_left()
            if event.key == pygame.K_s:
                guy.move_backward()
            if event.key == pygame.K_d:
                guy.move_right()
            if event.key == pygame.K_RIGHT:
                guy.turn_right()
            if event.key == pygame.K_LEFT:
                guy.turn_left()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                guy.stop()
            if event.key == pygame.K_a:
                guy.stop()
            if event.key == pygame.K_s:
                guy.stop()
            if event.key == pygame.K_d:
                guy.stop()

    # Draw walls
    for pos in walls:
        pygame.draw.rect(screen, (255,255,255), (pos[0]*20, pos[1]*20, 20, 20))

    guy.pos_update()
    pygame.draw.rect(screen, (255,0,255), (guy.pos[0]*20, guy.pos[1]*20, 20, 20))

    # Draw score

    pygame.display.flip()
    pygame.time.Clock().tick(60)