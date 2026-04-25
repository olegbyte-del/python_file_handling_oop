# Integer file processor

import random

class FileManager:
    
    filename = "integers.txt"
    
    def create_file(self, count = 20):
        random_numbers = []
        
        start = int(input("Number will start: "))
        end = int(input("Number will End: "))
        
        for _ in range(count):
                random_numbers.append(random.randint(start, end))
        
        with open(FileManager.filename, "w") as file: 
            