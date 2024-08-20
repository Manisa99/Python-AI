#logical AND : checks both the statements
#logical OR : checks any one statement
#logical NOT: reverse the boolean value

HSC = 66
CHSE = 70
criminal = False

if HSC >= 60 and CHSE >=60:
    if not criminal:
        print("Eligible for Addmission")
    else:
        print("Not Eligible")

if HSC >= 60 or CHSE >=80:
    print("Eligible for Addmission")
else:
    print("Not Eligible")

