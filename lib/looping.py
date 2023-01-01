#!/usr/bin/env python3

import ipdb

def happy_new_year():
    i = 10
    while i >= 0:
        if(i > 0):
            print(i)
        else:
            print('Happy New Year!')
        i-=1
    pass

def square_integers(int_list): return [num**2 for num in int_list]


def fizzbuzz():
    def is_fizzbuzz(num):
        if(num % 3 == 0 and num % 5 == 0):
            return "FizzBuzz"
        if(num % 3 == 0):
            return "Fizz"
        if(num % 5 == 0):
            return "Buzz"
        else:
            return num
    return [print(is_fizzbuzz(num+1)) for num in range(100)]