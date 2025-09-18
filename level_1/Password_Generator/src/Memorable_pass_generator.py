from src.password_generator_base import PasswordGenerator

import random


class MemorablePasswordGenerator(PasswordGenerator):
    """Memorable password generator.

    Args:
        PasswordGenerator (ABC): Abstract base class for password generators.
    """
    def __init__(self, length: int = 4, word_list: list = None, upper: float = 0.5):
        if word_list is None:
            word_list = nltk.corpus.words.words()
        self.length = length
        self.word_list = word_list
        self.upper = upper

    def generate(self) -> str:
        word = [random.choice(self.word_list) for _ in range(self.length)] # Generate a list of random words
        # upper words based on the upper probability
        for i, w in enumerate(word):
            if random.random() < self.upper:
                word[i] = w.upper()
        return '-'.join(word)