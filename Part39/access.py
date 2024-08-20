#Accessing elements of 'List'.
names = ["Manisha", "Abinash", "Arpita" , "Mousumi", "A", 1,2,3]

marks = ["india", [80,98,75] , [76,84,62], [75,89,96], "true", 50]

print(names[4])  #position of the items in the 'List'

print(marks[5])

print(marks[-4])

print(marks[1][2])  #accessing nested list

print(names[-3])

names[2] = "4" #changing the item
print(names) 

marks[2][0] = 35
print(marks)
