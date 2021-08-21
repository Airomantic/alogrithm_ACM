import io
import sys
"""
1234567891011121314151617181920212223.....
n>9位数：
第count=1行：10111213...979899 共10**1*9*2=90*2=180位数   每个数的位数count+1=2
第count=2行：100101102103...997998999 共10**2*9*3=900*3=2700位数 每个数的位数count+1=3
第count=3行：1000 1001 1002 ... 9997 9998 9999 共10***3*9*4=36000位数 每个数的位数count+1=3
"""
class Solution:
    def findNthDigit(self,n):
        if n<10:
            return n

        n-=9
        count=1
        while True:
            num=10**count*9*(count+1)
            if n>num:
                n-=num
                count += 1
            else:
                i,j=divmod(n,count+1)
                if not j:
                    return int(str(10**count+i-1)[-1]) #i有时会是两位数，所以不能直接返回int(str(i-1))
                else:
                    return int(str(10**count+i)[j-1])

def EnterMain():
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer,encoding='utf-8'):
            yield line.strip('\n')
            
    lines=readlines()
    while True:
        try:
            line=next(lines)
            n=int(line)
            res=Solution().findNthDigit(n)
            print(res)
        except StopIteration:
            break


if __name__ == '__main__':
    EnterMain()