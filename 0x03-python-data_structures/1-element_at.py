#!/usr/bin/python3
def element_at(my_list, index):
    listlength = len(my_list) - 1
    if (index < 0 or index > listlength):
        return (None)
    else:
        return (my_list[index])
