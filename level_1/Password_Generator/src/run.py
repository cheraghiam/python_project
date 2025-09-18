import string
import random


import nltk

nltk.download('words')

from src.Pin_pass_generator import PinPasswordGenerator
from src.Random_pass_generator import RandomPasswordGenerator
from src.Memorable_pass_generator import MemorablePasswordGenerator


if __name__ == "__main__":
    pin_generator = PinPasswordGenerator(length=8)
    print("PIN Password:", pin_generator.generate())

    random_generator = RandomPasswordGenerator(length=12)
    print("Random Password:", random_generator.generate())

    memorable_generator = MemorablePasswordGenerator(length=4)
    print("Memorable Password:", memorable_generator.generate())