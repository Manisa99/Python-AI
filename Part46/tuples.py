#Tuple is also group of items but can not be changed/modified.
#it's immutable.
student =  "Adil" , 4 , "Megha" , "Anu"
print(student)
print(type(student))

t1 = (1,5,4)
t2 = (2,0)
t3 = t1 + t2  #concatenation
print(t3)

list = [1, 2, 3, 4]
t1 = tuple(list)
print(t1)

tuple_list = (20, 1, 5, 12)
a = tuple_list[2]
print(a * 2)  #you can perform any operation after assigning to a variable.

tuple1 = (1,4,6)
x,y,z = tuple1
print(y)

if 3 in tuple1:
    print("Yes")
else:
    print("No") 