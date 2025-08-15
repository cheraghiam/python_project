from abc import ABC, abstractmethod
import string
import random


import nltk


nltk.download('words')



class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass


class PinPasswordGenerator(PasswordGenerator):
    def __init__(self, length: int = 8):
        self.length = length
    
    def generate(self):
        return ''.join([random.choice(string.digits) for _ in range(self.length)])
    

class RandomPasswordGenerator(PasswordGenerator):
    def __init__(self, length: int = 8, include_digits: bool = True, include_symbols: bool = True):
        self.length = length
        self.characters = string.ascii_letters
        if include_digits:
            self.characters += string.digits
        if include_symbols:
            self.characters += string.punctuation
        
    def generate(self):
        return ''.join([random.choice(self.characters) for _ in range(self.length)])
    

class MemorablePasswordGenerator(PasswordGenerator):
    def __init__(self, length: int = 4, word_list: list = None):
        if word_list is None:
            word_list = nltk.corpus.words.words()
        self.length = length
        self.word_list = word_list

    def generate(self):
        return '-'.join([random.choice(self.word_list) for _ in range(self.length)]) 
    

if __name__ == "__main__":
    pin_generator = PinPasswordGenerator(length=6)
    print("PIN Password:", pin_generator.generate())

    random_generator = RandomPasswordGenerator(length=12)
    print("Random Password:", random_generator.generate())

    memorable_generator = MemorablePasswordGenerator(length=3)
    print("Memorable Password:", memorable_generator.generate())