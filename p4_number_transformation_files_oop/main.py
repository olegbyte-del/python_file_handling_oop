# Main Program

# Main Program

import integer_processor as ip

analysis = ip.NumberAnalysis()

while True:
    try:
        print("="*50, "Number Analysis".center(50), "="*50, sep="\n")
        print("[1] File Manager",
            "[2] Number Analysis",
            "[0] Exit",
            "="*50, sep="\n")

        user_input = input("Enter choice: ")
        
        if user_input == "1":
            while True:
                print("="*50, "File Manager".center(50), "="*50, sep="\n")
                print("[1] Create Random 20 Integer File",
                    "[2] Remove Integer File",
                    "[3] Remove All Files",
                    "[0] Back",
                    "="*50, sep="\n")

                user_choice = input("Enter choice: ")

                if user_choice == "1":
                    ip.FileManager.create_file()
                    input("Press enter to continue...")

                elif user_choice == "2":
                    ip.FileManager.remove_file()
                    input("Press enter to continue...")

                elif user_choice == "3":
                    ip.FileManager.remove_all_files()
                    input("Press enter to continue...")

                elif user_choice == "0":
                    print("Returning to main menu...")
                    break

                else:
                    print("Invalid input!")

        elif user_input == "2":
            while True:
                print("="*50, "Number Analysis".center(50), "="*50, sep="\n")
                print("[1] Even Analysis",
                    "[2] Odd Analysis",
                    "[3] Square(Even) Cube(Odd) Analysis",
                    "[0] Back",
                    "="*50, sep="\n")

                user_choice = input("Enter choice: ")

                if user_choice == "1":
                    analysis.even_analysis()
                    input("Press enter to continue...")

                elif user_choice == "2":
                    analysis.odd_analysis()
                    input("Press enter to continue...")

                elif user_choice == "3":
                    analysis.square_cube_analysis()
                    input("Press enter to continue...")

                elif user_choice == "0":
                    print("Returning to main menu...")
                    break

                else:
                    print("Invalid input!")
                
        elif user_input == "0":
            print("Exiting the Program...")
            break

        else:
            print("Invalid input!")

    except Exception as e:
        print(f"Error Occured! {e}")