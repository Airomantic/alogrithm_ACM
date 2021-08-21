import io
import sys

"""
输入：
3
输出：
58
91
100
"""
class Solution:

    def NthM(self, M):
        res=[True]*100
        i=-1
        cnt=0
        m=100
        while m>M:
            i=(i+1)%100 #构成循环缩减
            if res[i]==False:
                continue
            cnt+=1   #通过该参数跳过出圈的人
            if cnt%3==0:
                res[i]=False
                m-=1
        for i in range(100):
            if res[i]==True:
                print(i+1)

while True:
    M=int(input())
    res=Solution().NthM(M)
    print(res)