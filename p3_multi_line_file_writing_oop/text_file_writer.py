# File and line generator

class FileManager:

    filename = input("What will be the name of the file?: ") + ".txt"
    
    def create_file():
        with open(FileManager.filename, "w") as file:
            def enter_text():
                while True:
                    try:
                        user_input = input("Enter line: ")
                        file.write(user_input)
                        
                        additional_input = input("Are there more lines y/n?: ").lower()
                        
                        if additional_input == "y":
                            enter_text()
                        
                        elif additional_input == "n": 
                            print(f)
                    
                    except Exception as e:
                        print(f"Error Occured! {e}")
                
                
            
            