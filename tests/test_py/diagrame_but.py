# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 05:14:30 2022

@author: uplay
"""
import matplotlib.pyplot as plt

liste1=[]
nom=[]
but=[]

f= open (r"C:\Users\uplay\Desktop\data.csv")
for colone in f:
    liste1=colone.split(',')
    but.append(liste1[5])
f.close()
print(but)

del but[0]
print(but)

f= open (r"C:\Users\uplay\Desktop\data.csv")
for colone in f:
    liste1=colone.split(',')
    nom.append(liste1[3])
f.close()
print(nom) 

b = [int(but[0])]

o = [int(but[2])]

o1= [int(but[3])]

b1= [int(but[1])]

import pandas as pd

mydata = pd.DataFrame({nom[1]:b,nom[2]:b1,nom[3]:o,nom[4]:o1})

mydata.index = [" "]

mydata.plot(kind="bar",rot=30) 

plt.show()

plt.savefig('/Users/uplay/Desktop/projet/tests/test_web/diag_but.png')