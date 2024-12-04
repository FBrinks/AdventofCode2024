"""My task is to identify a pattern in the input file and extract sequences that looks like this:
mul(#anydigit, #anydigit) and if the seguqence is found i will multiply the two number and sum up the products.
The sum of the new list will be printed out and this is the answer to the task.
Part 2 of the task is to find the sequences that don't start with don't() and sum up the products of the sequences."""

import os
import sys
import re # Used for regular expressions for easier sequence finding

# Setting the root directory to the folder where i have a folder for all input files
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def day3():
    # Reading in the input file as a string for easier sequence finding
    memory_content = open('inputs/inputday3.txt').read()
    #memory_content = open('inputs/inputday3example.txt').read() # Used for testing

    # Using regular expressions to find the sequences and extract the numbers for multiplication and summing up
    instruction_pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')

# Part I: I used a list comprehension to extract the numbers and multiply them and summing up the result
    result_part_1 = sum([int(instruction.group(1)) * int(instruction.group(2)) for instruction in instruction_pattern.finditer(memory_content)])
    print(result_part_1)

# Part II: I used a regular expression to find the sequences and extract the numbers for multiplication and summing up
    conditional_pattern = re.compile(r".+?(?=don?'?t?\(\)|\Z)", re.DOTALL) # Used to find the sequences that don't start with don't()
    memory_parts_match = conditional_pattern.findall(memory_content)
    result_part_2 = sum([sum([int(instruction.group(1)) * int(instruction.group(2)) for instruction in instruction_pattern.finditer(part)]) for part in memory_parts_match if not part.startswith("don't()")])
    print(result_part_2)
        
                

if __name__ == "__main__":
    day3()

# The correct answers is:
# Part 1 = 174336360
# Part 2 = 88802350    