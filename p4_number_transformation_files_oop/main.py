# Main Program

import integer_processor as ip 

analysis = ip.NumberAnalysis()
read = ip.FileManager()

while True:
    try:
        print("="*50, "Number Analysis".center(50), "="*50, sep="\n")
        print("[1] File Manager", 
            "[2] Number Analysis",
            "[0] Exit", "="*50, sep="\n")
        
        user_input = int(input())
        
        if user_input == 1:
            print("="*50, "File Manager".center(50), "="*50, sep="\n")
            print("[1] Create Random 20 Integer File", 
            "[2] Remove Integer File",
            "[3] Remove All Files",
            "[0] Exit", "="*50, sep="\n")
            
            user_choice = int(input())
            
            if user_choice == 1: 
                ip.FileManager.create_file()
            
            elif user_choice == 2:
                ip.FileManager.remove_file()
                
            elif user_choice == 3:
                ip.FileManager.remove_all_files()
            
            elif user_choice == 0:
                
                
            else:
                print("Invalid input!")
        
    except Exception as e:
        print(f"Error Occured! {e}")

