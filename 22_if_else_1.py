# write a program to convert 24 hours format time into 12 hours format time and display it.
# input hours 

hours = int(input("Enter hours "))
if hours>12:
    hours = hours - 12
    print(f"{hours} PM")
else:
    print(f"{hours} AM")

print("Good bye")
