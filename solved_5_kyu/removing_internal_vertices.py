# https://www.codewars.com/kata/5da06d425ec4c4001df69c49/python

from typing import List, Tuple, Set

def remove_internal(triangles: List[Tuple[int, int, int]]) -> Set[int]:
    sides = []
    vertices = []
    for tup in triangles:
        sides.append((tup[0],tup[1]))
        sides.append((tup[1],tup[2]))
        sides.append((tup[2],tup[0]))
        for vertex in tup:
            vertices.append(vertex)

    vertices = set(vertices)

    outside_v = []

    for v in vertices:
        touching_v = []
        for side in sides:
            if v in side:
                for s in side:
                    touching_v.append(s)
        for t in touching_v:
            if touching_v.count(t) == 1:
                outside_v.append(v)
    
    return sorted(set(outside_v))
                    
print(remove_internal([(0, 2, 1), (3, 2, 1), (4, 2, 3), (0, 2, 4)]))