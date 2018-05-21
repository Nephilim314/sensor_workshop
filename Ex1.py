#!/usr/bin/env python3

"""
    Ex1.py - Solution of the three problems from the first sensor workshop lab
    author: Nayeem Aquib
    date: 05/10/2018
    email: nayeemaquib@bennington.edu

"""

# Problem 1

def add_two_numbers(num1, num2):
    return num1 + num2

def subtract_two_numbers(num1, num2):
    return num1 - num2


def multiply(num, times):
    if not isinstance(num and times, int):
        raise TypeError("Int only, bud!")
    else:
        res = 0
        while num > 0:
            if num % 2 == 1:
                res += times
            times = times << 1
            num = num >> 1
        return res

print(multiply(10, 'a'))

def divide(num, times):
    try:
        res = 0
        while num > 0:
            num -= times
            if num >= 0:
                res += 1
        return res
    except TypeError as e:
        print(e)

print(divide(100, 'ask'))

# Problem 2

def calc_ascii_val_of_string(string):
    asciiDict = {chr(i): i for i in range(129)}
    sum = 0
    for i in string:
        sum += asciiDict[i]
    return sum

# Problem 3

def length_guesser(my_string, my_length_guess):
    if len(my_string) == my_length_guess:
        return 0
    if len(my_string) > my_length_guess:
        return 1
    if len(my_string) < my_length_guess:
        return -1

# def main():
#     assert multiply(4, 5)==28
#
# print(main())