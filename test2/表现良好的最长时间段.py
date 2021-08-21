import json


def stringToIntegerList(input):
    return json.loads(input)


class Solution:
    def longestWPI(self, hours):
        n=len(hours)

        if not hours: #注意这里不是n
            return 0
        score=[0]*n
        for i in range(n):
            if hours[i]>8:
                score[i] =1
            else:
                score[i]=-1
        preSum=[0]*(n+1)

        for i in range(1,n+1): #注意这里从1开始
            preSum[i]=preSum[i-1]+score[i-1]
        ans=0
        stack=[]
        for i in range(n): #注意这里用for，因为while的i没有初始化0
            """注意这里用or"""
            if not stack or preSum[stack[-1]]>preSum[i]: #单调递增的stack
                stack.append(i)
        i=n
        while i>0:
            while stack and preSum[stack[-1]] < preSum[i]: #注意这里用while，不是if not
                ans=max(ans,i-stack[-1])
                stack.pop()
            i-=1
        return ans

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