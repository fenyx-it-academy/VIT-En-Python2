# Third program
# Sum of odd numbers between twee numbers
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

first_num = input("Please enter first integer number: ")
second_num = input("Please enter second integer number: ")

lenx1 = len(first_num)
x = 0
isvalid1 = False

while x <= (lenx1 - 1):
    if first_num[x] in numbers:
        isvalid1 = True
        x += 1
    else:
        print('The first number is not valid!')
        isvalid1 = False
        break

lenx2 = len(second_num)
x = 0
isvalid2 = False

while x <= (lenx2 - 1):
    if second_num[x] in numbers:
        isvalid2 = True
        x += 1
    else:
        print('The second number is not valid!')
        isvalid2 = False
        break

if isvalid1 and isvalid2:
    num01 = int(first_num)
    num02 = int(second_num)
    oddnumbers = 0
    sumofodd = 0
    while not(num01 == num02):
        num01 += 1
        if ((num01 % 2) != 0) and (num01 != num02):
            sumofodd += num01
            oddnumbers += 1

    print("The number of ODD numbers between ", first_num,' and ', second_num, ' is ', oddnumbers)
    print("The sum of ODD numbers between ", first_num,' and ', second_num, ' is ', sumofodd)






