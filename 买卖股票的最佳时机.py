import io
import json
import sys
"""
[7,2,8,1,3,4]      #看出2-8，1-4的区别就知道min_price和prices[i]原理了，
这里的min_price就是指的是prices[i]第i+1个数（如8）前面中最小的值
"""

def stringToIntegerList(input):
    return json.loads(input)


class Solution:
    def maxProfit(self, prices):
        n=len(prices)
        min_price,max_price=prices[0],0    #min_price初始值设置成无穷大也行，但注意一定不能设置成0
        if len(prices)<=1:
            return 0

        for i in range(n):
            max_price=max(max_price,prices[i]-min_price) #求出第i+1个数前面所有数与前面最小值差最大值
            min_price=min(min_price,prices[i])

        return max_price


def main():
    def readlines():
        for lines in io.TextIOWrapper(sys.stdin.buffer,encoding='utf-8'):
            yield lines.strip('\n')

    line=readlines()
    while True:
        try:
            lines=next(line)
            prices=stringToIntegerList(lines)
            result=Solution().maxProfit(prices)
            print(result)
        except StopIteration:
            break

if __name__ == '__main__':
    main()