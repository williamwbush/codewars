def next_multiple_of_five(n):
    b = str(bin(n))[2:]
    i = 0
    print(f'b = {b}')
    
    while True:
        next = b + str(bin(i))[2:][::-1]
        print(f'next = {next}')
        if int(next, 2) % 5 == 0:
            return int(next, 2)
        i += 1
        




