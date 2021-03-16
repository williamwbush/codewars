# https://www.codewars.com/kata/554f76dca89983cc400000bb

# In mathematics, a Diophantine equation is a polynomial equation, usually with two or more unknowns, such that only the integer solutions are sought or studied.

# In this kata we want to find all integers x, y (x >= 0, y >= 0) solutions of a diophantine equation of the form:

# x2 - 4 * y2 = n
# (where the unknowns are x and y, and n is a given positive number) in decreasing order of the positive xi.

# If there is no solution return [] or "[]" or "". (See "RUN SAMPLE TESTS" for examples of returns).

## REFACTORED SOLUTION

from math import sqrt

def sol_equa(n):
    solution = []
    
    for i in range(1, round(sqrt(n)) + 1):
        j = n / i    
        x = (i + j) / 2
        y = (j - i) / 4
        if x % 1 == 0 and y % 1 == 0: 
            solution.append([int(x),int(y)])
    
    return solution


### FIRST SOLUTION

def sol_equa(n):
    from math import sqrt
    
    sqrt = sqrt(n)
    factors = []
    
    for i in range(1, round(sqrt) + 1):
        if n % i == 0:
            factors.append(i)
            factors.append(int(n/i))

    factors = sorted(set(factors))
    solution = []
    
    for i in factors:
        j = n / i    
        x = i + (j-i)/2
        y = (j - i) / 4
        if x % 1 == 0 and y % 1 == 0 and x >= 0 and y >= 0: 
            solution.append([int(x),int(y)])
    
    return solution