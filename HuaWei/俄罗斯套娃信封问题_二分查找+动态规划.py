"""
https://leetcode-cn.com/problems/russian-doll-envelopes/solution/e-luo-si-tao-wa-xin-feng-wen-ti-by-leetc-wj68/
时间复杂度：O(nlogn)
空间复杂度：O(n)
输入： 行 列
4 2
5 4
6 4
6 7
2 3

bisect用法：
https://www.cnblogs.com/beiluowuzheng/p/8452671.html
bisect_left和bisect_right  bisect_left函数是新元素会被放置于它相等的元素的前面，而 bisect_right返回的则是跟它相等的元素之后的位置。
https://blog.csdn.net/andybegin/article/details/84765049
key=lambda
https://blog.csdn.net/jidushanzhu/article/details/81476548
"""
import bisect
from typing import List


class Solution:

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0

        n = len(envelopes)
        # -x[1]有个负号同时保证在x[0]递增出现相同时，第二位大的放在前面，左边优先级大于右边
        envelopes.sort(key=lambda x: (x[0], -x[1])) #[[2,3],[5,4],[6,7],[6,4]]

        f = [envelopes[0][1]]  #f:[3]
        print('初始化f=',f)
        for i in range(1,n):
            #这个num:=很巧妙，当不满足if时赋给bisect_left之前满足的元素，比如[6,7],[6,4]时7>4
            if (num:=envelopes[i][1])>f[-1]: #注意envelopes[i][1]从1开始即envelopes元素4开始 f[-1] 当前末尾的元素值
                f.append(num)
            #else目的：为了最多套娃，覆盖比较
            else:
                #比较
                index=bisect.bisect_left(f,num) # 返回相同元素左边的索引，f[index]=num进行f新元素覆盖
                print('index=',index)
                f[index]=num
            print('num=', num)
            print(f) #f:[3,4,7]
        return len(f) #二分查找返回长度，动态规划返回状态转移方程记录的最大值

while True:
    try:
        num=list(map(int,input().split(" ")))
        row,col=num[0],num[1]
        envelopes=[[]*col]*row
        for i in range(row):
            envelopes[i]=list(map(int,input().split(" ")))
        print(envelopes)
        res=Solution().maxEnvelopes(envelopes)
        print(res)
    except:
        break