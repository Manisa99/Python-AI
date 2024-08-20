listofnames = ["Abinash" , "Manisha" , "Vishal" , "Megha"]

listofnames.append("Youtube")
print(listofnames)

listofnames.insert(2, "Twitter")
print(listofnames)

listofnames.pop()
print(listofnames)

listofnames.pop(3)     #removing item by index
print(listofnames)  

del listofnames[1:3]  #another way to delete items from list
print(listofnames)

listofnames.remove("Abinash")  #removing item by name
print(listofnames)

listofnames.clear()  #To empty a list use 'Clear' function.
print(listofnames)  