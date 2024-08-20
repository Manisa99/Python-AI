student = {
    "name": "Manisha", 
    "reg no": 220482308,
    "course": "MCA"
}

for x in student:
    print(x, student[x]) 

#Print data in 'tuple' using 'items'() function
for x in student.items():
    print(x) 

for key,value in student.items():
    print(key, value)