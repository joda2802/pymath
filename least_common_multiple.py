def gcd(n,k):
    
    while(k): 
        n, k = k, n % k 
  
    return n 

def lcm(n,k):
    return int(n*k/gcd(n,k))

n=int(input('insert first integer\n'))
k=int(input('input second integer\n'))

print(lcm(n,k))