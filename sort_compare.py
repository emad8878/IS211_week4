#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week4 algorithm module."""


import time
import random


def insertion_sort(lists):
    """This function sort list."""
    start = time.time()
    for index in range(1, len(lists)):
        current_value = lists[index]
        position = index
        while position > 0 and lists[position - 1] > current_value:
            lists[position] = lists[position - 1]
            position = position - 1
        lists[position] = current_value
    end = time.time()
    return end-start, lists


def gap_insertion_sort(lists, start, gap):
    """Insertion function."""

    for i in range(start + gap, len(lists), gap):
        current_value = lists[i]
        position = i
        while position >= gap and lists[position - gap] > current_value:
            lists[position] = lists[position - gap]
            position = position - gap
        lists[position] = current_value


def shell_sort(lists):
    """A shell function."""
    start = time.time()
    sublist_count = len(lists) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(lists, start_position, sublist_count)
        sublist_count = sublist_count // 2
    end = time.time()
    return end-start, lists


def python_sort(lists):
    """sort function."""
    start = time.time()
    lists = lists.sort()
    end = time.time()
    return end-start, lists


def random_list(avg_time):
    """Random Function."""
    my_list = []
    for item in range(avg_time):
        my_list.append(random.randint(1,avg_time))
    return my_list


def main():
    """main function."""
    test_num = [500, 1000, 10000]

    for i in test_num:
        counter = 100
        result = [0, 0, 0]

        while counter > 0:
            my_list = random_list(i)
            result[0] += insertion_sort(my_list)[0]
            result[1] += shell_sort(my_list)[0]
            result[2] += python_sort(my_list)[0]
            counter -= 1
        print 'For the list of {}... '.format(i)
        print ('Insertion Sort took %10.7f seconds to run,'
               'on average.' % (result[0] / 100))
        print ('Shell Sort ' + 'took %10.7f seconds to run,'
               'on average.' % (result[1] / 100))
        print ('Python Sort ' + 'took %10.7f seconds to run,'
               'on average.' % (result[2] / 100))

if __name__ == "__main__":
    main()
