#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replace an element of a list"""
    if idx > 0 or idx > (len(my_list) - 1):
        my_list = element
    return (my_list)
