import pygame


class Janela:
    def __init__(self, x, y, title):
        self.size = (x,y)
        self.title = title

 
def main():
    game = Janela(800,600,"Oi, sou o Pygame.")
    pygame.display.set_caption(game.title)
    pygame.display.set_mode(game.size)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = false

if __name__ == "__main__":
    pygame.init()
    main()