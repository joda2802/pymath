from scipy.misc import derivative

def derivate(g):
    return derivative(f,x,dx=1e-6)

def f(x):
    return eval(func)

func = input('input function in x\n')
x = float(input('input the x-value\n'))

print(derivate(f))