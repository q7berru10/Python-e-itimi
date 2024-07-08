# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 18:52:17 2024

@author: tusem
"""
#range fonksiyonu aralık demek , 3 aralık alabilir 3. parametre nasıl istiyorsa
#print(*range(10,20,2))#yıldız tetikliyici olarak kullanılır
#print(*range(10,0,-1))
#print(*range(5,-5,-1)) neyenö gdiceğini belirmemiz gerekir
#print(*range(-5,5))
#print(*range(0))



#for döngüsü(iş birden faazla kullanılıcaksa)

#♥çift sayılar için
""" 
for i in range(0,20,2):
    print(i)
    
#tek saylar için
for i in range(1,20,2):
    print(i)
    
sayilar=[1,2,3,4,5]

for i in sayilar:
    print(i)

   
sayilar=[1,2,3,4,5]
meyve=["elma","armut","kiraz"]
for i in meyve:
    print(i)
 
okul=("kalem","silgi","defter")
for i in okul:
    print(i)

harf="abcdef"
for i in harf:
    print(i)


#indexleri ve kendilerini yazdırma
okul=("kalem","silgi","defter")
for a,b in enumerate(okul):
    print(f"{a} : {b}")


#örnek itemslı
ogrenci={"1001":"ahmet","2356":"ayşe","1007":"neslihan"}
for no,ad in  ogrenci.items():
    print(f"öğrenci numarası={no},öğrencinin adı={ad}")

#örnek ögrenci keysli
ogrenci={"1001":"ahmet","2356":"ayşe","1007":"neslihan"}
for no in  ogrenci.keys():
    print(f"öğrenci numarası={no}")
"""








































