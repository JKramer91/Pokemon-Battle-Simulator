import pygame
from constants import *
from game import GameState

def draw_main_menu(screen, font, main_menu_buttons):
    draw_main_menu_buttons(main_menu_buttons)
    draw_main_menu_text(screen, font, (0,0,0), 200, 360)

def draw_main_menu_buttons(main_menu_buttons):
    for button in main_menu_buttons:
         button.draw()

def draw_main_menu_text(screen, font, color, x, y):
    img = font.render("Welcome to Jonas' Pokémon Battle Simulator. Please choose the Pokémon you want for the battle!", True, color)
    screen.blit(img, (x, y))
     
def draw_game(screen, game_buttons, player_pokemon, enemy_pokemon, player_healthbar, enemy_healthbar):
    for button in game_buttons:
            button.draw()
    draw_healthbars(screen, player_healthbar, enemy_healthbar)
    draw_pokemon(screen, player_pokemon, enemy_pokemon)

def draw_healthbars(screen, player, enemy):
     player.draw(screen)
     enemy.draw(screen)

def draw_pokemon(screen, player_pokemon, enemy_pokemon):
    player_sprite = pygame.image.load(f"assets/sprites/{player_pokemon.name}_back.png").convert_alpha()
    enemy_sprite = pygame.image.load(f"assets/sprites/{enemy_pokemon.name}.png").convert_alpha()

    # Scale the sprites
    scaled_player_sprite = pygame.transform.smoothscale(player_sprite, (350, 350)) 
    scaled_enemy_sprite = pygame.transform.smoothscale(enemy_sprite, (350, 350))

    _, player_height = scaled_player_sprite.get_size()
    enemy_width, _ = scaled_enemy_sprite.get_size()

    player_pos = (50, SCREEN_HEIGHT - player_height + 30)
    enemy_pos = (SCREEN_WIDTH - enemy_width - 175, 280)
     
    screen.blit(scaled_player_sprite, player_pos)
    screen.blit(scaled_enemy_sprite, enemy_pos)

def draw_game_over(screen, font, game, game_buttons):
    game_buttons[0].draw()
    draw_game_over_text(screen, font, (0,0,0), 420, 360, game)

def draw_game_over_text(screen, font, color, x, y, game):
    if game.game_state == GameState.WON:
        img = font.render("Congratulations, you won the game! Want to play again?", True, color)
        screen.blit(img, (x, y))
    else:
        img = font.render("You lost the game! Want to try again?", True, color)
        screen.blit(img, (x, y))