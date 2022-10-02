#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    reversed_list = []
    for i in my_list:
        reversed_list = [i] + reversed_list
    for j in reversed_list:
        print("{:d}".format(j))
