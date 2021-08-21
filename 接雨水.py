import io
import json
import sys
from typing import List

def stringToIntegerList(line):
    return json.loads(line)

class Solution:
    def waterContainer(self,height:List[int]):
        n=len(height) - 1
        left,right=0,n
        ans=0
        leftMax,rightMax=height[0],height[n]
        while left<right:
            leftMax = max(leftMax, height[left])
            rightMax=max(rightMax,height[right])
            if height[left]>height[right]: #关键点
                ans+=rightMax-height[right]
                right-=1
            else:
                ans+=leftMax-height[left]
                left+=1

        return ans

def EnterMain():
    def readlines():
        for lines in io.TextIOWrapper(sys.stdin.buffer,encoding='utf-8'):
            yield lines.strip('\n')

    lines=readlines()
    while True:
        try:
            line=next(lines)
            hList=stringToIntegerList(line)
            result=Solution().waterContainer(hList)
            out=str(result)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    EnterMain()