# Student Manager

import random

class StudentGenerator:
    
    def generate_student_file(filename = "students_list.txt"):
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
        
        with open(filename, "w") as file:
            for name, gwa in students:
                file.write(f"{name}, {gwa}\n")
            