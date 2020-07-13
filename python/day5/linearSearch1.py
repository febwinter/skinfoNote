from typing import Any

def linearSearch(lst:list, value:any)->int:
    i = 0
    while i != len(lst) and lst[i] != value:
        i += 1

    if i == len(lst):
        return -1
    else:
        return i