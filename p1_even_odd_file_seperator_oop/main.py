# Main Program

from number_generator_seperator import RandomNumberGenerator
from number_generator_seperator import EvenNumberProcessor

random = RandomNumberGenerator(20, 1, 100)
numbers = random.randint_gen()

file = EvenNumberProcessor("even_numbers.txt")
file.read_file()

print(file.numbers)
