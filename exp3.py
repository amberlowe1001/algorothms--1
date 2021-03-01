# Python Program to find Sum of Even and Odd Numbers in a List
import builtins
from numbers import Number


def even_sum(num_list):
    evensum = 0
    for j in range(int):
        if num_list[j] % 2 == 0:
            evensum = evensum + num_list[j]
    return evensum


def odd_sum(num_list):
    odds = 0
    for j in range(int):
        if num_list[j] % 2 != 0:
            odds = odds + num_list[j]
    return odds
