#!/usr/bin/python3
def delete_at(my_list=[], index=0):
    length_list = len(my_list) - 1
    if index < 0 or index > length_list:
        return(my_list)
    else:
        del my_list[index]
        return(my_list)
