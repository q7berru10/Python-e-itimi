# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 19:45:50 2024

@author: tusem
"""
#bir liste tanımlayıp toplayalım
"""
sayilar =[1,2,3,4,5]
toplam=0

for i in sayilar:
    toplam=toplam+i     #toplam+=i ilede yazılabilir#
    #print("toplam=",toplam) yaparsak tek tek toplar her seferinde her bir tur gösterilir ekranda
print("toplam=",toplam)

#listeyi 2ye bölme
sayilar=[1,2,3,4,5,6,7,8,9,10]
for i in sayilar:
  if(i%2==0):
    print(i)
   
#listeyi tek sayılara bölme 
sayilar=[1,2,3,4,5,6,7,8,9,10]
for i in sayilar:
  if(i%2==1):
    print(i)

sayilar=[1,2,3,4,5,6,7,8,9,10]
#sayilar=[]
if len (sayilar)>0:
    for i in sayilar:
        print(i)
else:
    print("eleman yok")

#3ün katları 20ye kadar
sayilar=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in sayilar:
  if(i%3==0):
    print(i)

#örenek kullanıcıdan sayı alıp bastırmak
a=int(input("Başlanıç sayısını giriniz: "))
b=int(input("Bitiş Noktasını giriniz: "))
for i in  range(a+1,b):
  print(i)

#iç içe for
sayilar=[1,2,3,4]
for sayi in sayilar:
  print(f"1.döngü çalıştı sayi={sayi}")
for sayi in sayilar:
  print(f"2.döngü çalıştı sayi={sayi}")

 #her elamanın toplamı
sayilar=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
toplam=0
for i in sayilar:
    toplam=toplam+i 
    print("toplam:",toplam)
print("toplam=",toplam)

#listedeki tek sayıların karesi
sayilar=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
karesi=1
for i in sayilar:
    print("{} sayısının karesi={}".format(i, i**2))


a=int(input("ilk sayıyı giriniz: "))
b=int(input("Bitiş sayısını giriniz: "))
if a>b:
    for i in range(b,a):
        print(i)
else:
    for i in range(a,b):
        print(i)
  
 #calışıyor ama gereksiz uzun
a=int(input("ilk sayının toplamı: "))
b=int(input("Bitiş sayının giriniz: "))
toplam=a+b
for i in range(a,b):
    toplam=toplam+i 
    print("toplam:",toplam)
print("toplam=",toplam)

 #yada
a=int(input("ilk sayıyı giriniz: "))
b=int(input("Bitiş sayısını giriniz: "))
toplam=a+b
if a>b:
    for i in range(b,a):
        toplam=toplam+i
        print("toplam=",toplam)
        print(i)
else:
    for i in range(a,b):
        toplam=toplam+i
print("toplam=",toplam)

#faktoriyel 5!=5.4.3.2.1 gibi
toplam=1
deger=int(input("birinci sayıyı giriniz:"))
for i in range(deger+1):
    if i>0:
        toplam*=i
print("toplam:",toplam)

#daha kısa yolu

toplam=1
deger=int(input("birinci sayıyı giriniz:"))
for i in range(1,deger+1):
    toplam*=i
print("toplam:",toplam)



toplam=1
deger=int(input("birinci sayıyı giriniz:"))
for i in range(deger,0,-1):
    toplam*=i
print("toplam:",toplam)
 
"""





























