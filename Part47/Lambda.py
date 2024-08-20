students = [("Manisha" ,92),("Abinash" ,96),
            ("Arpita", 80),("Priya",89)]

students.sort()  #sorting alphabatically
print(students)

def sort_students(stu):
    return stu[1]  #sorting by marks

students.sort(key= sort_students, reverse=True)
print(students)

#Lambda function is an anonymous function.
students.sort(key= lambda stu:stu[1])
print(students)