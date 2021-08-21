import sys
"""
输入：
3 1
-1 1 3
1 1 3
输出：
3
https://blog.csdn.net/qq_18055167/article/details/108660179
"""
def myfun(n,xset,sset):
    if n==0:
        return sset[n]
    res=[]
    for i in range(n):
        if (n-i)*d>=abs(xset[n]-xset[i]):
            res.append(myfun(i,xset,sset)+sset[n])
    return max(res)

n,d = map(int,sys.stdin.readline().strip().split())
xset = list(map(int,sys.stdin.readline().strip().split()))
sset=list(map(int,sys.stdin.readline().strip().split()))
# n,d=4,1
# xset=[-1,1,1,3]
# sset=[4,5,6,8]
xset.insert(0,0)
sset.insert(0,0)
res=[]
for i in range(n+1):
    res.append(myfun(i,xset,sset))
print(max(res))