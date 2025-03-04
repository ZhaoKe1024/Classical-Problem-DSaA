#!/user/zhao/miniconda3/envs/torch-0
# -*- coding: utf_8 -*-
# @Time : 2025/1/4 11:43
# @Author: ZhaoKe
# @File : mathtricks.py
# @Software: PyCharm
import math
from typing import List


def fastpow(a: int, n: int) -> int:
    res = 1
    factor = a
    while n > 0:
        if (n & 1) == 1:
            res *= factor
        factor *= factor
        n >>= 1
    return res


def fastpowmod(a: int, n: int, c: int) -> int:
    res = 1
    factor = a % c
    while n > 0:
        if (n & 1) == 1:
            res *= (factor % c)
        factor *= (factor % c)
        n >>= 1
    return res


def eratosthenes_sieve(num: int) -> List[int]:
    sieve = [True] * (num + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.sqrt(num)) + 1):
        pointer = i << 1
        while pointer < num + 1:
            sieve[pointer] = False
            pointer += i
    primes = []
    for i in range(num + 1):
        if sieve[i]:
            primes.append(i)
    return primes


def gcd(a: int, b: int) -> int:
    if a == b:
        return a
    if b < a:
        a, b = b, a
    r = a % b
    while r != 0:
        a, b = b, r
        r = a % b
    return b


if __name__ == '__main__':
    # print(gcd(54, 21))
    # print(gcd(54, 18))
    # print(fastpow(2, 0))
    # print(fastpow(2, 1))
    # print(fastpow(2, 8))
    # print(fastpow(2, 7))
    print(fastpowmod(4, 1989, 5))
    # print(fastpowmod(2, 0, 3))
    # print(fastpowmod(2, 1, 3))
    # print((2 ** 8) % 3)
    # print(fastpowmod(2, 8, 3))
    # print((2 ** 7) % 3)
    # print(fastpowmod(2, 7, 3))
    # print(eratosthenes_sieve(101))
