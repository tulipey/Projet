# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 03:31:26 2022

@author: uplay
"""

import matplotlib.pyplot as plt

liste1=[]
nom=[]
score=[]

f= open (r"C:\Users\uplay\Desktop\data.csv")
for colone in f:
    liste1=colone.split(',')
    score.append(liste1[4])
f.close()
print(score)

del score[0]
print(score)

f= open (r"C:\Users\uplay\Desktop\data.csv")
for colone in f:
    liste1=colone.split(',')
    nom.append(liste1[3])
f.close()
print(nom)

plt.pie(score, labels = [nom[1], nom[2], nom[3], nom[4]], normalize = True)
plt.figure(figsize = (8, 8))
plt.pie(score, labels = [nom[1], nom[2], nom[3], nom[4]], normalize = True)
plt.legend()