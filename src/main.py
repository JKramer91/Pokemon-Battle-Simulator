import pygame

def main():
    print("This is the very start of my Pokémon Battle Simulator")
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Pokémon Battle Simulator")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()


if __name__ == "__main__":
    main()