#Unpacking the items in the 'List' .
names = ["Abinash" , "Manisha" , "Subham" , 1, 2, 3, "Mousumi"]
first, second, third, *others, fourth = names

print(first)
print(second)
print(third)
print(fourth)
print(others)