import pygame
from constants import *
from button import Button
from scenes import *
from uimanager import UIManager
from scenemanager import SceneManager, Scene
from game import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption("Pokémon Battle Simulator")
    background = pygame.image.load("assets/background/background.png")
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    scene_manager = SceneManager()
    Button.set_screen_and_font(screen, font)
    ui_manager = UIManager()
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("white")
        screen.blit(background, (0,0))

        if scene_manager.current_scene == Scene.MAIN_MENU:
            draw_main_menu(screen, font, ui_manager.main_menu_buttons)
            was_clicked, pokemon = ui_manager.is_pokemon_clicked()
            # Flip the display once such that the user can see the button going dark gray indicating a button press
            pygame.display.flip()

            if was_clicked:
                scene_manager.has_player_chosen = True

            if scene_manager.has_player_chosen:
                game.setup(pokemon)
                ui_manager.create_game_buttons(game.player_pokemon.moves)
                scene_manager.go_to(Scene.BATTLE_SCREEN)
        elif scene_manager.current_scene == Scene.GAME_OVER:
            draw_game_over(screen, font, game, ui_manager.game_buttons)
            if ui_manager.is_main_menu_button_clicked():
                scene_manager.go_to(Scene.MAIN_MENU)
                scene_manager.has_player_chosen = False
        else:
            draw_game(screen, ui_manager.game_buttons, game.player_pokemon, game.enemy_pokemon, game.player_healthbar, game.enemy_healthbar)
            game.game_on(ui_manager)
            if game.is_game_over:
                scene_manager.go_to(Scene.GAME_OVER)
            
            # If the "Main Menu"-button is clicked, switch to main menu scene
            if ui_manager.is_main_menu_button_clicked():
                scene_manager.go_to(Scene.MAIN_MENU)
                scene_manager.has_player_chosen = False

        pygame.display.flip()

if __name__ == "__main__":
    main()