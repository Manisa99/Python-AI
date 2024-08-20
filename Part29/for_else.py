for number in range(3):
    num = int(input("Enter odd number: "))

    if num % 2 == 0:
        print("You loose!")
        break

else:
    print("You won!")