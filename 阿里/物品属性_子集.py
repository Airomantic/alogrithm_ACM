import sys
"""
https://www.nowcoder.com/test/question/a55198d2e65746009110226f2f6c8533?pid=30440638&tid=46176333
输入
2
3
1 3 2
0 2 3
输出
2
输入：
4
1 5 4 2
10 32 19 21
输出
3
argsort() argsort返回数据从小到大的索引值，即先从小到大排序，再取元素原来的索引值进行替换
https://blog.csdn.net/AILEARNER_L/article/details/105509127
"""
import numpy as np
def myfun(n,val,x,y):
    if n==0:
        return 0
    res=[]
    for k in range(n):
        if y[k]<val:
            res.append(myfun(k,y[k],x,y)+1) #当n==0时，res可获得(0+1)
    if res:
        return max(res)
    else:
        return 0
def main(n,x,y):
    index=np.argsort(x)
    y=y[index] #x取索引后覆盖原来y的元素
    res = []
    for k in range(n):
        res.append(myfun(k, y[k],x,y) + 1)
    return max(res)



N=int(sys.stdin.readline().strip())
for i in range(N):
    n=int(sys.stdin.readline().strip())
    x=np.array(list(map(int,sys.stdin.readline().strip().split(' '))))
    y=np.array(list(map(int,sys.stdin.readline().strip().split(' '))))

    res1=main(n,x,y)
    # res1=0
    res2=main(n,-x,-y)
    print(max(res1,res2))
