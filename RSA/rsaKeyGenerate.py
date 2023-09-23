from Crypto.Util.number import *
from random import choice
import gmpy2

def Prime(bits):
    while True:
        n=2
        while n.bit_length()<bits:
            n*=choice(sieve_base)
        if gmpy2.is_prime(n-1):
            return n-1
        
#get a Prime with specified bits

def gcd(A,B):
    if A<B:
        C = A
        A = B
        B = C
    r = A % B
    while(r != 0):
        A = B
        B = r
        r = A%B
    return B

#use Euclid algorithm to check if A B are ralative prime

def xgcd(a, b):
    if a == 0:
        return 0, 1, b
    if b == 0:
        return 1, 0, a

    px, ppx = 0, 1
    py, ppy = 1, 0

    while b:
        q = a // b
        a, b = b, a % b
        x = ppx - q * px
        y = ppy - q * py
        ppx, px = px, x
        ppy, py = py, y

    return ppx, ppy, a

#use exgcd to find d(the inverse of e)

p = Prime(700)
q = Prime(700)

N = p*q

r = (p-1)*(q-1)

e = 0x10001

#encode number should be relatively prime to r

while (gcd(e,r) != 1):
    e-=1

#(N, e) is the public key

publicKey = [N,e]
e_inverse, _, _ = xgcd(e, r)
d = e_inverse % r
#generating decode number

print(N, e, '\n')


print(N, d, '\n')