"""I will read in a file containing rows with each 5 digits separated by space.
I will read in each row and append it to a list.
The goal is to check if these conditions are met:
The digits in each row is either declining or increasing with 1, 2 or 3 steps.
If the requirements are met, a counter named safe will be increased by 1.
Part 2 is the implementation of a problem dampener, where the unsafe reports
will be checked if they can be removed and fulfill the requirements of the task.
If so, those reports will be added as safe reports. I separated these two parts
as a 2-step process, because the problem dampener will only be used if there are
unsafe reports. And because task 2 came after task 1 was done :)"""

import os
import sys

# Setting the root directory to the parent directory, i am placing all inputs in a folder called inputs
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def main():
    # Part 1 of the task
    #with open('inputs/inputday2example.txt') as inputdaytwo:
    with open('inputs/inputday2.txt') as inputdaytwo:
        safe = 0
        unsafe = 0
        unsafe_reports = {}  # Storing the unsafe reports in a dictionary for handling in part 2 of the test
        row_nr = 0
        
        for lines in inputdaytwo:
            row_nr += 1
            reports = lines.strip().split()
            reports = [int(i) for i in reports]
            #print(reports)  # Used for testing
            
            is_increasing = all((reports[i + 1] - reports[i]) in [1, 2, 3] for i in range(len(reports) - 1))
            is_decreasing = all((reports[i] - reports[i + 1]) in [1, 2, 3] for i in range(len(reports) - 1))
            
            if is_increasing or is_decreasing:
                safe += 1
            else:
                unsafe += 1
                unsafe_reports.update({row_nr: reports}) # Storing the row number and the report in a dictionary
                #print(unsafe_reports)  # Used for testing

        inputdaytwo.close()

        if unsafe_reports:
            problem_dampener = 0
            for key, value in unsafe_reports.items():
                for i in range(len(value)):
                    modified_report = value[:i] + value[i+1:]
                    is_increasing = all((modified_report[j + 1] - modified_report[j]) in [1, 2, 3] for j in range(len(modified_report) - 1))
                    is_decreasing = all((modified_report[j] - modified_report[j + 1]) in [1, 2, 3] for j in range(len(modified_report) - 1))
                    
                    if is_increasing or is_decreasing:
                        problem_dampener += 1
                        print(f"By removing {value[i]} from row {key}, the sequence becomes {'increasing' if is_increasing else 'decreasing'}: {modified_report}")
                        break
                
            
        
        print(f"The number of unsafe reports are {unsafe}")
        print(f"The number of safe reports are {safe}")
        print (f"The problem dampener has found {problem_dampener} more safe reports")
        print(f"The total number of safe reports are now {safe + problem_dampener}")
        print(f"The total number of unsafe reports are now {unsafe - problem_dampener}")

if __name__ == "__main__":
    main()