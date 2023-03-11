#Python Fonksiyonlar


def kare_al(x):
    print("Girilen Sayi:" + str(x) +
          ", Karesi:" 
          + str(x**2))
kare_al(3)    

#iki Argümalı fonksiyon tanımlamak
def carpma_yap(x,y):
    print(x*y)
    
carpma_yap(3, 6)
 

#Örnek: sokak lambası   
#isi, nem, sarj
(40+25)/90

def direk_hesap(isi,nem,sarj):
    print((isi+nem)/sarj)
direk_hesap(25,40,70)

#Çıktıyı Gİrdi Olarak Kullanmak

def direk_hesap(isi,nem,sarj):
    return (isi+nem)/sarj

cikti = direk_hesap(25,40,70)
cikti
print(cikti)

#Local ve Global Değişkenler

x=10
y=20

def carpma_yap(x,y):  #buradaki x ve y değişkenleri local değişkenlerdir
    return x*y

carpma_yap(2, 3)

#local etki alanından Global etki alanını değiştirmek

x=[]
def eleman_ekle(y):
    x.append(y)
    print(str(y) + " ifadesi eklendi")

eleman_ekle("Gül") 
eleman_ekle("Lale")
eleman_ekle("Yasemin")

x

#☺KARAR & KONTROL YAPILARI

#True-False sorgulamaları

sinir = 5000

sinir == 4000
sinir==5000

#İF

sinir = 50000
gelir=40000

gelir < sinir 

if gelir < sinir:
    print("Gelir sinirdan kucuk")
    print(gelir*2)
    
if gelir > sinir:
    print("Gelir sinirdan kucuk")  

#ELSE
sinir = 50000
gelir = 45000
if gelir > sinir:
    print("Gelir sinirdan buyuk")  
else:
    print("Gelir sinirdan kucuk")

#ELİF

sinir = 50000
gelir1 = 60000
gelir2 = 50000
gelir3 = 35000

if gelir1 > sinir:
    print("Tebrikler, hediye kazandınız.")
elif gelir1 < sinir:
    print("Uyari !")
else:
    print("Takibe devam.")

if gelir2 > sinir:
    print("Tebrikler, hediye kazandınız.")
elif gelir2 < sinir:
    print("Uyari !")
else:
    print("Takibe devam.")


if gelir3 > sinir:
    print("Tebrikler, hediye kazandınız.")
elif gelir3 < sinir:
    print("Uyari !")
else:
    print("Takibe devam.")






    




