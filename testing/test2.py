# def power_sumDigTerm(n):
#     from math import log
#     psds = []
#     i = 81
#     while len(psds) <= n:
#         for power in range(2, round(log(i,2))):
#             print(f'trying {i}, {power}')
#             if i == sum([int(d) for d in list(str(n))]) ** power:
#                 psds.append(i)
#             else:
#                 print(f'{i}, {power} didnt work')
#         i += 1
#         print(f'i = {i}')
#     return psds[-1]
# power_sumDigTerm(2)


# print(sum([int(d) for d in list(str(81))]) ** 2)

# print(list(str(1234)))

# if "0" in "01":
#     print('hi')

# def isDividingNumber(num):
#     n = num
#     while n > 0:
#         n, i = divmod(n, 10)
#         if i == 0 or (num % i ) != 0:
#             return False
#     return True
# print([num for num in range(1, 1122+1) if isDividingNumber(num)])

# output = []
# for num in range (1, 1000 + 1):
#     if '0' not in str(num):
#         ls = []
#         for i in list(str(num)):
#             if num % int(i) == 0:
#                 ls.append(i)
#         if len(ls) == len(str(num)):
#             output.append(num)
# print(output)

# from math import sqrt
# for i in range(1, 13858000):
#     if type(sqrt(13858000 - (i**2))) == int:
#         print(i)

# alist = [1, 0, 2]
# while alist[0] == 0:
#     for i in range(len(alist)-1):
#         if alist[i] == 0:
#             zero = alist.pop(i)
#             alist.append(zero)
# print(alist)


# Lucky Numbers
# Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.
# Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is no lucky integer return -1.White
# Example 1:
# Input: arr = [2,2,3,4]
# Output: 2
# Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
# Example 2:
# Input: arr = [1,2,2,3,3,3]
# Output: 3
# Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.

# def Lucky(arr):
#     lucky_ints = []
#     for num in arr:
#         if num == arr.count(num):
#             lucky_ints.append(num)
#     if lucky_ints == []:
#         print(-1)
#     else:
#         print(max(lucky_ints))

# Lucky([2,2,3,4])

# Remove Element
# Given an array nums and a value val, remove all instances of that value in-place and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
# Example 1:
# Given nums = [3,2,2,3], val = 3,
# Your function should return length = 2, with the first two elements of nums being 2.
# It doesn't matter what you leave beyond the returned length.
# Example 2:
# Given nums = [0,1,2,2,3,0,4,2], val = 2,
# Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.
# Note that the order of those five elements can be arbitrary.
# It doesn't matter what values are set beyond the returned length.

# def remove(alist, val):
#     while val in alist:
#         alist.remove(val)
#     print(len(alist))

# remove([0,1,2,2,3,0,4,2], 2)

lst = ['dad', 'racecar', 'baseball']
print(len(max([i for i in lst if i == i[::-1]])))

