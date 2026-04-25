# Integer file processor

import random
import os

class FileManager:
    """Handles file creation, reading, and deletion for integer-based text files."""
    
    filename = "integers.txt"
    
    def read_file(self):
        """Reads integers from the file and returns them as a list."""
        number_list = []
        
        with open(FileManager.filename, "r") as file:
            for line in file:
                number_list.append(int(line.strip()))
        
        return number_list
    
    def create_file():
        """Creates a file with 20 random integers based on user-defined range."""
        count = 20
        random_numbers = []
        
        start = int(input("Number will start: "))
        end = int(input("Number will End: "))
        
        if start >= end:
            print("Invalid range! Start must be less than End.", "="*50, "Press enter to start again...", sep="\n")
            input("Press enter to continue")
            
        for _ in range(count):
                random_numbers.append(random.randint(start, end))
        
        with open(FileManager.filename, "w") as file: 
            for num in random_numbers:
                file.write(str(num) + "\n")
            
            print(f"{FileManager.filename} successfully created!")
            input("Press enter to continue")
            
    def remove_file():
        """Deletes the main integer file after user confirmation."""
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
    
    def remove_all_files():
        """Deletes all generated output files."""
        files = ["integers.txt", "double.txt", "triple.txt"]
        print(f"Are you sure you want to delete the corresponding files: {files} y/n")
        confirmation = input("").lower()
        
        if confirmation == "y": 
            for file in files:
                if os.path.exists(file):
                    os.remove(file)
                    print(f"Deleted: {file}")
                else:
                    print(f"File not found: {file}")
            
            print(f"Deletion of files finished.")
            
        elif confirmation == "n":
            print(f"Deletion cancelled..")
        else:
            print("Invalid input")

class NumberAnalysis(FileManager):
    """Performs statistical and transformation analysis on integer files."""
    
    def even_analysis(self):
        """Displays all even numbers and their count."""
        even_count = 0
        even_numbers = []
        
        with open(FileManager.filename, "r") as file:
            for line in file:
                num = int(line.strip())
                
                if num % 2 == 0:
                    even_numbers.append(num)
                    even_count += 1

        print("="*50)
        print(even_numbers)
        print("="*50)
        print(f"Total number of even: {even_count}".center(50))
        print("="*50)
    
    def odd_analysis(self):
        """Displays all odd numbers and their count."""
        odd_count = 0
        odd_numbers = []
        
        with open(FileManager.filename, "r") as file:
            for line in file:
                num = int(line.strip())
                
                if num % 2 != 0:
                    odd_numbers.append(num)
                    odd_count += 1
                    
        print("="*50)
        print(odd_numbers)
        print("="*50)
        print(f"Total number of odd: {odd_count}".center(50))
        print("="*50)
        
    def square_cube_analysis(self):
        """Creates files for squared even numbers and cubed odd numbers."""
        numbers = self.read_file()
        
        even_squared = []
        odd_cubed = []
        
        for num in numbers:
            if num % 2 == 0:
                even_squared.append(num ** 2)
            else: 
                odd_cubed.append(num ** 3)
                
        with open("double.txt", "w") as file:
            for num in even_squared:
                file.write(str(num) + "\n")
            
            print("="*100)
            print(f"Even Squared Integers:  {even_squared}")
            print("="*100)
            
        with open("triple.txt", "w") as file:
            for num in odd_cubed:
                file.write(str(num) + "\n")
            
            print("="*100)
            print(f"Odd Cubed Integers:  {odd_cubed}")
            print("="*100)
                
        print(f"Successfully created 'double.txt' and 'triple.txt'").center(50)
        print("="*50)
