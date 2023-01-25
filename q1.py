
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24] #given list
# sorting
ages.sort()
print("ages after sorting", ages)
min_age = ages[0] 
max_age = ages[-1]
print("min age = ", min_age)
print("max age = ", max_age)
ages.append(min_age) # adding min and max to list again
ages.append(max_age)
print("ages after adding min and max again", ages)
ages.sort()# we have to sort list again (because we added new elements)
n = len(ages)
if (n%2 == 0): #if even length
    median = (ages[n//2] + ages[(n//2) - 1])/2# finding median
else: #if odd length
    median = ages[n//2]
print("median = ", median)
# finding average
sum = 0
for i in ages:
    sum += i # adding all elements
average = sum/n # sum/no.of elements
print("average = ", average)
# finding range
age_range = max_age - min_age
print("range = ", age_range)
