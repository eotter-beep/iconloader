# iconloader.py
import pygame
import os

def load_icon(path, convert_alpha=True):
    """
    Load an icon image using Pygame.
    
    Args:
        path (str): Path to the image file.
        convert_alpha (bool): Whether to use convert_alpha() for transparency.
        
    Returns:
        pygame.Surface: The loaded image.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Icon not found: {path}")
    
    image = pygame.image.load(path)
    if convert_alpha:
        image = image.convert_alpha()
    else:
        image = image.convert()
    return image
