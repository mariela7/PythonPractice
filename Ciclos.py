# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 21:05:04 2021

@author: Mariela
"""

#similar al for each de otros lenguajes
palabra="patatas"
for letra in palabra:
    print(letra)
print('siguiente instrucción')



a="patatas"
for i in range(0,len(a)):
    print(a[i])
print('siguiente instrucción')


palabra="patatas"
for letra in palabra:
    print (letra)
    if letra == 't':
      break
print('siguiente instrucción')



a="patatas"
for letra in a:
    if letra=='a':
        continue    
    print (letra)
print('siguiente instrucción')