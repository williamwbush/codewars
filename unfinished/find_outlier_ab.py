def find_outlier(list_a):
    counter1 = 0
    list_odd = []
    counter2 = 0
    list_even = []
    for num in list_a:
        # if list_a.index(num) == len(list_a) - 1:
        #     return num
        if num % 2 != 0:
            counter1 += 1
            list_odd.append(num)
            if counter1 > 1 and counter2 == 1:
                return list_even[0]
        elif num % 2 == 0:
            counter2 += 1
            list_even.append(num)
            if counter2 > 1 and counter1 == 1:
                return list_odd[0]


list_a = [1,2,3,7]
print(find_outlier(list_a))