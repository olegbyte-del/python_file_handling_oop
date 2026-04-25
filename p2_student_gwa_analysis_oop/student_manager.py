# Student Manager

import random
import os

class StudentGenerator:
    
    """Handles the creation and deletion of student records stored in a text file.
        Each record contains a randomly generated student name and GWA."""
    filename = "students_list.txt"
    
    def generate_student_file():
        """Generate 20 random students records and writes them to a text file"""

        students = []
        
        first_names = [
            "Juan", "Maria", "Pedro", "Ana", "Mark",
            "Carla", "John", "Elena", "Jose", "Sofia",
            "Miguel", "Paula", "Daniel", "Angela", "Kevin",
            "Nicole", "Ryan", "Gabriela", "Patrick", "Isabella"
        ]

        last_names = [
            "Cruz", "Santos", "Reyes", "Lopez", "Garcia",
            "Gomez", "Ramos", "Martinez", "Fernandez", "Rivera"
        ]
    
        for _ in range(20): 
            name = f"{random.choice(first_names)} {random.choice(last_names)}"
            gwa = round(random.uniform(1.00, 3.00), 2)
            students.append((name, gwa))
        
        with open(StudentGenerator.filename, "w") as file:
            for name, gwa in students:
                file.write(f"{name}, {gwa}\n")

    def remove_files():
        """Deletes the student file if it exist"""
        
        if os.path.exists(StudentGenerator.filename):
            os.remove(StudentGenerator.filename)
            print(f"{StudentGenerator.filename} deleted.")
            
class StudentAnalysis():
    """Process student records from a file and performs analysis"""
    def __init__(self, filename = "students_list.txt"):
        self.filename = filename
        self.students = []
    
    def highest(self):
        """Read studen records from file and determines the student with the highest gwa"""
        
        self.highest_gwa = None
        self.highest_student = ""
        with open(self.filename, "r") as file:
            for line in file:
                student_record = line.strip().split(",")
                self.students.append((student_record[0], float(student_record[1])))
                
        for name, grade in self.students:
            if self.highest_gwa is None or grade < self.highest_gwa: 
                self.highest_gwa = grade  
                self.highest_student = name
                
        print(f"{self.highest_student} is the top of the class! with a GWA of {self.highest_gwa}")