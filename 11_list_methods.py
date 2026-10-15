#list methods
fruits = ['banana','apple','mango','kiwi','orange','kiwi']
nuts = ['cashew','almonds','nuts']
print(fruits)

#add new item at the end of list
fruits.append('watermelon')
fruits.append('coconut')
#add at the beginning 
fruits.insert(0,"pineapple")
print("after inserting new items", fruits)

#extends list (concatenation )

fruits.extend(nuts)
print("After extending list ",fruits)

#remove item  using value
fruits.remove("watermelon")

#remove item using position
fruits.pop(0)
print("after removal fruit has ", fruits)

#make list empty 
nuts.clear()
print(nuts)

print("position of apple ",fruits.index("apple"))
# print("position of cherry ",fruits.index("cherry")) #return ValueError as value not found

#find count of items
print("count of kiwi ",fruits.count("kiwi"))
print("count of cherry ",fruits.count("cherry"))

fruits.sort()
print("Sorted fruits ",fruits)

fruits.reverse()
print("reversed fruits ",fruits)

#we must copy method to copy list into another list 
fruits_2 = fruits.copy()
print(fruits,fruits_2)

