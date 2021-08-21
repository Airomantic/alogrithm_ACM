import sys
import json
from typing import List
import io

from sortedcontainers import SortedList
def stringToIntergeList(input):
    return json.loads(input)


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        s = SortedList()
        for i in range(len(nums1)):
            s.add(nums1[i])
        for j in range(len(nums2)):
            s.add(nums2[j])
        n = len(s)
        if n % 2 == 0:
            l=int(n/2)
            p = float((s[l - 1] + s[l]) / 2)
            return p
        else:
            return s[n // 2]


def EnterMain():
    def readlines():
        for lines in io.TextIOWrapper(sys.stdin.buffer,encoding='utf-8'):
            yield lines.strip('\n')

    lines=readlines()
    while True:
        try:
            line=next(lines)
            nums1=stringToIntergeList(line)
            line = next(lines)
            nums2 = stringToIntergeList(line)
            result=Solution().findMedianSortedArrays(nums1,nums2)
            out=str(result)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    EnterMain()