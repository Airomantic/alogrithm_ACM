"""
https://leetcode-cn.com/problems/russian-doll-envelopes/solution/e-luo-si-tao-wa-xin-feng-wen-ti-by-leetc-wj68/
跟 最长递增子序列 一样
输入： 列 行
2 4
5 4
6 4
6 7
2 3
"""

class Solution:
    def maxEnvelopes(self, envelopes):

        if not envelopes:
            return 0
        n = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        print(envelopes)
        f = [1] * n #f相当于dp 状态转移方程
        for i in range(n):
            for j in range(i):
                if envelopes[j][1] < envelopes[i][1]: # 比较高
                    f[i] = max(f[i], f[j] + 1) #每次遇到递增数字状态转移方程就加1

        return max(f)

while True:
    try:
        n=list(map(int,input().split(" ")))
        col,row=n[0],n[1] #列 行
        envelopes=[[]*col]*row
        # print(envelopes)
        for i_row in range(row):
            envelopes[i_row]=list(map(int,input().split(" ")))
        res=Solution().maxEnvelopes(envelopes)
        print(res)
    except:
        break