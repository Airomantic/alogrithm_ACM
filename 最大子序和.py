
import json
from typing import List

"""
1.连续数组，考虑前缀和
2.由于当前最大值，只与前一位置的和相关，于是维护变量 min_preSum即可
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ln = len(nums)
        presum, min_presum = 0, 0
        res = nums[0]
        for i in range(ln):
            presum += nums[i]
            res = max(presum - min_presum, res) #关键点1：相当于求单调递增
            min_presum = min(presum, min_presum) #关键点2：保留前一位置的和，避免当前位置出现下降（下降的话，就选择前一位置作为连续最大和）
        return res

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
            nums = stringToIntegerList(line)

            ret = Solution().maxSubArray(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()