# write a program to print how many days month has from given month no 
# input month
# 1 3 5 7 8 10 12 then month 31 days
# 4 6 9 11 then month has 30 day 
# 2 then month has 28/29 day 
month = int(input("Enter month no (1 to 12)"))
if month==2:
    print("this month has 28/29 days")
    exit(1) #it will stop your program 
    
if month==4 or month==6 or month==9 or month==11:
    print("this month has 30 days")
else:
    print("this month has 31 days")