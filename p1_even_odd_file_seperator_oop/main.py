# Main Program
from number_generator_seperator import RandomNumberGenerator
from number_generator_seperator import EvenNumberProcessor
from number_generator_seperator import OddNumberProcessor

while True:
    try:
        print("="*50)
        print("Number Processing System".center(50))
        print("="*50)

        print("[1] Generate Numbers + file")
        print("[2] Process Even Numbers")
        print("[3] Process Odd Numbers")
        print("[0] Exit")
        print("="*50)

        user_input = input("Please enter your choice: ")

        if not user_input.isdigit():
            print("Invalid input. Try again.")
            continue

        user_input = int(user_input)

        if user_input == 1:
            number_list = []
            start_number = int(input("Starting point: "))
            end_number = int(input("End point: "))

            generator = RandomNumberGenerator(20, start_number, end_number)
            generator.randint_gen()

            with open("numbers.txt", "r") as file:
                for line in file:
                    number_list.append(int(line.strip()))
                    
            print("="*50)
            print(number_list)

            input("\nPress Enter to continue...")
        
        elif user_input == 2:
            print("="*50, "Options".center(50), "="*50, sep = "\n")
            print("[1] Identify even",
                "[2] Identify even + create file",
                "[3] back", "="* 50, sep="\n")
            
            user_choice = int(input())
            
            even_processor = EvenNumberProcessor("numbers.txt")
                        
            if user_choice == 1:
                even_processor.read_file()
                even_processor.identify_even()
                print("Even numbers:", even_processor.even_numbers)
            
            elif user_choice == 2: 
                even_processor.save_list_even()
                list_even = even_processor.readfile("even.txt")
                print("Even numbers:", even_processor.even_numbers)
            
            elif user_choice == 3:
                pass
                
        elif user_input == 0:
            print("Exiting the program...")
            break

        else:
            print("Invalid choice try again...")

    except Exception as e:
        print(f"Error occurred: {e}")
        input("Press Enter to continue...")