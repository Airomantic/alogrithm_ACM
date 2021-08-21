import json
from typing import List
"""

"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2: #保证参数n1总是小于n2
            return self.findMedianSortedArrays(nums2, nums1)
        k = (n1 + n2 + 1) // 2
        left = 0
        right = n1
        while left < right:
            m1 = left + (right - left) // 2 #关键点1：起到循环直到要删除折半的前一半部位
            m2 = k - m1 #折半剩余部位
            if nums1[m1] < nums2[m2 - 1]: #关键点2：第k数最小
                left = m1 + 1 #
            else:
                right = m1
        m1 = left
        m2 = k - m1
        c1 = max(nums1[m1 - 1] if m1 > 0 else float("-inf"), nums2[m2 - 1] if m2 > 0 else float("-inf"))
        if (n1 + n2) % 2 == 1:
            return c1
        c2 = min(nums1[m1] if m1 < n1 else float("inf"), nums2[m2] if m2 < n2 else float("inf"))
        return (c1 + c2) / 2


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
            nums1 = stringToIntegerList(line);
            line = next(lines)
            nums2 = stringToIntegerList(line);

            ret = Solution().findMedianSortedArrays(nums1, nums2)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()