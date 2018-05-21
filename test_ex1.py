#!/usr/bin/env python3

"""
    test_ex1.py - Test program using the py.test module to test the functions from Ex1.pye
    author: Nayeem Aquib
    date: 05/10/2018
    email: nayeemaquib@bennington.edu

"""


import Ex1

def test_add_two_numbers():
    result = Ex1.add_two_numbers(10, 90)
    assert result == 100

def test_subtract_two_numbers():
    result = Ex1.subtract_two_numbers(5, 4)
    assert result == 1

def test_multiply():
    result = Ex1.multiply(4, 5)
    assert result == 20

def test_divide():
    result1 = Ex1.divide(30, 6)
    result2 = Ex1.divide(31, 6)
    assert result1 == 5
    assert result2 == 5

def test_calc_ascii_val_of_string():
    result1 = Ex1.calc_ascii_val_of_string('ZZZ')
    result2 = Ex1.calc_ascii_val_of_string('ZZZ ZZZ')
    assert result1 == 270
    assert result2 == 572

def test_length_guesser():
    result1 = Ex1.length_guesser('Dickinson Catlab', 16)
    result2 = Ex1.length_guesser('Dickinson Catlab', 8)
    result3 = Ex1.length_guesser('Dickinson Catlab', 32)
    assert result1 == 0
    assert result2 == 1
    assert result3 == -1

