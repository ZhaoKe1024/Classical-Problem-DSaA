#!/user/zhao/miniconda3/envs/torch-0
# -*- coding: utf_8 -*-
# @Time : 2025/2/25 9:26
# @Author: ZhaoKe
# @File : Astar.py
# @Software: PyCharm


def get_map():
    return [
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 0, 0, 0, 0, 0, 0, 0, -1],
        [-1, 0, 0, 0, -1, 0, 0, 0, -1],
        [-1, 0, 0, 0, -1, 0, 0, 0, -1],
        [-1, 0, 0, 0, -1, 0, 0, 0, -1],
        [-1, 0, 0, 0, 0, 0, 0, 0, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1]
    ]


def distance(pos1, pos2):
    return abs(pos1[1] - pos2[1]) + abs(pos1[0] - pos2[0])


def min_dis_pos(arrlist):
    minindex = 0
    minvalue = arrlist[0][0]
    for i in range(1, len(arrlist)):
        if arrlist[i][0] < minvalue:
            minindex = i
    return minindex


def get_list_str(arrlist):
    res = ""
    for item in arrlist[:-1]:
        res += str(item) + "\t"
    return res + str(arrlist[-1])


def print_new_map(amap, path):
    for item in path:
        # print(item)
        amap[item[0]][item[1]] = 1
    R, C = len(amap), len(amap[0])
    for i in range(R):
        print(get_list_str(amap[i]))


def astar_4direction(amap, st, en):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    # G_list = [0]
    # F_list = [st[1]]
    g_score = {st: 0}
    open_list = [(distance(st, en), st)]
    # close_list = []
    came_from = {}
    while open_list:
        ind = min_dis_pos(open_list)
        current_f, current_pos = open_list[ind]
        # print("select point:", current_pos, ", F:", current_f)
        del open_list[ind]
        if current_pos == en:
            path = []
            while current_pos in came_from:
                path.append(current_pos)
                current_pos = came_from[current_pos]
            path.append(st)
            path.reverse()
            return path
        for direction in directions:
            neighbor = (current_pos[0] + direction[0], current_pos[1] + direction[1])
            if (0 < neighbor[0] < len(amap)) and (0 < neighbor[1] < len(amap[0])) and (
                    amap[neighbor[0]][neighbor[1]] == 0):
                tentative_g_score = g_score[current_pos] + 1
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + distance(neighbor, en)
                    open_list.append((f_score, neighbor))

                    came_from[neighbor] = current_pos
        # print(open_list)
    return []


def astar_8direction(amap, st, en):

    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (0, -1), (1, 0), (1, -1), (-1, -1)]
    # G_list = [0]
    # F_list = [st[1]]
    g_score = {st: 0}
    open_list = [(distance(st, en)*10, st)]
    # close_list = []
    came_from = {}
    while open_list:
        ind = min_dis_pos(open_list)
        current_f, current_pos = open_list[ind]
        # print("select point:", current_pos, ", F:", current_f)
        del open_list[ind]
        if current_pos == en:
            path = []
            while current_pos in came_from:
                path.append(current_pos)
                current_pos = came_from[current_pos]
            path.append(st)
            path.reverse()
            return path
        for direction in directions:
            neighbor = (current_pos[0] + direction[0], current_pos[1] + direction[1])
            if (0 < neighbor[0] < len(amap)) and (0 < neighbor[1] < len(amap[0])) and (
                    amap[neighbor[0]][neighbor[1]] == 0):
                if 0 in direction:
                    tentative_g_score = g_score[current_pos] + 10
                else:
                    tentative_g_score = g_score[current_pos] + 14
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + distance(neighbor, en)*10
                    open_list.append((f_score, neighbor))

                    came_from[neighbor] = current_pos
        # print(open_list)
    return []


if __name__ == '__main__':
    st, en = (3, 2), (3, 6)
    amap = get_map()
    path = astar_8direction(amap=amap, st=st, en=en)
    print(path)
    print_new_map(amap, path)
