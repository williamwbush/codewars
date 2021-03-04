# i = 8
# print (i & (i & -i) << 1)
# print (i & ((i & -i) << 1))
# print ((i & (i & -i)) << 1)

from math import sqrt
primes = []
for i in range (2, 101):
    factors = []
    for n in range(1, i + 1):
        if i % n == 0:
            factors.append(n)
    if len(factors) <= 2:
        primes.append(i)
print(primes)



