from src.password_generator_base import PasswordGenerator
import random
import string


class PinPasswordGenerator(PasswordGenerator):
    """PIN password generator.

    Args:
        PasswordGenerator (ABC): Abstract base class for password generators.
    """
    def __init__(self, length: int = 8):
        self.length = length

    def generate(self) -> str:
        return ''.join([random.choice(string.digits) for _ in range(self.length)])