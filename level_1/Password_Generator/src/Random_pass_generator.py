from src.password_generator_base import PasswordGenerator

import string
import random


class RandomPasswordGenerator(PasswordGenerator):
    """Random password generator.

    Args:
        PasswordGenerator (ABC): Abstract base class for password generators.
    """
    def __init__(self, length: int = 8, include_digits: bool = True, include_symbols: bool = True):
        self.length = length
        self.characters = string.ascii_letters
        if include_digits:
            self.characters += string.digits
        if include_symbols:
            self.characters += string.punctuation

    def generate(self) -> str:
        return ''.join([random.choice(self.characters) for _ in range(self.length)])