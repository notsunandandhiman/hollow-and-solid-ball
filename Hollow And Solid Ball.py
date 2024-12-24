import pygame

pygame.init()

window = pygame.display.set_mode((500, 500))

window.fill((255, 255, 255))

Green = (0, 255, 0)

pygame.draw.circle(window, Green, (400, 400), 50)

pygame.draw.circle(window, Green, (200, 200), 50, 30)


pygame.display.update()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = False

pygame.quit()