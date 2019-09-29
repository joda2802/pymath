def gcd(n,k):
    while(k): 
        n, k = k, n % k 
    return n 


def phi(n):
    p=0
    for i in range(1,n):
        if gcd(n,i)==1:
            p+=1
    return p

n=int(input('input integer:\n'))

print(phi(n))
