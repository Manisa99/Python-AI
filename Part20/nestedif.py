print("Checking Legal age of marriage in India")

gender = input("Enter Male (m) or Female (f): ")
age = int(input("Enter age: "))

if gender == "m":
    if age >=21:
        print("Eligible for marriage")
    else:
        print("Not eligible for marriage")

elif gender == "f":
    if age >=21:
        print("Eligible for marriage")
    else:
        print("Not eligible for marriage")

else:
    print("Enter valid gender input")
