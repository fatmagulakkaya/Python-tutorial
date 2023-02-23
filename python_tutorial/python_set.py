#PYTHON SET

fruits = {"banana", "grape", "cherry"}
print(fruits)

#Accessing Set Elements
#set elemanlarına index no olmadığından elemanlara döngü ile ulaşabiliri.

fruits = {"banana", "grape", "cherry"}
for fruit in fruits:
    print(fruit)

#set listesinin bir elemanı olup olmadığını kontrol için 'in' operatörü kullanılır.

fruits = {"banana", "grape", "cherry"}
print("banana" in fruits)

#set elemanları güncellenmez. Ancak liste üzerine yeni eleman eklenebilir.

#Adding New Element to Set
#add()--> tek bir eleman ekleme
fruits = {"banana", "grape", "cherry"}
fruits.add("orange")

#update()--> birden fazla eleman ekleme
fruits = {"banana", "grape", "cherry"}
fruits.update(["orange", "mango"])

#Deleting Set Elements

#set'den bir eleman silmek için remove() ya da discard() metodu
fruits = {"banana", "grape", "cherry"}
fruits.remove("grape")

fruits = {"banana", "grape", "cherry"}
fruits.discard("grape")

#clear() metodu ile set elemanlarının hepsini silebiliriz.

fruits = {"banana", "grape", "cherry"}
fruits.clear()

#Combine Multiple Set Lists

#Birden fazla set listesini birleştirmek için kullanabileceğimiz union() ve update() metot
#union() metodu ile birleştirilen set' ler yeni bir set objesiyle geri döner

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#update() metodu ile bir set'i diğer set içerisine eklemiş oluyoruz yeni bir set objesi oluşturulmaz.

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)





















