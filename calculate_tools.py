import copy
from itertools import *

import numpy as np


class CalcTools:
    # 保存点坐标
    v = []
    # 保存边关系
    e = []

    # 临时变量
    v_connect = []

    def __init__(self, v, e):
        self.v = v
        self.e = e

    # 计算图的度序列
    def calc_degrees(self):
        d_line = []
        d = 0
        for i in range(0, self.e.shape[0]):
            for j in range(0, self.e.shape[1]):
                if self.e[i][j] > 0:
                    if i == j:
                        d += 2 * self.e[i][j]
                    else:
                        d += 1 * self.e[i][j]
            d_line.append(d)
            d = 0
        # print("任务二：图的度序列为" + str(d_line))
        return d_line

    # 计算图的连通性
    def calc_connect(self, flag):
        self.v_connect.append(flag)
        for i in range(0, self.e.shape[1]):
            if i > 0 and i not in self.v_connect:
                if self.e[flag][i] != 0:
                    self.calc_connect(i)

    # 判断连通性
    def judge_connect(self):
        flag = False
        self.calc_connect(0)
        result = list(set(self.v_connect))
        self.v_connect = []
        if len(result) == self.e.shape[0]:
            # print("任务四：该无向图是连通的")
            flag = True
        else:
            # print("任务四：该图只有" + str(len(result)) + "个点是连通的，分别是" + str(result))
            # print("任务四：该无向图是不连通的")
            flag = False
        return flag

    # 判断连通性
    def judge_connect_complex(self, v_size, del_v):
        flag = False
        for i in range(0, v_size):
            if i not in del_v:
                # print(i)
                self.calc_connect(i)
                break

        result = list(set(self.v_connect))
        self.v_connect = []

        if len(result) == v_size - len(del_v):
            # print(v_size - len(del_v))
            # print("任务四：该无向图是连通的")
            flag = True
        else:
            # print("任务四：该图只有" + str(len(result)) + "个点是连通的，分别是" + str(result))
            # print("任务四：该无向图是不连通的")
            flag = False
        return flag

    # 计算边连通度
    def calc_edge_connect(self):
        # 深拷贝原邻接矩阵
        dc_e = copy.deepcopy(self.e)

        # 判断是不是连通图
        if not self.judge_connect():
            return []

        # 计算图中的所有边数
        e_count = 0
        for i in range(0, self.e.shape[0]):
            for j in range(0, self.e.shape[1]):
                e_count = e_count + self.e[i][j]
        e_count = int(e_count / 2.0)
        # print("总边数" + str(e_count))

        e_combination = range(1, e_count + 1)

        # 删边，然后判断是否连通
        for num in range(1, self.e.shape[0]):

            # 确定要删除的边组合
            e2del = list(combinations(e_combination, num))
            # print(e2del)
            # 循环删除要删除的边组合
            for edges in e2del:
                del_count = 0

                cut = []

                temp_e = copy.deepcopy(self.e)
                for i in range(0, temp_e.shape[0]):
                    for j in range(i + 1, temp_e.shape[1]):
                        while temp_e[i][j] > 0:
                            del_count += 1
                            temp_e[i][j] -= 1
                            temp_e[j][i] -= 1

                            for e in edges:
                                # 说明该边在要删除的边组合中
                                if del_count == e:
                                    self.e[i][j] = 0
                                    self.e[j][i] = 0
                                    # print(str(self.e))
                                    # 对该边进行保存
                                    cut.append((i, j))
                # 删除完边，判断图的连通性
                # print("测试连通性" + "\n" + str(self.e))

                flag = self.judge_connect()

                # 对边进行还原
                self.e = copy.deepcopy(dc_e)

                if not flag:
                    return cut

        self.e = copy.deepcopy(dc_e)

    # 计算点连通度
    def calc_vertex_connect(self):

        # 深拷贝原邻接矩阵
        dc_e = copy.deepcopy(self.e)

        # 判断是不是连通图
        if not self.judge_connect():
            return []

        # 计算图中的所有点个数
        v_count = self.v.shape[0]
        # print("总点数" + str(v_count))

        v_combination = range(0, v_count)

        # 删点和相关联的边，然后判断是否连通
        for num in range(1, self.v.shape[0]):

            # 确定要删除的点组合
            v2del = list(combinations(v_combination, num))
            # print(v2del)

            # 循环删除要删除的点和边组合
            for vertexes in v2del:
                del_count = 0

                cut = []

                # print(vertexes)

                self.e = np.array(self.e)
                for v in vertexes:
                    self.e[v, :] = 0
                    self.e[:, v] = 0
                    cut.append(v)

                # 删除完点和关联边，判断图的连通性
                # print("测试连通性" + "\n" + str(self.e))

                if num == self.v.shape[0] - 1:
                    return cut

                flag = self.judge_connect_complex(self.v.shape[0], vertexes)

                if not flag:
                    return cut

                # 对边进行还原
                self.e = copy.deepcopy(dc_e)

            # print("===================================")

        self.e = copy.deepcopy(dc_e)
