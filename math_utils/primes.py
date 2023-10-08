from math import sqrt, isqrt

def isprime(n):
    """Uses a simple algorithm to determine whether or not n is prime"""

    if n==1:
        return False
    
    root_n = isqrt(n)

    for i in range(2,root_n+1):
        if n % i == 0:
            return False
        
    return True

print(isprime(2))