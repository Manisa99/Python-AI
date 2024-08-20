var0 = "global variable"
def func1():
    global var0  #to change the of var0 and store a new value
    var0 = "local variable"
    print(var0)

func1()
print(var0)