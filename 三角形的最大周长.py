

import json
from typing import List


def stringToIntegerList(input):
    return json.loads(input)


class Solution:
    def triangleLargestPerimeter(self, nums: List[int]):
        newSort=sorted(nums,reverse=True) #从大到小
        for i in range(len(nums) - 2): #你懂的
            if newSort[i+2]+newSort[i+1]>newSort[i]: #两个小的之和大于大的
                return newSort[i]+newSort[i+1]+newSort[i+2]
        return 0

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
            nums = stringToIntegerList(line)

            ret = Solution().triangleLargestPerimeter(nums)
            out = str(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()