from cmath import cosh, e
import matplotlib.pyplot as plt
import numpy as np
import random
import math
print ("1-Infinitely long fin")
print ("2-Insulated fin tip")
print ("3-Convective heat loss from tip")
print ("4-Prescribed temperature at tip")
num = int(input("Enter a number:"))
x=np.linspace(0,0.03,1000)
k=370
h=10
m=2.32495278
L=0.03
p=0.008
a=0.00004
THb=45
if(num==3):
    def f(x): 
        return THb*((((k*m)-h)*(e**(m*(x-L))))+(((k*m)+h)*e**(m*(L-x))))/((h*(e**(m*L)-e**(-m*L)))+(k*m*(e**(m*L)+e**(-m*L))))
    plt.plot(x,f(x))
    print(f(0))
    print(f(0.03))
    plt.show()
if(num==1):
    x=np.linspace(0,1,1000)
    def f(x): 
        return THb*(e**(-m*x))
    plt.plot(x,f(x))
    print(f(0))
    print(f(100000000000000000000))
    plt.show()
if(num==2):
    def f(x): 
        return THb*(((e**(m*(L-x)))+(e**(-m*(L-x))))/((e**(m*(L)))+(e**(-m*(L)))))

    plt.plot(x,f(x))
    print(f(0))
    print(f(0.03))
    plt.show()
if(num==4):
    n=random.randint((26+273),(69+273))-298
    print (n)
    x=np.linspace(0,0.03,1000)
    def f(x): 
        return THb*((((n/THb)*((e**(m*x))-(e**(-m*x))))+(e**(m*(L-x)))-(e**(-m*(L-x))))/((e**(m*(L)))-(e**(-m*(L)))))
    plt.plot(x,f(x))
    print(f(0))
    print(f(0.03))
    plt.show()