students = [("Manisha" ,92),("Abinash" ,96),
            ("Arpita", 80),("Priya",89)]

new_list = []
for x in students:
    if x[1] > 90:
        new_list.append(x)

print(new_list)

#Using 'filter' function
new_list = filter(lambda x: x[1] > 90, students)
new_list = list(new_list)
print(new_list)                  
