# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 19:34:48 2024

@author: tusem
"""

isim= input("isminiz:")
yas=int(input("yaşınız:"))
egtim=input("eğtim seviyesi:")
egtim_seviyeleri=["lise","ilkokul","üniversite","ortaöğretim","yüksek lisana","doktra"]

if (yas>=18):
 #   egtim=input("eğtimseviyesi")
    if egtim in egtim_seviyeleri:
        print("{} ehliyet alabilirsin".format(isim))
    else:
        print("{} ehliyet alamazsın".format(isim))
else:
   print("{} ehliyet alaazsın,yaşın tutömıypr".format(isim))     


