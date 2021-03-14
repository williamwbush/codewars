# # Perfect Squares
# # ---------------
# # Given a positive integer num, write a function which returns True if num is a perfect square else False.
# # Follow up: Do not use any built-in library function such as sqrt.
# # Example 1:
# # Input: num = 16
# # Output: True
# # Example 2:
# # Input: num = 14
# # Output: False
# # Constraints:
# # 1 <= num <= 2^31 - 1

print(2**31)

def perfect(num):
    squares = [n**2 for n in range(214748)]
    if num in squares:
        return True 
    else:
        return False

# print(perfect(16))
# print(perfect(14))


# Two Sum Problem
# ---------------
# Create a function that given a list of numbers (that are sorted) and a target number as a sum, return the two index numbers that when added equal the target number
# Example Input: [2,7,11,15], target = 9
# Example Output: [0,1]

def two_sum(num_list, target):
    for i in range(len(num_list)):
        for j in range(len(num_list)):
            if num_list[i] + num_list[j] == target:
                return [i,j]

print(two_sum([2,7,11,15],9))

def two_sum_better(num_list, target):
    d = {}
    for num in num_list:
        d[num] = target - num
    for key, value in d.items():
        if value in num_list:
            return [num_list.index(key), num_list.index(value)]

print(two_sum_better([2,7,11,15],9))

def two_sum_3(num_list, target):
    for num in num_list:
        a = target - num
        if a in num_list:
            return [num_list.index(num), num_list.index(a)]

print(two_sum_3([2,7,11,15],9))



