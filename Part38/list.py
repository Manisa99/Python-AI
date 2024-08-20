#'List' is group of items
# in python 'List' is really flexible
#it can be changed.
names = ["Manisha", "Abinash", "Arpita" , "Mousumi", "A", 1,2,3]
marks = [[80,98,75] , [76,84,62], [75,89,96]]

print(type(names))
print(len(names))
print(names)
print(marks)

final_list = names + marks
print(final_list)

num = list(range(1,25))   #list function
num1 = list(range(5,21,2))
print(num)
print(num1)

text = list("my name is Manisha")
print(text)