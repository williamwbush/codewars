# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

def snail(snail_map):
    clock = []
    while True:
        while len(snail_map[0]) > 0:
            clock.append(snail_map[0].pop(0))
        del snail_map[0]
        
        if not any(snail_map):
            return clock
        
        for lst in snail_map:
            clock.append(lst.pop())
             
        while len(snail_map[-1]) > 0:
            clock.append(snail_map[-1].pop())
        del snail_map[-1]
        
        if not any(snail_map):
            return clock
        
        for lst in snail_map[::-1]:
             clock.append(lst.pop(0))

print(snail([[1,2,3],
             [4,5,6],
             [7,8,9]]))