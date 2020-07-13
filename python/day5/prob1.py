from typing import Any

def linearSearch1_back(L:list, value:any)->int:

    i = len(L) - 1

    while i >= 0 and L[i] != value:
        i -= 1
    
    if L[i] != value:
        return -1
    else:
        return i

def linearSearch2_back(L:list, value:any)->int:

    for i in range(len(L) - 1, 0, -1):
        if L[i] == value:
            return i

    return -1

def linearSearch3_back(L:list, value:any)->int:

    L.insert(value,0)
    
    i = len(L) - 1

    while L[i] != value:
        i -= 1
    L.remove(0)

    if i == 0:
        return -1
    else:
        return i - 1
