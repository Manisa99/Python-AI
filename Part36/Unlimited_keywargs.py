#To pass unlimited keyword Args we should use '**'

def add_student(**args):
    for x,y in args.items():
    #   print(x)
    #   print(args[x])
      print(f"{x} = {y}")

add_student(name = "Vishal" , Roll=1 , Age=25)
