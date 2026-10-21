#example of for loop on tuple
tuple = (10,20,50,100,200,500)
for item in tuple:
    #print(item,end=' ')
    square = item * item 
    print(square,end=' ')

print("") #new line
print("now let us process tuple in reverse order ")
for item in reversed(tuple):
    #print(item,end=' ')
    square = item * item 
    print(square,end=' ')