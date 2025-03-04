# -*- coding: utf-8 -*-
# @Author : ZhaoKe
# @Time : 2025-01-21 23:20
from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


def build_bitree(ver_list: List):
    if len(ver_list) == 0:
        return None
    node_list = []
    for item in ver_list:
        if item is None:
            node_list.append(None)
        else:
            node_list.append(TreeNode(val=item, left=None, right=None))
    # print("given nodes:", [str(v) for v in node_list])
    # print("count:", len(node_list))
    root = node_list[0]
    pre_st, pre_num = 0, 1
    st, num = 1, 2
    while st + num <= len(node_list):
        # print("find v from {} to {}".format(pre_st, pre_st+pre_num))
        for v in range(pre_st, pre_st + pre_num):
            if node_list[v] is None:
                continue
            else:
                node_list[v].left = node_list[2 * v + 1]
                node_list[v].right = node_list[2 * v + 2]
        pre_st, pre_num = st, num
        st = st + num
        num <<= 1
        # print("update v from {} to {}".format(pre_st, pre_st+pre_num))
        # print("update children v from {} to {}".format(st, st+num))
    return root


class BiTree:
    def levelOrderTravel(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            # print("ok")
            return []
        level_list = []
        cur_dq = deque()
        cur_dq.append(root)
        while len(cur_dq) > 0:
            ver_list = []
            next_dq = deque()
            while len(cur_dq) > 0:
                cur = cur_dq.popleft()
                ver_list.append(cur.val)
                if cur.left is not None:
                    next_dq.append(cur.left)
                if cur.right is not None:
                    next_dq.append(cur.right)
            level_list.append(ver_list)
            cur_dq = next_dq
        return level_list
        # print(["ok"])


if __name__ == '__main__':
    root = build_bitree([3, 9, 20, None, None, 15, 7])
    print(root, root.left, root.right, root.right.left, root.right.right)
    so = BiTree()
    print(so.levelOrderTravel(root))

    root = build_bitree([1])
    so = BiTree()
    print(so.levelOrderTravel(root))

    root = build_bitree([])
    so = BiTree()
    print(so.levelOrderTravel(root))
    # print([])
