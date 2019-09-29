from sympy import *

def integral(f):
    return integrate(eval(f),x)

x=Symbol('x')
f=input('input function in x:\n')
print(integral(f))