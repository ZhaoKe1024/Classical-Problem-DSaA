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
    """ return the primes from 2 to num, [2, nums].
    the primes from 2 to 1000:
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
    101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
    211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
    307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
    401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
    503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599,
    601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
    701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797,
    809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887,
    907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
    :param num:
    :return:
    """
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


def is_prime(num: int) -> bool:
    if num < 2:
        return False
    elif num == 2:
        return True
    elif (num & 1) == 0:
        return False
    for it in range(2, int(math.sqrt(num))+1):
        if num % it == 0:
            return False
    return True
    # 检测素数的常用方法：
    # 算法学习笔记(48): 米勒-拉宾素性检验 - Pecco的文章 - 知乎
    # https://zhuanlan.zhihu.com/p/220203643


def is_prime1(num: int) -> bool:
    if num < 2:
        return False
    elif num == 2:
        return True
    elif (num & 1) == 0:
        return False
    x = 2
    while num >= x ** 2:
        if num % x != 0:
            x += 1
        else:
            return False
    return True


def number_factorising(number: int) -> List[int]:
    res = list()
    if number < 4:
        res.append(number)
    else:
        x = 2
        while number >= x ** 2:
            if number % x != 0:
                x += 1
            else:
                res.append(x)
                number = number // x
        res.append(number)
    if len(res) == 1 and number != 1:
        # prime number
        return [1, number]
    if number == 1:
        # 1
        return [1]
    if len(res) > 1:
        return res

    # 素因子分解还有更牛的算法，贴个链接略了
    # 算法学习笔记(55): Pollard-Rho算法 - Pecco的文章 - 知乎
    # https://zhuanlan.zhihu.com/p/267884783


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


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minv, maxv = nums[0], nums[0]
        for it in nums:
            if it < minv:
                minv = it
            if it > maxv:
                maxv = it
        if minv == maxv:
            return minv
        r = maxv % minv
        while r > 0:
            maxv, minv = minv, r
            r = maxv % minv
        return minv


if __name__ == '__main__':
    # print(number_factorising(1))
    # print(number_factorising(2))
    # print(number_factorising(3))
    # print(number_factorising(6))
    # print(number_factorising(24))
    # print(number_factorising(64))
    # print(number_factorising(127))
    # s = Solution()
    # print(s.findGCD([2,5,6,9,10]))
    # print(s.findGCD([7,5,6,8,3]))
    # print(s.findGCD([3,3]))
    # print(gcd(54, 21))
    # print(gcd(54, 18))
    # print(fastpow(2, 0))
    # print(fastpow(2, 1))
    # print(fastpow(2, 8))
    # print(fastpow(2, 7))
    # print(fastpowmod(4, 1989, 5))
    # print(fastpowmod(2, 0, 3))
    # print(fastpowmod(2, 1, 3))
    # print((2 ** 8) % 3)
    # print(fastpowmod(2, 8, 3))
    # print((2 ** 7) % 3)
    # print(fastpowmod(2, 7, 3))

    nums = eratosthenes_sieve(1009)
    print(nums)
    # print(len(nums))
    # print([it*it for it in nums])
    # for it in range(100):
    #     print(it, it in nums, is_prime(it), is_prime1(it))
