from sympy import *

x=Symbol('x')

def lim(f,a):
    return limit(f,x,a)


f=input('input function in x:\n')
a=input('input x-value (oo for infinity):\n')

print(lim(f,a))