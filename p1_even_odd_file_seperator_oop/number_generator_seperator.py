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
    
