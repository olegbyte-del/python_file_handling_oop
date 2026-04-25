# Integer file processor

import random
import os

class FileManager:
    
    filename = "integers.txt"
    
    def create_file():
        count = 20
        random_numbers = []
        
        start = int(input("Number will start: "))
        end = int(input("Number will End: "))
        
        for _ in range(count):
                random_numbers.append(random.randint(start, end))
        
        with open(FileManager.filename, "w") as file: 
            for num in random_numbers:
                file.write(str(num) + "\n")
            
            print(f"{FileManager.filename} successfully created!")
            
    def remove_file():
        print(f"Are you sure you want to delete '{FileManager.filename}'? y/n ")
        confirmation = input("").lower()
        
        if confirmation == "y":
            if os.path.exists(FileManager.filename):
                os.remove(FileManager.filename)
                print(f"Successfully deleted '{FileManager.filename}'.")
        
        elif confirmation == "n":
            return
        
        else:
            print("Invalid input!")