# lab3.py
# Lab 3 - recursion  Kanaparan Arudchelvan

def factorial(number):
    # 0! = 1
    if number == 0:
        return 1

    # 1! = 1 (also stops)
    if number == 1:
        return 1

    # recursive part
    return number * factorial(number - 1)


def linear_search(list, key):
    # recursive linear search
    # only allowed to use len()

    def helper(pos):
        if pos >= len(list):
            return -1

        if list[pos] == key:
            return pos

        return helper(pos + 1)

    return helper(0)


def binary_search(list, key):
    # recursive binary search (list must be sorted)
    # only allowed to use len()

    def helper(lo, hi):
        if lo > hi:
            return -1

        mid = (lo + hi) // 2

        if list[mid] == key:
            return mid
        elif key < list[mid]:
            return helper(lo, mid - 1)
        else:
            return helper(mid + 1, hi)

    return helper(0, len(list) - 1)
