"""
https://blog.csdn.net/m0_37324740/article/details/78830136
"""
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class Solution:
    def reverse(self, x: int) -> int:
        # stack=Stack()
        INT_MIN,INT_MAX=-2**31,2**31-1   #32位即：2**(32-1)
        rev =0

        while x!=0: #判断的终止条件是等于0
            if rev < INT_MIN // 10 + 1 or rev > INT_MAX // 10:  # 反转后整数超过 32 位
                return 0
            digit=x%10 #x为负数，直接余除的余数是正数，需要取模转化到 (-9,0]
            if x<0 and digit>0:
                digit-=10
            x=(x-digit)//10
            rev=rev*10+digit
        return rev

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
            x = int(line);

            ret = Solution().reverse(x)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()