from typing import List
import json
"""
示例1
输入：[6,0,8,2,1,5]
输出：4
解释：
最大宽度的坡为 (i, j) = (1, 5): A[1] = 0 且 A[5] = 5.###5-1=4
示例2
输入：[9,8,1,0,1,9,4,0,4,1]
输出：7
解释：
最大宽度的坡为 (i, j) = (2, 9): A[2] = 1 且 A[9] = 1.###9-2=7
"""
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        ans = 0
        m = float('inf') #inf字符对应一个很大的正数值，目的是为了作为中间值min(m, i)找到最前面的下标（最小的下标）
        for i in sorted(range(len(nums)), key=nums.__getitem__):
            #nums={0:6,1:0,2:8,3:2,4:1,5:5}对其按Value排小大按Key组序为：{0:1,1:4,2:3,5:5,6:0,8:2} 再输出下标即1 4 3 5 0 2
            print("i=",i,"m=",m,"i-m=",i-m) #注意这里的i是按1 4 3 5 0 2
            ans = max(ans, i - m)
            print("ans=",ans)
            m = min(m, i)
            print("m=",m)
        return ans

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
            nums = stringToIntegerList(line);

            ret = Solution().maxWidthRamp(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()