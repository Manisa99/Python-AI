# *
# * *
# * * *
# * * * *
# * * * * *

#for loop
for x in range(1 ,6):
    for y in range(1 , x+1):
        print("* " , end="")
    print("")
print("Loop ends here")

#while loop
line = 1
while line <= 5:
    star = 1
    while star <= line:
        print("* ", end="")
        star += 1
    print("")
    line += 1 
