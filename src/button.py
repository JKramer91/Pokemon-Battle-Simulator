import pygame
from constants import *
class Button:
    screen = None
    font = None

    def __init__(self, x, y, text, enabled):
        self.x = x
        self.y = y
        self.text = text
        self.enabled = enabled

    @classmethod
    def set_screen_and_font(cls, screen, font):
        cls.screen = screen
        cls.font = font

    @classmethod
    def create_buttons(cls, moves):
        row_x_start = (1280 - (2 * BUTTON_WIDTH + PADDING_X)) // 2
        row1_y = 720 - BOTTOM_OFFSET - (BUTTON_HEIGHT + PADDING_Y)
        row2_y = row1_y + BUTTON_HEIGHT + PADDING_Y
        
        buttons = [
        cls(row_x_start, row1_y, cls.capitalize(moves[0]["name"]), True),
        cls(row_x_start + BUTTON_WIDTH + PADDING_X, row1_y, cls.capitalize(moves[1]["name"]), True),
        cls(row_x_start, row2_y, cls.capitalize(moves[2]["name"]), True),
        cls(row_x_start + BUTTON_WIDTH + PADDING_X, row2_y, cls.capitalize(moves[3]["name"]), True),
        ]
        return buttons
    
    @staticmethod 
    def capitalize(text):
        arr = text.split("-")
        arr = [v.capitalize() for v in arr]
        return " ".join(arr)

    def draw(self):
        text_surface = self.font.render(self.text, True, 'black')
        rect = pygame.rect.Rect((self.x, self.y), (150, 50))
        
        text_rect = text_surface.get_rect(center=rect.center)
        if self.check_click():
            pygame.draw.rect(self.screen, 'dark gray', rect, 0, 5)
        else:
            pygame.draw.rect(self.screen, 'gray', rect, 0, 5)

        pygame.draw.rect(self.screen, 'black', rect, 2, 5)
        self.screen.blit(text_surface, text_rect)
    
    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        rect = pygame.rect.Rect((self.x, self.y), (150, 50))
        
        if left_click and rect.collidepoint(mouse_pos) and self.enabled:
            return True
        return False