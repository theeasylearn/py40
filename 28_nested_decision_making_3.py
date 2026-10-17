# write a program to findout eldest person from 3 person's give age by user 
age1 = int(input("Enter 1st person age"))
age2 = int(input("Enter 2nd person age"))
age3 = int(input("Enter 3rd person age"))

if age1>age2:
    if age1>age3:
        print("1st person is eldest person ")
    else:
        print("3rd person is eldest person")
else:
    if age2>age3:
        print("2nd person is eldest person")
    else:
        print("3rd person is eldest person")

print("Good bye")