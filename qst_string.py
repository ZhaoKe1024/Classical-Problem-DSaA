#!/user/zhao/miniconda3/envs/torch-0
# -*- coding: utf_8 -*-
# @Time : 2025/3/5 9:23
# @Author: ZhaoKe
# @File : qst_string.py
# @Software: PyCharm


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        else:
            flag = True
            for it in palindrome:
                if it != "a":
                    flag = False
            if flag:
                return palindrome[:-1] + "b"
            for i in range(len(palindrome)):
                if palindrome[i] == "a":
                    continue
                else:
                    if i == len(palindrome) // 2:
                        for j in range(len(palindrome) - 1, i, -1):
                            if palindrome[j] == "a":
                                return palindrome[:j] + 'b' + palindrome[j + 1:]
                    else:
                        return palindrome[:i] + 'a' + palindrome[i + 1:]


if __name__ == '__main__':
    s = Solution()
    print(s.breakPalindrome("abccba"))
    print(s.breakPalindrome("aaaa"))
    print(s.breakPalindrome("aba"))
    print(s.breakPalindrome("aabaa"))
    print(s.breakPalindrome("a"))
    print(s.breakPalindrome("c"))
