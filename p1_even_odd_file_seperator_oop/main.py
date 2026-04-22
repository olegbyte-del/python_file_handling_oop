# Main Program

from number_generator_seperator import RandomNumberGenerator
from number_generator_seperator import EvenNumberProcessor

random = RandomNumberGenerator(20, 1, 100)
numbers = random.randint_gen()

with open("numbers.txt", "w") as file:
    for num in numbers:
        file.write(str(num) + "\n")

        
file = EvenNumberProcessor("numbers.txt")
file.read_file()
print(file.numbers)