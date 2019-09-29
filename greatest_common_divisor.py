def gcd(n,k):
    
    while(k): 
        n, k = k, n % k 
  
    return n 

n=int(input('insert first integer\n'))
k=int(input('input second integer\n'))

print(gcd(n,k))