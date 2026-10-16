# write a program to findout profit or loss amount from given product's purchase and sales price 
#input : purchase price & sales price

purchase_price = int(input("Enter purchase price "))
sales_price = int(input("Enter sales price "))

difference = sales_price - purchase_price

if difference>0:
    print("you have made profit of ",difference)

if difference<0:
    print("you have made loss of ",difference)

if difference==0:
    print("you have made no loss no profit")

print("Good bye")

