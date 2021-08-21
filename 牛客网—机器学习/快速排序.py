import io
import json
import sys


def stringToIntergeList(input):
    return json.loads(input)

class Solution:

    def quicksort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.quicksort(left) + middle +self.quicksort(right)

def EnterMain():
    def readlines():
        for lines in io.TextIOWrapper(sys.stdin.buffer,encoding='utf-8'):
            yield lines.strip('\n')

    lines=readlines()
    while True:
        try:
            # line=next(lines)
            # arr=stringToIntergeList(line)
            arr=list(map(int,input().strip().split()))
            result=Solution().quicksort(arr)
            result=str(result).strip("[]").split(",")
            print(''.join(result))
        except StopIteration:
            break

if __name__ == '__main__':
    EnterMain()