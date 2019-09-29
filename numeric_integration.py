from scipy.integrate import quad

def f(x):
    return eval(func)

def integral(f,a,b):
    i,err=quad(f,a,b)
    return i

func = input('input function in x\n')
a = float(input('input left bound\n'))
b = float(input('input right bound\n'))

print(integral(f,a,b))