#list example
box = ['car',69,100,3.14,True]
print(box)

#print 1st value
print(box[0]) #car
print(box[1]) #69
print(box[0:2]) #Car 69
print(box[3:]) #3.14 True

#change value 
box[0] = 'Plane'
box[1] = 'Ankit'
box[2] = True
print(box)

#delete 3rd value 
del box[3]
print(box)

print(box * 5)
fruits = ['apple','banana','mango']
print(box + fruits)
