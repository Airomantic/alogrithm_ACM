import json
from typing import List
from sortedcontainers import SortedList
"""[8,2,4,7]"""
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        s = SortedList() #初始化为空 有序list
        n = len(nums)
        left = right = ret = 0

        while right < n:
            s.add(nums[right]) #每次新加的元素都必须按从小到大排序，即s[-1]总是最大的，并保证s[-1] - s[0]总是正数
            print("s[-1]=",s[-1],"s[0]=",s[0])
            while s[-1] - s[0] > limit: #s[-1]对于每一轮是新加入的元素，其目的就是为了找出不超过limit的最大值和最小值的元素
                s.remove(nums[left]) #nums[left]=nums[0]移除的是8，按值删除，目的是找出左边最小的
                left += 1 #比较出最小值s[0]=2，之后的循环left就不变了，再循环比较其后的数字与它s[0]两两之差都是小于limit的
            ret = max(ret, right - left + 1) #长度比较，因为left和right都是从0开始的，所以还得加1
            right += 1
        return ret

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
            line = next(lines)
            limit = int(line);

            ret = Solution().longestSubarray(nums, limit)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()