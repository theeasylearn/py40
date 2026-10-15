#dictionary related methods
person = {'name':"Vishnu",'age':19,'weight':50.99,'gender':True}
print(person)
print("get only keys ",person.keys())
print("get only values ",person.values())
print("get key & values ",person.items())

person.pop("gender")
person.popitem()
print("after removal ",person)

#key value pair update
person.update({'age':21,'email':'vishnu@gmail.com'})
print("after update ",person)

match = ['teamA','teamB','venue','date','time']
print(match)

#create dictionary using list value as key 
match_1 = dict.fromkeys(match)
match_2 = dict.fromkeys(match)
print(match_1,match_2)

person_2 = person.copy()
print(person,person_2)

person.clear()
print(person,person_2)

