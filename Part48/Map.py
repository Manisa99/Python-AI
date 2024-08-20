students = [("Manisha" ,92),("Abinash" ,96),
            ("Arpita", 80),("Priya",89)]

#Creating a new list from the existing list.
names = []
for x in students:
    names.append(x[0])
print(names)

#using map function
new_list = list(map(lambda x:x[0], students))
print(new_list)  