# This is second question
# This program compute the average of a list

numbers = [42, 29, 17, 15, 10, 9, 6, 4, 2, 1]

counter = 0
sum = 0.0

for x in numbers :
    sum += x
    counter +=1

average = sum / counter

highcount = 0
lowcount = 0

for x in numbers :
    if x > average :
        highcount += 1
    elif x < average :
        lowcount +=1

print("The count if High_Numbers: ", highcount)
print("The count if Low_Numbers: ", lowcount)

#End of program