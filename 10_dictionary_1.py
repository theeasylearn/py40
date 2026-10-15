#example of dictionary

person = {'name':"Vishnu",'age':19,'weight':50.99,'gender':True}
print(person)

#print name
print(person['name']) 
print(person['age'])
print(person['weight'])

#update key value
person['weight'] = 55.11
print(person['weight'])

#add new key value pair
person['email'] = 'vishnu@gmail.com'
print(person)
