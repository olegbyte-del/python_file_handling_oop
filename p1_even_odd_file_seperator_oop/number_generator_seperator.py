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
    
    def __init__(self, input_file):
        self.input_file = input_file
        self.numbers = []
        self.even_numbers = []
        
    def read_file(self):
        with open(self.input_file, "r") as file: 
            for line in file:
                num = int(line.strip())
                self.numbers.append(num) 
                
    def identify_even(self): 
        for num in self.numbers:
            if num % 2 == 0: 
                self.even_numbers.append(num)

    def save_list_even(self, output_file = "even_numbers.txt"): 
        self.read_file() 
        self.identify_even()
        with open(output_file, "w") as file:
            for num in self.even_numbers:
                file.write(str(num) + "\n")
                
        print(f"Succesfully Created {output_file} containing {len(self.even_numbers)} even numbers.")
        
        
                
