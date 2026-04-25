# Main Program

import text_file_writer as tf

while True:
    try:
        print("="*50, "Text Writer Program".center(50), "="*50, sep="\n")
        print("[1] Create file",
            "[0] Exit", "="*50, sep="\n")
        
        user_input = int(input())
        
        if user_input == 1:
            tf.FileManager.create_file()
            print(f"Press enter to continue...")
        
        elif user_input == 0:
            print("Exiting the program...")
            break
        
        else:
            print("Invalid input! Try again.")
    
    except Exception as e:
        print(f"Error Occured! {e}")
