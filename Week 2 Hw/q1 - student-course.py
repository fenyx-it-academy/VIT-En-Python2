# Question 1
courses = []
# first_name
first_name = input('Enter your first name: ')
# last_name
last_name = input('Enter your last name: ')
# student_number
student_number = input('Enter your student number: ')
# courses information
for i in range(1, 5):
    course_name = input(f'Enter the name of course #{i}: ')
    midterm_test_grade = float(input('Midterm test grade: '))
    final_test_grade = float(input('Final test grade: '))
    # year_end_average = (40% x mid + 60% x final)
    year_end_average = 0.4 * midterm_test_grade + 0.6 * final_test_grade
    # fail_or_pass
    if year_end_average >= 50:
        fail_or_pass = 'Passed'
    else:
        fail_or_pass = 'Failed'

    course_info = {
        "Course": course_name,
        "Midterm Grade": midterm_test_grade,
        "Final Grade": final_test_grade,
        "Year-End Average": year_end_average,
        "Result": fail_or_pass
    }
    courses.append(course_info)

# display for each course
print("\nStudent Information:")
print(f"Name: {first_name} {last_name}")
print(f"Student Number: {student_number}\n")

print("Course info:")
for course_info in courses:
    print(f"Course: {course_info['Course']}")
    print(f"Midterm Grade: {course_info['Midterm Grade']}")
    print(f"Final Grade: {course_info['Final Grade']}")
    print(f"Year-End Average: {course_info['Year-End Average']:.2f}")
    print(f"Result: {course_info['Result']}\n")
# --------------------------------------------------------------