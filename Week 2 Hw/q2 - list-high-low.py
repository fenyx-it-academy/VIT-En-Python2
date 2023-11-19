# Question 2
numbers = [42, 29, 17, 15, 10, 9, 6, 4, 2, 1]
average = float(sum(numbers) / len(numbers))
print(average)
high_or_low = []
high_count = 0
low_count = 0
for number in numbers:
    if number > average:
        high_or_low.append('High')
        high_count += 1
    else:
        high_or_low.append('Low')
        low_count += 1
print(f'The number of high numbers is: {high_count}')
print(f'The number of low numbers is: {low_count}')
# --------------------------------------------------------------