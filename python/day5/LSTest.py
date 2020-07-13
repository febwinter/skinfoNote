import time
import linearSearch1
import linearSearch2
import linearSearch3

from typing import Any

def time_it(search: callable([[list, Any],Any]), L: list, v: Any) -> float:

    t1 = time.perf_counter()
    search(L,v)
    t2 = time.perf_counter()
    return (t2 - t1) * 1000.0

def print_times(V: Any, L: list)->None:

    t1 = time.perf_counter()
    L.index(V)
    t2 = time.perf_counter()
    index_time = (t2 - t1) * 1000.0

    while_time = time_it(linearSearch1.linearSearch, L, V)
    for_time = time_it(linearSearch2.linearSearch, L, V)
    sentinel = time_it(linearSearch3.linearSearch, L, V)

    print('{0}\t{1:.2f}\t{2:.2f}\t{3:.2f}\t{4:.2f}'.format(V, while_time, for_time, sentinel, index_time))

L = list(range(10000001))

print_times(10,L)
print_times(5000000,L)
print_times(10000000, L)
