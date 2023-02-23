#Python Tuple

#tuple = ("banana", "grape", "cherry")
#print(tuple)


#updating tuple list elements

a=("banana","grape","cherry")
b= list(a)
b[1] = "apple"
a= tuple(b)
print (a)

#Accessing Tuple Elements

message = ('Hello', 'There.', 'My', 'name', 'is', 'Fatma', 'Gül')

print(message[2])   
print(message[4])   
print(message[-1])  
print(message[-3])  


# 0 ve 2. indeks arası elemanlar
message = ('Hello', 'There.', 'My', 'name', 'is', 'Fatma', 'Gül')
print(message[0:2])

#baştan 2. indekse kadar
message = ('Hello', 'There.', 'My', 'name', 'is', 'Fatma', 'Gül')
print(message[:2])

#Loop Access to Tuple Elements

names = ('Toprak','su','ates')
for name in names:
   print(name)


#Tuple Methods
#count()--> tekrarlayan eleman sayısı

numbers = (1, 10, 5, 16, 4, 9, 10)
letters = ('a', 'g', 's', 'b', 'y', 'a', 's')
numbers.count(10)  
letters.count('a')

#index()-->bir elemanın index numarasını almak

numbers = (1, 10, 5, 16, 4, 9, 10)
numbers.index(10)





















