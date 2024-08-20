students = [ ("Manisha" ,92),
            ("Abinash" ,96),
            ("Arpita", 80),
            ("Priya",89) 
            ]
#map function
new_list = [x[1] for x in students]

print(new_list)

#filter function
list1 = [ x for x in students if x[1] > 90]

print(list1)