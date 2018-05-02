# Prompt: Write two functions to find the minimum number in a list. The first function should compare each number to
# every other number in the list O(n^2). The second function should be linear O(n).


import random


num_list = random.sample(range(0,100),10) #creates list of ten random integers from 0 to 99


def get_min_num_On2(some_list):
    for i in some_list:
        is_smallest = True
        while is_smallest == True:
            for j in some_list:
                if j < i:
                    is_smallest = False
            if is_smallest:
                return i


def get_min_num_On(some_list):
    min_num = some_list[0]

    for num in some_list:
        if num < min_num:
            min_num = num

    return min_num


print(get_min_num_On2(num_list))

print(get_min_num_On(num_list))