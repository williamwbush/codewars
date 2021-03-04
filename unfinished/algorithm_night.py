# Problem 1:
# https://www.hackerrank.com/challenges/counting-valleys/problem
# Problem 2:
# You found directions to hidden treasure only written in words. The possible directions are "NORTH", "SOUTH","WEST","EAST".
# "NORTH" and "SOUTH" are opposite directions, as are "EAST" and "WEST". Going one direction and coming back in the opposite direction leads to going nowhere. Someone else also has these directions to the treasure and you need to get there first. Since the directions are long, you decide to write a program top figure out the fastest and most direct route to the treasure. 
# Write a function that will take a list of strings and will return a list of strings with the unneeded directions removed (NORTH<->SOUTH or EAST<->WEST side by side).
# Example 1:
# input: ['NORTH','EAST','WEST','SOUTH','WEST','SOUTH','NORTH','WEST']
# output:['WEST','WEST']
# In ['NORTH','EAST','WEST','SOUTH','WEST','SOUTH','NORTH','WEST'] 'NORTH' and 'SOUTH' are not directly opposite but they become directly opposite after reduction of 'EAST' and 'WEST'. The whole path can be reduced to ['WEST','WEST'].
# Example 2:
# input: ['EAST','NORTH','WEST','SOUTH']
# output:['EAST','NORTH','WEST','SOUTH']
# Not all paths are reducible. The path ['EAST','NORTH','WEST','SOUTH'] is not reducible. 'EAST' and 'NORTH', 'NORTH' and 'WEST', 'WEST' and 'SOUTH' are not directly opposite of each other and thus can't be reduced. The resulting path has

inp = ['EAST','NORTH','WEST','SOUTH']

position = [0,0]

for d in inp:
    if d == 'NORTH':
        position[1] += 1
    elif d == 'SOUTH':
        position[1] -= 1
    elif d == 'EAST':
        position[0] += 1
    elif d == 'WEST':
        position[0] -= 1
print(position)

directions = []

if position[0] > 0:
    for i in range(position[0]):
        directions.append('EAST')
if position[0] < 0:
    for i in range(abs(position[0])):
        directions.append('WEST')
if position[1] > 0:
    for i in range(position[1]):
        directions.append('NORTH')
if position[1] < 0:
    for i in range(abs(position[1])):
        directions.append('SOUTH')      

print(directions)
