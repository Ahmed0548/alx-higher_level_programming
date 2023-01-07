#!/usr/bin/python3
def replace_in_list(my_list, index, element):
    listlength = len(my_list) - 1
    if (index < 0 or index > listlength):
        return (my_list)
    else:
        my_list[index] = element
        return (my_list)
