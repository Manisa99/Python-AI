numbers = [90, 32, 55, 2, 11, 68, 10]

#This will change the original List
numbers.sort()  #ascending order
print(numbers)

numbers.sort(reverse=True)  #descending order
print(numbers)

#This doesnot change the og list
new_list = sorted(numbers)
# new_list = sorted(numbers, reverse=True)
print(new_list)
print(numbers)