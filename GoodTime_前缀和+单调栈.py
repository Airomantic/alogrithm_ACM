import json
from typing import List
"""
hours = [9,9,6,0,6,6,9]
score = [1, 1, -1, -1, -1, -1, 1]
presum = [0, 1, 2, 1, 0, -1, -2, -1] #前缀和
前缀和一开始设置为0作为第一个元素presum[0]=0，
presum[1]=presum[0]+score[0]=0+1=1
presum[2]=presum[1]+score[1]=1+1=2
presum[3]=presum[2]+score[2]=2-1=1
presum[4]=presum[3]+score[3]=1-1=0
presum[5]=presum[4]+score[4]=0-4=-1
presum[6]=presum[5]+score[5]=-1-1=-2
presum[7]=presum[6]+score[6]=-2+1=-1
"""
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        # 大于8小时计1分 小于等于8小时计-1分
        score = [0] * n #初始化[0, 0, 0, 0, 0, 0, 0]
        for i in range(n):
            if hours[i] > 8:
                score[i] = 1
            else:
                score[i] = -1
        # 前缀和
        presum = [0] * (n + 1) #初始化比hours数组多一位元素的0数组
        for i in range(1, n + 1): #从第2为开始计算presum与score的关系
            presum[i] = presum[i - 1] + score[i - 1]

        ans = 0
        stack = []

        # 顺序生成单调栈，栈中元素从第一个元素开始严格单调递减，最后一个元素肯定是数组中的最小元素所在位置
        #presum[stack[-1]] 单调递减
        for i in range(n + 1):
            if not stack or presum[stack[-1]] > presum[i]:
                stack.append(i) #是把下标压进去，presum[stack[-1]]只有第二次循环后才有意义，第一次循环压入数据到stack

        # 倒序扫描数组，求最大长度坡
        i = n
        while i > ans: #从后往前自然i>stack[-1]栈顶元素
            while stack and presum[stack[-1]] < presum[i]: #关键点1：满足presum倒序扫描大于栈中下标得来的presum[]条件的 进入比较处理
                # print("压入了元素就有栈时：stack[-1]=", stack[-1], "presum[stack[-1]]=", presum[stack[-1]],"presum[",i,"]=",presum[i])

                ans = max(ans, i - stack[-1]) #关键点2：求最大差值为"表现良好的最长时间段"
                stack.pop() #数组也有pop()，弹出数组尾部元素相当于弹出栈顶元素

            i -= 1
        return ans #举例中是 3-0=3刚好满足"表现良好的最长时间段"

def stringToIntegerList(input):
    return json.loads(input)


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            hours = stringToIntegerList(line)
            ret = Solution().longestWPI(hours)

            out = str(ret)
            print("长度为：",out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()