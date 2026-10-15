#example of set 
fruits = {'apple','mango','orange','pineapple','apple'} 
print(fruits)

fruits.add('kiwi')
fruits.add('watermelon')
fruits.add('kiwi')
print(fruits)

vegis = ['potato','tomato','onion','potato'] 
print(vegis)

#remove duplicate from list 
set1 = set(vegis)
print(set1)

a = {1,2,3,4,5}
b = {4,5,6,7,8}
print(a,b)
print(a,b)

union = a.union(b)
print(union)

intersection = a.intersection(b)
print(intersection)

difference = a.difference(b)
print(difference)

