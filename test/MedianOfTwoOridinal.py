import json
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:  # 保证左边参数list小于右边参数
            return self.findMedianSortedArrays(nums2, nums1)
        k = (n1 + n2 + 1) // 2  # 取商整
        print("整合两个list的中位数k=", k)
        left = 0
        right = n1
        print("right=", right)
        while left < right:  # 直到left>=right跳出
            m1 = left + (right - left) // 2  # 总会取到（奇）中位数（偶数中位线）的左边一位
            print("1.m1=", m1)
            m2 = k - m1
            print("1.m2=k - m1=", m2)
            print("nums1[m1]=", nums1[m1], "nums2[m2 - 1]=", nums2[m2 - 1])  # 总会取到中位数
            if nums1[m1] < nums2[m2 - 1]:
                left = m1 + 1
                print("left=", left)
            else:
                right = m1
                print("right=", right)
        m1 = left
        print("2.m1=", m1)
        m2 = k - m1
        c1 = max(nums1[m1 - 1] if m1 > 0 else float("-inf"), nums2[m2 - 1] if m2 > 0 else float("-inf"))  # 三目运算符
        if (n1 + n2) % 2 == 1:
            print("奇数c1=", c1)
            return c1
        c2 = min(nums1[m1] if m1 < n1 else float("inf"), nums2[m2] if m2 < n2 else float("inf"))
        print("偶数(c1 + c2) / 2=", (c1 + c2) / 2)
        # 关键点：c1,c2分别为两个list的中位数
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