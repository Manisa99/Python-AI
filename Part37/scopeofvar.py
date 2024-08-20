#global variable - can be accessed anywhere.
var0 = "global var"

def func1():
    #local variable can be accessed only inside that function.
    var1 = "local var"
    print(var1)
    print(var0)

func1()
print(var0)
# print(var1)