#https://www.codewars.com/kata/564057bc348c7200bd0000ff/python

def thirt(n):    
    sequence = [1, 10, 9, 12, 3, 4]
    sum1, sum2 = -1, -1
    
    while True:
        n = [int(i) for i in list(str(n))]
        sum2 = sum(sequence[(len(n) - 1 - i) % 6] * n[i] for i in range(len(n)))
        if sum2 == sum1:
            return sum2
        sum1 = sum2
        n = sum2

print(thirt(1234567))