# Number Generator & Seperator Program

import random 

class RandomNumberGenerator:
    """Generates random integers based on count, start, and end range."""
        
    def __init__(self, count, start, end):
        self.count = count
        self.start = start 
        self.end = end 
    
    def randint_gen(self):
        file_name = "numbers.txt"
        if self.count <= 0: 
            print("Count must be greate than 0")
            return
        if self.start > self.end: 
            print("Start must be less than or equal to end.")
            return
        
        number_file = [random.randint(self.start, self.end) for _ in range(self.count)]
        with open(file_name, "w") as file: 
            for num in number_file:
                file.write(str(num) + "\n")
            
        print(f"Succesfully created {file_name} containing 20 random integers")
        

class EvenNumberProcessor:
    """Process integers from a file and idenfity even numbers."""
    
    def __init__(self, input_file):
        self.input_file = input_file
        self.numbers = []
        self.even_numbers = []
        
    def read_file(self):
        try: 
            with open(self.input_file, "r") as file: 
                for line in file:
                    try:
                        self.numbers.append(int(line.strip()))
                    except Exception as e: 
                        print(f"Error occured! {e}")
                        
        except FileNotFoundError:
            print(f"Error: file '{self.input_file}' not found.")
                    
    def identify_even(self):
        if not self.numbers:
            print("No data to process.")
            return
        
        for num in self.numbers:
            if num % 2 == 0: 
                self.even_numbers.append(num)

    def save_list_even(self, output_file = "even.txt"): 
        self.read_file() 
        self.identify_even()
        try: 
            with open(output_file, "w") as file:
                for num in self.even_numbers:
                    file.write(str(num) + "\n")
                
            print(f"Succesfully created {output_file} containing {len(self.even_numbers)} even numbers.")
            
        except Exception as e: 
            print("Error occured! {e}")
            
class OddNumberProcessor(EvenNumberProcessor): 
    
    def __init__(self, input_file): 
        super().__init__(input_file)
        self.odd_numbers = []
    
    def identify_odd(self):
        if not self.numbers:
            print("No data to process.")
            return 
        
        for num in self.numbers:
            if num % 2 != 0: 
                self.odd_numbers.append(num)
    
    def save_list_odd(self, output_file = "odd.txt"):
        self.read_file()
        self.identify_odd()
        with open(output_file, "w") as file:
            for num in self.odd_numbers:
                file.write(str(num) + "\n")
        
        print(f"Succesfully created {output_file} containing {len(self.odd_numbers)} odd numbers.")
        