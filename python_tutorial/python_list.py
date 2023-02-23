#Python Collections  
#list

message = 'Hello There. My name is Fatma Gül Akkaya'.split()
print(message)   
print(message[5]) 

#list definition
list1 = ['one','two','there']
list2 = ['four','five','six']

numbers = list1 + list2

list1 = [[1,2,3],[4,5,6],[7,8,9],10]

kullaniciA = ['Fatma Gül', 36]
kullaniciB = ['Külter', 2]

kullanicilar = [kullaniciA,kullaniciB]

#Number of Elements in Lists
#len() method

list1 = ['one','two','there']
list2 = [[1,2,3],[4,5,6],[7,8,9],10]

print(len(list1)) 
print(len(list2)) 

#Accessing List Elements
message = ['Hello', 'There.', 'My', 'name', 'is', 'Fatma', 'Gül']

print(message[2])  
print(message[4])   
print(message[-1])  
print(message[-3])  

liste = [[1,2,3],[4,5,6],[7,8,9],10]

print(liste[0])    
print(liste[1][2]) 

names = ['Büşra','Tuğçe','Ceyda']
surnames = ['Yılmaz','Köse','Önal']

result = names[0] +' '+ surnames[0]  
result = names[1] +' '+ surnames[1]

names = ['büşra','tuğçe','ceyda']
for name in names:
   print(name)

#List Shredding
message = ['Hello', 'There.', 'My', 'name', 'is', 'Fatma Gül', 'Akkaya']
print(message[0:2])

message = ['Hello', 'There.', 'My', 'name', 'is', 'Fatma Gül', 'Akkaya']
print(message[:2])

#list updated
list1 = ['Rose','Jasmine','Lilac']
list1[1] = 'Carnation '
print(list1)

#Adding Elements to the List-listeye eleman ekleme
#append() listenin sonuna ekleme
liste = ['cherry','banana','grape']
liste.append('Strawberry')
print(liste)

#insert() indekse eleman ekleme
liste = ["cherry","banana","grape"]
liste.insert( 2,"strawbery")
print(liste)

#remove() eleman silme
liste = ['cherry','banana','grape']
liste.remove('strawbery')
print(liste)

#pop() indeks'deki elemanı silme
liste = ['cherry','banana','grape']
liste.pop(1)
print(liste)

#indeks numarası verilmediğinde son eleman silinir.
liste = ['cherry','banana','grape']
liste.pop()
print(liste)

#del ()

liste = ['cherry','banana','grape']
del liste[2]
print(liste)

#min and max method
numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a', 'g', 's', 'b', 'y', 'a', 's']
min(numbers) 
max(numbers) 
max(letters) 
min(letters)

#count() method
numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a', 'g', 's', 'b', 'y', 'a', 's']
numbers.count(10)  
letters.count('a')






























