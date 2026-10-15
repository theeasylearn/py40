#example of string
name = 'the_easylearn_academy'
city = "bhavnagar "
pincode = """364001"""

print(name,city,pincode)

#1st letter of name
print(name[0]) #t
print(name[1]) #h
print(name[2]) #e
#print 1st 3 letter 
print(name[0:3]) #the
print(name[:3]) #the
#some character from inbetween
print(name[4:13])
#all letter starting from 14th position onwards 
print(name[14:]) 

#reverse string
print(name[::-1])
print(name+city+pincode)
print(city * 5 )

name = 'T.E.A'
print(name)
#ERROR BECAUSE STRING IS IMMUTABLE 
# name[0] = 'THE' #ERROR
print(name)