# Вычислить число ПИ c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from time import time
from random import random
from math import sqrt
 
dates=100000
t1=time()
hists=0
for i in range(1,dates):
     x,y=random(),random()
     dist=sqrt(x**2+y**2)
     if dist<=1:
        hists+=1     
pi=4*(hists/dates)
print('Для заданной точности:', round((time()-t1),3))
print(f'Число Пи равно : {pi}')