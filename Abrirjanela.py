import pygame

def main():
    pygame.init()
    pygame.display.set_caption("Oi, sou o Pygame.")
    screen = pygame.display.set_mode((800,600))
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = false

if __name__ == "__main__":
    main()