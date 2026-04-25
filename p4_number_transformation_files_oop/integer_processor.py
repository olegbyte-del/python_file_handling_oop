# Integer file processor

import random
import os

class FileManager:
    
    filename = "integers.txt"
    
    def read_file():
        number_list = []
        
        with open(FileManager.filename, "r") as file:
            for line in file:
                number_list.append(int(line.strip()))
        
        print(f"="*100, number_list, "="*100, sep="\n")
    
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

class NumberAnalysis():
    
    def even_analysis():
        even_count = 0
        even_numbers = []
        
        with open(FileManager.filename, "r") as file:
            for line in file:
                num = int(line.strip())
                
                if num % 2 == 0:
                    even_numbers.append(num)
                    even_count += 1
        
        print("="*50)
        print(f"Total number of even: {even_count}").center(50)
        print("="*50)
    
    def odd_analysis():
        odd_count = 0
        odd_numbers = []
        
        with open(FileManager.filename, "r") as file:
            for line in file:
                num = int(line.strip())
                
                if num % 2 != 0:
                    odd_numbers.append(num)
                    odd_count += 1
        
        print("="*50)
        print(f"Total number of odd: {odd_count}").center(50)
        print("="*50)