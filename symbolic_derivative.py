from sympy import *

def derivative(f,n):
    return diff(eval(f),x,n)

x=Symbol('x')
f=input('input function in x:\n')
n=input('input number of derivations:\n')

print(derivative(f,n))