import string
import random


import nltk

from src.password_generator_base import PasswordGenerator
from src.Pin_pass_generator import PinPasswordGenerator
from src.Random_pass_generator import RandomPasswordGenerator


nltk.download('words')
    

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


if __name__ == "__main__":
    pin_generator = PinPasswordGenerator(length=8)
    print("PIN Password:", pin_generator.generate())

    random_generator = RandomPasswordGenerator(length=12)
    print("Random Password:", random_generator.generate())

    memorable_generator = MemorablePasswordGenerator(length=4)
    print("Memorable Password:", memorable_generator.generate())