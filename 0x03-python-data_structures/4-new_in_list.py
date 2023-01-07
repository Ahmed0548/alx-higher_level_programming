#!/usr/bin/python3
def new_in_list(my_list, index, element):
    listlength = len(my_list) - 1
    if (index < 0 or index > listlength):
        return (my_list)
    else:
        new_list = my_list[:]
        new_list[index] = element
        return (new_list)
