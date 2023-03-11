#break & continue
        
maaslar =[1000,8000,3000,9000,5000,2000]

for i in maaslar:
    print(i)

maaslar.sort()
maaslar

for i in maaslar:
    if i == 3000:
        print("kesildi")
        break
    print(i)
 

for i in maaslar:
    if i == 3000:
        print("kesildi")
        continue
    print(i)

#while

sayi = 1

while sayi < 9:
    sayi += 1
    print(sayi)