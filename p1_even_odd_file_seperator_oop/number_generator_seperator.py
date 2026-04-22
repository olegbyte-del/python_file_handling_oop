# Number Generator & Seperator Program

import random 

class RandomNumberGenerator:
    """Generates random integers based on count, start, and end range."""
        
    def __init__(self, count, start, end):
        self.count = count
        self.start = start 
        self.end = end 
    
    def randint_gen(self):
        return [random.randint(self.start, self.end) for _ in range(self.count)]

class EvenNumberProcessor:
    """Identifies if a number is an even number from the list of numbers"""

    def __init__(self, input_file):
        self.input_file = input_file
        self.numbers = []
        self.even_numbers = []
        
    def read_file(self):
        with open(self.input_file, "r") as file: 
            for line in file:
                num = int(line.strip())
                self.numbers.append(num) 
    
