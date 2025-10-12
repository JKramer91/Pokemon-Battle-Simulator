import pygame

_cache = {}

def get_sprite(name, back, size):
    key = (name, back, size)
    if key in _cache:
        return _cache[key]
    path = f"assets/sprites/{name}_back.png" if back else f"assets/sprites/{name}.png"
    img = pygame.image.load(path).convert_alpha()
    if size:
        img = pygame.transform.smoothscale(img, size)
        img = img.convert_alpha()
    _cache[key] = img
    return img
