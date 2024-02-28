# This file is for use with the Basic Math for Data Analysis course
# If you cannot see the console, choose View -> Show Console from the menu above this tab
# Type or copy/paste any code that you would like to run.
# We'll be using the statistics library later in the course one function at a time.
# If you would like to use more than one function, you can separate them with commas.
# For example: from statistics import mean, median, mode
# To run the code type the following command in the Console:  python basic_math.py

#MIN
test_grades = [98, 100, 54, 70, 83, 83, 75, 68, 83, 91, 75]
min_grade = min(test_grades)
print(f"The minimum grade is: {min_grade}")
#MAX
test_grades = [98, 100, 54, 70, 83, 83, 75, 68, 83, 91, 75]
max_grade = max(test_grades)
print(f"The maximum grade is: {max_grade}")
#SORT
test_grades = [54, 68, 70, 75, 75, 83, 83, 83, 91, 98, 100]
test_grades.sort()
print(test_grades)

essay_grades = [93, 97, 84, 91, 87, 68, 63, 72, 75, 89]
essay_grades.sort()
print(essay_grades)
#MEDIAN
from statistics import median

test_grades = [98, 100, 54, 70, 83, 83, 75, 68, 83, 91, 75]
essay_grades = [93, 97, 84, 91, 87, 68, 63, 72, 75, 89]

median_grade = median(test_grades)
median_essay = median(essay_grades)
print(f"The median test grade is: {median_grade}")
print(f"The median essay grade is: {median_essay}")
#MODE
from statistics import mode

test_grades = [98, 100, 54, 70, 83, 83, 75, 68, 83, 91, 75]
test_mode = mode(test_grades)
print(f"The most often seen grade is: {test_mode}")
#MULTIMODE
from statistics import multimode

project_grades = [80, 75, 68, 80, 92, 84, 77, 100, 100, 88, 82]
project_mode = multimode(project_grades)
print(f"The most often seen project grade is: {project_mode}")
#MEAN==AVERAGE
from statistics import mean

test_grades = [98, 100, 54, 70, 83, 83, 75, 68, 83, 91, 75]
essay_grades = [63, 68, 72, 75, 84, 87, 89, 91, 93, 97]

test_average = mean(test_grades)
essay_average = mean(essay_grades)

print(f"The average test grade is: {test_average}")
print(f"The average essay grade is: {essay_average}")

#PERCENTAGE - USE A FOR LOOP TO ITERATE WITH EACH ELEMENT
test_grades = [98, 100, 54, 70, 83, 83, 75, 68, 83, 91, 75]

passed = 0
total_grades = len(test_grades)

for grade in test_grades:
    if grade >= 70:
        passed += 1

percentage_passed = round(passed / total_grades * 100)
        
print(f"The number of students who passed: {passed}")
print(f"The number of students who did not pass: {total_grades - passed}")
print(f"The percentage of students who passed: {percentage_passed}")
print(f"The percentage of students who did not pass: {100 - percentage_passed}")