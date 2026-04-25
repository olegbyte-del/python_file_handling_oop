# File and line generator

class FileManager:

    filename = input("What will be the name of the file?: ") + ".txt"
        
    def create_file():
        count = 0 
        lines = []
            
        with open(FileManager.filename, "w") as file:
                
            while True:
                try:
                    user_input = input("Enter line: ")
                    file.write(user_input + "\n")
                    lines.append(user_input)
                    count += 1
                            
                            
                    additional_input = input("Are there more lines y/n?: ").lower()
                            
                    if additional_input == "n": 
                        print(f"Successfully created {FileManager.filename}!")
                        break
                        
                except Exception as e:
                    print(f"Error Occured! {e}")
                            
        print("="*50, "Lines Added".center(50), "="*50, sep="\n")
        for line in lines:
            print(line + "\n")
        print("="*50)
        print(f"Total lines: {count}".center(50))
        print("="*50)