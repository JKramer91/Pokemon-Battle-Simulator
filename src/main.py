import pygame
from constants import *
from button import Button
from pokemon import Pokemon
from scenes import draw_main_menu, draw_game, draw_main_menu_text
from api import get_pokemon_data, extract_attributes

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption("Pokémon Battle Simulator")
    background = pygame.image.load("assets/background/background.png")

    main_menu = True
    has_player_chosen = False
    player_pokemon = None
    enemy_pokemon = None
    game_buttons = None

    while True:
        Button.set_screen_and_font(screen, font)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("white")
        screen.blit(background, (0,0))

        if main_menu:
            main_menu_buttons = Button.create_main_menu_buttons()
            draw_main_menu(main_menu_buttons)
            draw_main_menu_text(screen, font, (0,0,0), 220, 150)

            if main_menu_buttons[0].check_click():
                has_player_chosen = True

            if has_player_chosen:
                player_data = get_pokemon_data("pikachu")
                attributes = extract_attributes(player_data)
                enemy_data = get_pokemon_data("charmander")
                enemy_attributes = extract_attributes(enemy_data)
                player_pokemon = Pokemon(attributes)
                enemy_pokemon = Pokemon(enemy_attributes)
                game_buttons = Button.create_game_buttons(attributes["moves"])

                main_menu = False
        else:
            draw_game(screen, game_buttons, player_pokemon, enemy_pokemon)

            # If the "Main Menu"-button is clicked, switch to main menu scene
            if game_buttons[0].check_click():
                main_menu = True
                has_player_chosen = False

        pygame.display.flip()


if __name__ == "__main__":
    main()