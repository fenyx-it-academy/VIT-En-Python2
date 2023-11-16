firstname = input('what is your firstname? ')
lastname = input('what is your last name? ')
student_number = int(input('what is your student number? '))
print('\nresult of courses ')

# i used a for loop here:
for names  in range(4):
     courses_names = input(f'what are the names of your courses? {names + 1} ')
     midterm_grades = float(input(f'what is your midterm grades {courses_names}? '))
     final_grades = float(input(f'what is your final grades ? {courses_names} '))
     year_end_average = (0.4 * midterm_grades) + (0.6 * final_grades)
     result = "FAILED" if year_end_average < 50 else "PASSED"
     print(f"{courses_names} ,{result}")

# exercise 2:
numbers = [42, 29, 17, 15, 10, 9, 6, 4, 2, 1]
total = 0
for x in numbers:
    total += x
average = total / len(numbers)
high_count = 0
low_count = 0
for x in numbers:
    if x > average:
        high_count += 1
    else:
        low_count += 1
print(f"Count of numbers higher than the average: {high_count}")
print(f"Count of numbers lower than the average: {low_count}")

# exercise3:
while True:
    first_number = int(input('what is your first number '))
    second_number = int(input('what is your second number'))
    first_number = int(first_number)
    second_number= int(second_number)
    odd_sum_num = sum(x for x in range(first_number, second_number + 1) if x % 2 != 0)
    print(f"sum of odd number between {first_number} and {second_number} is {odd_sum_num}")



