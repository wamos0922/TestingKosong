from PIL import Image, ImageEnhance
import math
from typing import Generator, Tuple, Union

def load_image(path: str) -> Image.Image:
    """Loads an image from a file path."""
    return Image.open(path)