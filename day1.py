"""Part 1: The goal is to read a file and extract two lists of numbers and
then sort them from loweest to highest, then
compare the numbers on each position. The difference between
the numbers will be added to a new list (Distance). The sum of the new list
will be printed out.
Part2: The goal is to use the same lists of numbers, but this time i will check how many times the numbers 
in the first column exists in the second column. The value in the first column will be multiplied by the 
number of times it exists in the second column. This new value will be added to a new list (similarity_score)
and the sum of the new list will be printed out.
"""

import os
import sys

# Setting the root directory to the parent directory, i am placing all inputs in a folder called inputs
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def main():
    # To try the logic i use the examples provided in the task, but to get the correct answer i will use the input file
    #with open ('inputs/inputday1example.txt') as inputdayone:
    with open('inputs/inputday1.txt') as inputdayone:
        firstcolumn = []
        secondcolumn = []
        distance = []

        for line in inputdayone:
            first, second = line.strip().split()
            firstcolumn.append(int(first))
            secondcolumn.append(int(second))

        inputdayone.close()
        #print(firstcolumn) # Used for testing
        #print(secondcolumn) # Used for testing

    firstcolumn.sort()
    secondcolumn.sort()
    #print(firstcolumn) # Used for testing
    #print(secondcolumn) # Used for testing

    # Part 1 of the task finding the distance between the numbers in the two columns
    for i in range(len(firstcolumn)):
        distance.append(abs(firstcolumn[i] - secondcolumn[i]))

    #print(distance) # Used for testing
    print(f"The total distance is {sum(distance)}")

    #Part 2 of the task finding the similarity score between the numbers in the two columns
    similarity_score = []
    for i in range(len(firstcolumn)):
        similarity_score.append(firstcolumn[i] * secondcolumn.count(firstcolumn[i]))
        
    print(similarity_score)
    print(f"The similarity score is {sum(similarity_score)}")


if main() == '__main__':
    main()
        
    
    


