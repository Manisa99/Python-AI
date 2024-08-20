#using break in 'for' loop

for x in range(10):
    if x == 5:
        break
    print(x)
print("Loop ended")

#using break in 'while'loop
x = 1
while x <= 10:
    if x == 6:
        break
    print(x)
    x += 1