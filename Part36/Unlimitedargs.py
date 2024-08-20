#By using * we can pass unlimited args.
def add(*num):
    print(num)

add(2, 3, 4, 10, 32)

#addition in 'for' loop.
def add1(*num):
    result = 0
    for n in num:
        result = result + n
    print(result)

add1(2, 3, 4, 10, 32)