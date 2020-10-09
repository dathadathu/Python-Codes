# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 13:10:54 2020

@author: datha
"""

#pip install qrcode

#pip install pillow

import qrcode as q

name  = input("Enter your name:"+"\n")

ECN = input("Emergency contact numbers(2) provide space and type another : "+"\n")

BG = input("Enter you blood group:"+"\n")

Add = input("Enter Address:"+"\n") 

img = q.make(name+"\n"+ECN+"\n"+BG+"\n"+Add)

#print(type(img))

#print(img.size)

img.save('D:/details.png')
