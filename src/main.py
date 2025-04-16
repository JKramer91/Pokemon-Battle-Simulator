import pygame
from constants import *
from button import Button
from pokemon import Pokemon
from api import get_pokemon_data, extract_attributes

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption("Pokémon Battle Simulator")
    
    # Testing
    data = get_pokemon_data("pikachu")
    attributes = extract_attributes(data)
    Button.set_screen_and_font(screen, font)
    buttons = Button.create_buttons(attributes["moves"])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("white")
        for button in buttons:
            button.draw()
        pygame.display.flip()


if __name__ == "__main__":
    main()