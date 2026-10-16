#example of in and not in operator
fruits = ['banana','apple','mango','kiwi','orange','kiwi']
nuts = ('cashew','almonds','nuts')
line = "I am citizen of india."

fav_fruit = 'mango'
fav_nuts = 'nuts'
result = fav_fruit in fruits
result_2 = fav_nuts in nuts 
print("mango found in list ",result)
print("nuts found in tuple ",result_2)

result = fav_fruit not in fruits
result_2 = fav_nuts not in nuts 
print("mango is not found in list ",result)
print("nuts is not found in tuple ",result_2)

country = "india"
result = country in line 
print(f"india is found in {line} ",result)
