# Main program

import student_manager as sm 

analysis = sm.StudentAnalysis()

while True:
    try:
        print("="*50, "Faculty Panel".center(50), "="*50, sep="\n")
        print("[1] Create Random student record",
            "[2] Analyze Highest Student", 
            "[3] Exit", "="*50, sep = "\n")
        
        user_input = int(input())
        
        if user_input == 1:
            sm.StudentGenerator.generate_student_file()
            
            print("="*50)
            with open("students_list.txt", "r") as file:
                for line in file:
                    print(line.strip())
            print("="*50)
            
            input("Press enter to go back.")
        
        
    except Exception as e:
        print(f"Error Occured! {e}")
        

