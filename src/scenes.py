import pygame
from constants import *

def draw_main_menu(main_menu_buttons):
    for button in main_menu_buttons:
         button.draw()

def draw_main_menu_text(screen, font, color, x, y):
    img = font.render("Choose a Pokémon for battle!", True, color)
    screen.blit(img, (x, y))
     

def draw_game(screen, player_buttons, player_pokemon, enemy_pokemon):
    for button in player_buttons:
            button.draw()
    draw_pokemon(screen, player_pokemon, enemy_pokemon)

def draw_pokemon(screen, player_pokemon, enemy_pokemon):
    player_sprite = pygame.image.load(f"assets/sprites/{player_pokemon.name}_back.png").convert_alpha()
    enemy_sprite = pygame.image.load(f"assets/sprites/{enemy_pokemon.name}.png").convert_alpha()

    # Scale the sprites
    scaled_player_sprite = pygame.transform.smoothscale(player_sprite, (500, 500)) 
    scaled_enemy_sprite = pygame.transform.smoothscale(enemy_sprite, (500, 500))

    _, player_height = scaled_player_sprite.get_size()
    enemy_width, _ = scaled_enemy_sprite.get_size()

    player_pos = (0, SCREEN_HEIGHT - player_height)
    enemy_pos = (SCREEN_WIDTH - enemy_width, 0)
     
    screen.blit(scaled_player_sprite, player_pos)
    screen.blit(scaled_enemy_sprite, enemy_pos)