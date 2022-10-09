import matplotlib.pyplot as plt
import copy


class BrushTools:
    # 创建figure
    figure = plt.figure()
    # 创建axes
    axes = figure.add_subplot(1, 1, 1)

    # 保存点坐标
    v = []
    # 保存边关系
    e = []

    def __init__(self, v, e):
        self.v = v
        self.e = e

    # 在画布上画点
    def draw_vertex(self):
        # 标点
        self.axes.scatter(self.v[:, 0], self.v[:, 1], c="red")
        # 给点加注释
        for i in range(0, self.v.shape[0]):
            self.axes.annotate("v" + str(i),
                               xy=[self.v[i, 0], self.v[i, 1]],
                               xytext=[self.v[i, 0] + 0.05, self.v[i, 1] - 0.05])

    # 在画布上画边
    def draw_edge(self):
        # 标边
        ec = copy.deepcopy(self.e)
        count = 0
        for i in range(0, ec.shape[0]):
            for j in range(0, ec.shape[1]):
                if ec[i, j] > 0:
                    # 判断是不是环
                    if i == j:
                        self.axes.add_artist(plt.Circle((self.v[i, 0], self.v[i, 1] + 0.2), 0.2,
                                                        fill=False,
                                                        color="green"))

                        # 考虑多个环的情况，加多个注释
                        a_str = ""
                        for k in range(0, ec[i][j]):
                            a_str = a_str + "e" + str(count) + ","
                            count += 1

                        self.axes.annotate(a_str[:-1],
                                           xy=[self.v[i, 0] + 0.15, self.v[i, 1] + 0.3],
                                           xytext=[self.v[i, 0] + 0.15, self.v[i, 1] + 0.3])

                    else:
                        ec[j, i] = 0
                        x = [self.v[i, 0], self.v[j, 0]]
                        y = [self.v[i, 1], self.v[j, 1]]
                        self.axes.plot(x, y, c="green")

                        # 给边加注释(考虑平行边的情况)
                        a_str = ""
                        for k in range(0, ec[i][j]):
                            a_str = a_str + "e" + str(count) + ","
                            count += 1

                        xm = (self.v[i, 0] + self.v[j, 0]) / 2
                        ym = (self.v[i, 1] + self.v[j, 1]) / 2
                        self.axes.annotate(a_str[:-1], xy=[xm, ym], xytext=[xm + 0.02, ym + 0.02])

    # 画出图的补图（考虑简单无向图）
    def draw_complement(self):
        # 预处理，确保是简单无向图
        ec = copy.deepcopy(self.e)
        ec = self.transform2simple(ec)

        # 生成补图
        for i in range(0, ec.shape[0]):
            for j in range(0, ec.shape[1]):
                if i != j:
                    if ec[i][j] == 1:
                        ec[i][j] = 0
                    else:
                        ec[i][j] = 1

        # 画出补图
        e_temp = copy.deepcopy(self.e)
        self.e = ec
        self.show()
        self.e = e_temp

    # 将无向图转换为简单无向图(去环，去平行边)
    def transform2simple(self, e):
        for i in range(0, e.shape[0]):
            for j in range(0, e.shape[1]):
                # 去环
                if i == j:
                    e[i][j] = 0
                else:
                    # 去平行边
                    if e[i][j] > 0:
                        e[i][j] = 1
        return e

    def show(self):
        self.axes.cla()
        self.draw_vertex()
        self.draw_edge()

        plt.axis('scaled')
        self.figure.show()
