def apply(num, f):
    return f(num)

def double(num):
    return 2 * num

#print(apply(5, lambda num: 2 * num))

from functools import reduce
from typing import List, Callable, TypeVar

dollars = ["32$", "15$", "12$", "17$", "20$"]

prices = map(lambda dollar: int(dollar[0:-1]), dollars)
expensive = filter(lambda price: price >= 20, prices)
total = reduce(lambda acum, price: acum+price ,expensive, 0)
##print(total)

E = TypeVar('E')
R = TypeVar('R')
A = TypeVar('A')

def map2(iterable: List[E], func: Callable[[E], R]) -> List[R]:
    mapped: List[R] = []
    for e in iterable:
        mapped.append(func(e))
    
    return mapped

def filter2(iterable: List[E], func: Callable[[E], R]) -> List[R]:
    filtered: List[E] = []
    for e in iterable:
        if func(e):
            filtered.append(e)
    return filtered

def reduce2(iterable: List[E], func: Callable[[A,E], R],acum: A) -> A:
    for e in iterable:
        acum = func(acum, e)
    return acum


prices = map2(dollars, lambda dollar: int(dollar[0:-1]))
expensive = filter2(prices, lambda price: price >= 20)
total = reduce2(expensive, lambda acum, price: acum+price, 0)
print(prices)
print(expensive)
print(total)