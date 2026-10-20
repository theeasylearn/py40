# write a program to findout sum of all digits in given number 
# 12345 process : 1 + 2 + 3 + 4 + 5 =15
# 456 process : 4 + 5 + 6 = 15
num = int(input("Enter number"))
sum = 0 

while num>0:
    reminder = num % 10 # 4
    sum = sum + reminder
    num = num // 10 #123

print(sum)