# https://www.codewars.com/kata/52b7ed099cdc285c300001cd

def sum_of_intervals(intervals):
    expans = []
    for interval in intervals:
        expan = list(range(interval[0],interval[1]+1))
        expans.append(expan)   
    
    adjacents = []
    for expan in expans:
        for i in range(len(expan)-1):
            adjacent = str(expan[i]) + str(expan[i+1])
            adjacents.append(adjacent)
    
    return len(set(adjacents))

print(sum_of_intervals( [
   [1,5],
   [10, 20],
   [1, 6],
   [16, 19],
   [5, 11]
] ))

