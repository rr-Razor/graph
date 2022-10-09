import numpy as np
from brush_tools import BrushTools
from calculate_tools import CalcTools

if __name__ == '__main__':
    # # 接收点
    # v = np.array([[1, 1], [1, 4], [7, 3], [5, 1]])
    # # 接收边
    # e = np.array([[1, 2, 0, 0],
    #               [2, 0, 0, 1],
    #               [0, 0, 0, 0],
    #               [0, 1, 0, 0]])

    # # 接收点
    # v = np.array([[1, 1], [1, 3], [2, 2], [3, 2]])
    # # 接收边
    # e = np.array([[0, 1, 1, 0],
    #               [1, 0, 1, 0],
    #               [1, 1, 1, 1],
    #               [0, 0, 1, 0]])

    # 接收点
    v = np.array([[1, 1], [1, 3], [3, 1], [3, 3], [5, 2], [7, 1], [7, 3], [9, 1], [9, 3]])
    # 接收边
    e = np.array([[0, 1, 1, 1, 0, 0, 0, 0, 0],
                  [1, 0, 1, 1, 0, 0, 0, 0, 0],
                  [1, 1, 0, 1, 1, 0, 0, 0, 0],
                  [1, 1, 1, 0, 1, 0, 0, 0, 0],
                  [0, 0, 1, 1, 0, 1, 1, 0, 0],
                  [0, 0, 0, 0, 1, 0, 1, 1, 1],
                  [0, 0, 0, 0, 1, 1, 0, 1, 1],
                  [0, 0, 0, 0, 0, 1, 1, 0, 1],
                  [0, 0, 0, 0, 0, 1, 1, 1, 0]
                  ])

    # 任务一：画出图G，并给所有顶点和边标号
    brush = BrushTools(v, e)
    brush.show()
    print("任务一：如图所示")

    # 任务二：求出图G的度序列
    calc = CalcTools(v, e)
    degrees = calc.calc_degrees()
    print("任务二：图的度序列为" + str(degrees))

    # 任务三：画出图G的补图
    brush.draw_complement()
    print("任务三：如图所示，原图已被处理为简单无向图")

    # 任务四：连通性
    calc = CalcTools(v, e)
    flag = calc.judge_connect()
    print("任务四：该图的连通性为" + str(flag))

    # 任务五：求边连通度和点连通度
    calc = CalcTools(v, e)
    e_cut_set = calc.calc_edge_connect()
    print("任务五、六：边连通度是" + str(len(e_cut_set)) + ",最小边割集是" + str(e_cut_set))

    v_cut_set = calc.calc_vertex_connect()
    print("任务五、六：点连通度是" + str(len(v_cut_set)) + ",最小点割集是" + str(v_cut_set))
