# Question 3
while True:
    lower_end = int(input('Enter the lower end of the range: '))
    higher_end = int(input('Enter the higher end of the range: '))
    if lower_end >= higher_end:
        print('Error! Lower end must be smaller than higher end.Try Again: ')
    else:
        my_range = range(lower_end, higher_end + 1)
        sum_odd = sum(0 if i % 2 == 0 else i for i in my_range)
        print(f'The sum of odd numbers in your range is: {sum_odd}')
        break
# --------------------------------------------------------------