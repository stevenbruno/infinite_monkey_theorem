"""
Prompt: Write two functions to find the minimum number in a list. The first function should compare each number to
every other number in the list O(n^2). The second function should be linear O(n). From Miller and Ranum.
Author: Steven Bruno
To Do: progress bar
"""

from random import randrange
import timeit
import matplotlib.pyplot as plt
import sys


def get_min_num_On2(some_list):
    for i in some_list:
        is_smallest = True
        if is_smallest == True:
            for j in some_list:
                if j < i:
                    is_smallest = False
            if is_smallest == True:
                return i


def get_min_num_On(some_list):
    min_num = some_list[0]

    for num in some_list:
        if num < min_num:
            min_num = num

    return min_num


list_range = []  # range for x axis in time complexity plot
On2_time = []    # for storing On2 times for plot
On_time = []     # for storing On times for plot


if __name__ == '__main__':
    for list_size in range(20, 501, 20):
        list_range.append(list_size)
        alist = [randrange(101) for i in range(list_size)]
        t1 = timeit.Timer("get_min_num_On2(alist)", "from __main__ import get_min_num_On2, alist")
        t2 = timeit.Timer("get_min_num_On(alist)", "from __main__ import get_min_num_On, alist")
        On2_time.append(t1.timeit(number=1000))
        On_time.append(t2.timeit(number=1000))


    plt.plot(list_range, On2_time, 'bo', label="On2")
    plt.plot(list_range, On_time, 'ro', label="On")

    plt.xlabel('list size')
    plt.ylabel('function runtime (ms)')
    plt.title('time complexity of linear and exponential functions')

    plt.legend()

    plt.show()
