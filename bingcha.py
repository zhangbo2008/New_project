import numpy as np
import os


class DIS_JOIN(object):
    def __init__(self):
        '''
        并查集算法
        拥有两个函数
        一个是把某个元素放在某个集合中
        另一个是返回一个list，包含所有集合和集合中所有的点
        '''
        self.Set = None
        self.Sum = None
        self.n = None

    def clear(self, n):
        '''
        初始化
        n为一共有多少个元素
        '''
        self.Set = np.zeros(n, dtype=int)
        self.Set = self.Set - 1     # 都初始化为-1. 表示他自己就是根.   Set是一个数组.
        # Set[i] 表示i的根是谁.
        self.Sum = n
        self.n = n
        return

    def find_r(self, p):
        '''
        返回p属于那一个集合
        '''
        if self.Set[p] < 0:
            return p

        self.Set[p] = self.find_r(self.Set[p])  #通过迭代不停的找根.
        return self.Set[p]

    def join(self, a, b):
        '''
        将元素b加入元素a所在的集合中
        '''
        ra = self.find_r(a)
        rb = self.find_r(b)
        if (ra != rb):
            self.Set[rb] = ra
            self.Sum = self.Sum - 1
        return

    def get_set(self):
        '''
        返回一个list，每个元素是一个set
        '''
        Set = [None] * self.Sum
        cnt = 0

        lis = [None] * self.n
        for k in range(self.n):
            lis[k] = [k, self.find_r(k)]         # 把 节点,节点的根   这个tuple 存入lis
        lis.sort(key=lambda x: (x[1]))
        lis.append([-100, -100])  # 加一个终止条件?干啥用的....如果不加的话,下面for循环会少跑一次.因为显然节点pre里面不可能取到-100.所以这么加是没错的.

        pre = lis[0][-1]             # 编号最小的根
        pre_poi = 0

        for k in range(1, self.n + 1):
            if lis[k][-1] != pre:
                element_set = [None] * (k - pre_poi)
                for i in range(pre_poi, k):   # 从pre_poi 到k-1 都指向pre 因为上面的if条件.
                    element_set[i - pre_poi] = lis[i][0]
                Set[cnt] = np.array(element_set)
                cnt = cnt + 1 # cnt 表示武林门派的数量.  也就是根的数量.用的是左层云的比喻哈哈.
                pre = lis[k][-1]
                pre_poi = k

        return Set


if __name__ == '__main__':
    dis_join = DIS_JOIN()
    dis_join.clear(8)
    dis_join.join(0, 3)
    dis_join.join(1, 4)
    dis_join.join(0, 1)
    dis_join.join(2, 5)
    Set = dis_join.get_set()
    print(Set)
    # for k in range(5):
    #     print(k, dis_join.find_r(k))
    # print(dis_join.Sum)

    '''
    挺牛逼啊,做一下总结吧..
    
    运行完上面的结果.就会得到各个门派的分类结果.
    '''