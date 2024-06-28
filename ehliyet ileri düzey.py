# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 18:55:21 2024

@author: tusem
"""

#♠28.06 cuma günü
#in işleci içindemi diye soruyor 

ad=input("adınız")
yas=int(input("yaşınız"))
egtim_seviyesi=["ilköğretim","ortaöğretim","lise","niversite"]

if yas<18:
    print("üzgünüz malesef yaşınız ehliyet almaya uygun değildir")
else:
    eğtim=input("eğtim seviyeniz(ilköğretim,ortaöğretim,lise,üniversite):")
    if eğtim in egtim_seviyesi:
        print("tebrikler ehliyet alabilirsiniz")
    else:
        print("üzgünüm eğtim seviyeniz ehliyet için yeterli değil")