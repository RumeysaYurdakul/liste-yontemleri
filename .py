#liste uygulamaları
#8.12.2020

import math
toplam=0   #toplamın ilk değeri
sayi=[] #boş liste

for i in range(10):
     print(i+1,". sayıyı giriniz:",end="")
     x=eval(input())
     sayi.append(x)
     toplam=toplam+x

print("girdiğiniz sayıların toplamı",toplam)
ortalama=toplam/10
print("girdiğiniz sayıların ortalaması", ortalama)

print(sayi)

farklar=[]
for i in range(10):
     farklar.append(abs(ortalama-sayi[i]))
#bunun yerine aşağıdaki şekildede olur
#f=ortalama-sayi[i]
#md=abs(f)
#farklar.append(md)
print(farklar)

#farklar listesinin en küçük elamanını bulma
en_kucuk=farklar[0] #listenin ilk elemanı
                    #başlangıçta en küçük olarak kabul et
indis=0
for i in range(1,10): #listenin geri kalanını kontrol et
     if farklar[i]<en_kucuk:
          en_kucuk=farklar[i]
          indis=i
          
print("en küçük fark:",en_kucuk)
print("ortalamaya en yakın sayı:",sayi[indis])

