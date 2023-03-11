#mini uygulama2
#if, for ve fonksiyonlari birlikte kullanmak  
#maasi 3000 den yüksek olanlara %10, düşük olanlara %20 zam yapılacaktır. 

maaslar = [1000,2000,3000,4000,5000]
def maas_yuksek(x):
        print(x*10/100 + x)
def maas_dusuk(x):
        print(x*20/100 + x)
for i in maaslar:
    if i>=3000:
        maas_yuksek(i)
    else:
        maas_dusuk(i)