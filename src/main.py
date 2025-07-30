import pygame
from constants import *
from button import Button
from scenes import draw_game
from uimanager import UIManager
from scenemanager import SceneManager
from game import Game
import time

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption("Pokémon Battle Simulator")
    background = pygame.image.load("assets/background/background.png")
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    scene_manager = SceneManager()
    ui_manager = UIManager()
    game = Game()

    while True:
        Button.set_screen_and_font(screen, font)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("white")
        screen.blit(background, (0,0))

        if scene_manager.current_scene == "main_menu":
            ui_manager.draw_main_menu(screen, font)
            was_clicked, pokemon = ui_manager.is_pokemon_clicked()
            
            # Flip the display once such that the user can see the button going dark gray indicating a button press
            pygame.display.flip()

            if was_clicked:
                scene_manager.has_player_chosen = True

            if scene_manager.has_player_chosen:
                game.setup(pokemon)
                ui_manager.create_game_buttons(game.player_pokemon.moves)
                scene_manager.go_to("battle")
                
        else:
            draw_game(screen, ui_manager.game_buttons, game.player_pokemon, game.enemy_pokemon, game.player_healthbar, game.enemy_healthbar)
            
            #if ui_manager.game_buttons[1].check_click():
            #    print("Testing that it works")
            
            # If the "Main Menu"-button is clicked, switch to main menu scene
            if ui_manager.is_main_menu_button_clicked():
                scene_manager.go_to("main_menu")
                scene_manager.has_player_chosen = False

        pygame.display.flip()

if __name__ == "__main__":
    main()