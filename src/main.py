import pygame
from constants import *
from button import Button
from pokemon import Pokemon
from scenes import draw_game
from api import get_pokemon_data, extract_attributes
from uimanager import UIManager
from healthbar import HealthBar
from scenemanager import SceneManager

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption("Pokémon Battle Simulator")
    background = pygame.image.load("assets/background/background.png")
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    scene_manager = SceneManager()
    ui_manager = UIManager()
    player_pokemon = None
    enemy_pokemon = None

    while True:
        Button.set_screen_and_font(screen, font)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("white")
        screen.blit(background, (0,0))

        if scene_manager.current_scene == "main_menu":
            ui_manager.draw_main_menu(screen, font)
            was_clicked, pokemon = ui_manager.is_main_menu_button_clicked()
            
            # Flip the display once such that the user can see the button going dark gray indicating a button press
            pygame.display.flip()

            if was_clicked:
                scene_manager.has_player_chosen = True

            if scene_manager.has_player_chosen:
                player_data = get_pokemon_data(pokemon)
                attributes = extract_attributes(player_data)
                enemy_data = get_pokemon_data("charmander")
                enemy_attributes = extract_attributes(enemy_data)
                player_pokemon = Pokemon(attributes)
                enemy_pokemon = Pokemon(enemy_attributes)
                player_healthbar = HealthBar(125, 420, 200, 20, player_pokemon.current_hp)
                enemy_healthbar = HealthBar(755, 245, 200, 20, player_pokemon.current_hp)
                ui_manager.create_game_buttons(attributes["moves"])
                scene_manager.go_to("battle")
        else:
            draw_game(screen, ui_manager.game_buttons, player_pokemon, enemy_pokemon, player_healthbar, enemy_healthbar)

            # If the "Main Menu"-button is clicked, switch to main menu scene
            if ui_manager.is_game_button_clicked():
                scene_manager.go_to("main_menu")
                scene_manager.has_player_chosen = False

        pygame.display.flip()


if __name__ == "__main__":
    main()