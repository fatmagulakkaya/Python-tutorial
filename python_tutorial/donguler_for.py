#DONGULER - for

ogrenci = ["Fatma","Gül","Külter","Zeynep","Adem"]

ogrenci[0]
ogrenci[1]
ogrenci[2]
ogrenci[3]
ogrenci[4]

for i in ogrenci:
    print("Ogrenci Adi: " +i)

#for

maaslar = [1000,2000,3000,4000,5000]

maaslar[0]
maaslar[1]
maaslar[2]
maaslar[3]
maaslar[4]

for maas in maaslar:
    print("Maaslar : " +str(maas))

#dongu ve fonksiyonları birlikte kullanmak

def kare_al(x):
    print(x**2)    
    
kare_al(2)    

maaslar = [1000,2000,3000,4000,5000]

for i in maaslar:
    print(i)
    
#maaslara %20 zam yapilacak gerekli kodlari yaziniz.

1000*20/100  + 1000   

maaslar[0]*20/100 + maaslar[0]
maaslar[1]*20/100 + maaslar[1]
maaslar[2]*20/100 + maaslar[2]    

#donguyu fonksiyon ile yazma.    
def yeni_maas(x):
    print(x)

yeni_maas(4)

def yeni_maas(x):
    print(x*20/100 + x)
    
yeni_maas(1000)
yeni_maas(2000)
yeni_maas(3000)


for i in maaslar:
    yeni_maas(i)
