from typing import Any

def linearSearch(lst:list,value:Any)->int:
    i = 0

    for i in range(len(lst)):
        if lst [i] == value:
            return i
    
    return -1

