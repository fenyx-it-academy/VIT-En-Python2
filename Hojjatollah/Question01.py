# This is the first Question

# This program get information of one student and compute situation

fname = input("Please enter your first name: ")
lname = input("Please enter your first name: ")

course01_name = input("Please enter the name of first course: ")
course01_midnum = float(input("Please enter the middel term grade of first course: "))
course01_lastnum =  float(input("Please enter the final grade of first course: "))

course02_name = input("Please enter the name of second course: ")
course02_midnum = float(input("Please enter the middel term grade of second course: "))
course02_lastnum =  float(input("Please enter the final grade of second course: "))

course03_name = input("Please enter the name of third course: ")
course03_midnum = float(input("Please enter the middel term grade of third course: "))
course03_lastnum =  float(input("Please enter the final grade of third course: "))

course04_name = input("Please enter the name of forth course: ")
course04_midnum = float(input("Please enter the middel term grade of forth course: "))
course04_lastnum =  float(input("Please enter the final grade of forth course: "))

course01_result = (course01_lastnum * 0.60) + (course01_midnum * 0.40)
course02_result = (course02_lastnum * 0.60) + (course02_midnum * 0.40)
course03_result = (course03_lastnum * 0.60) + (course03_midnum * 0.40)
course04_result = (course04_lastnum * 0.60) + (course04_midnum * 0.40)

if course01_result >= 50 :
    print("The average of the ", course01_name, " is ", course01_result)
    print("***You are PASSED***")
else:
    print("The average of the ", course01_name, " is ", course01_result)
    print("!!!You are FAILED!!!")

if course02_result >= 50 :
    print("The average of the ", course02_name, " is ", course02_result)
    print("***You are PASSED***")
else:
    print("The average of the ", course02_name, " is ", course02_result)
    print("!!!You are FAILED!!!")

if course03_result >= 50 :
    print("The average of the ", course03_name, " is ", course03_result)
    print("***You are PASSED***")
else:
    print("The average of the ", course03_name, " is ", course03_result)
    print("!!!You are FAILED!!!")

if course04_result >= 50 :
    print("The average of the ", course04_name, " is ", course04_result)
    print("***You are PASSED***")
else:
    print("The average of the ", course04_name, " is ", course04_result)
    print("!!!You are FAILED!!!")

# End of the program
