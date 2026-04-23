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
