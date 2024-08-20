student = {
    "name": "Manisha", 
    "reg no": 220482308,
    "course": "MCA"
}
print(student)

#How to access dictionary
student["name"] = "Abinash"
student["contact no"] = 7978448395
print(student)

# print(student["hbuki"])

#checking
if "name" in student:
    print(student["name"])

#Checking using 'get' function
print(student.get("mobile"))
print(student.get("mobile" ,210010))

del student["reg no"]
print(student)