#example of for loop on list 
# create two list, one list should have odd values and other list should have even values
list = [10,11,13,20,25,50,101,200,251,399]
odd = []
even = []

for num in list: 
    # print(num,end=' ') 
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)

print("Even list",even)
print("ODD list",odd)