

"""
control+r 运行快捷键
动态规划算法 ：https://blog.csdn.net/sun897949163/article/details/49559679
状态转移方程 dp[][]
可以举个例：
        cbabz
        01234
        i=1,j=3,则直径就是r(bab)=j-i+1=3
"""
class Solution:

    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        if n<2:
            return s
        maxDiameter=0
        begin=0
        """初始化"""
        dp=[[False]*n]*n
        for i in range(n):
            dp[i][i]=True #初始化假设最大回文子串

        for diameter in range(2,n+1):
            for i in range(n):
                j=diameter+i-1

                if j>=n: #注意j最大值是n-1
                    break
                """关键操作，判断回文子串区域"""
                if s[i]!=s[j]:
                    dp[i][j]=False
                else: #关键点：if和else构成一个循环判断回文子串并记录的目的
                    if j-i<3:
                        dp[i][j]=True
                    else:
                        dp[i][j]=dp[i+1][j-1] #状态转移方程，循环缩进，以求得最大回文子串的左右边界
                """计算直径diameter"""
                if dp[i][j] and j-i+1>maxDiameter:
                    maxDiameter=j-i+1
                    begin=i

        return s[begin:begin+maxDiameter]


def stringToString(input):
    # return input[1:-1].encode('utf-8').decode('utf-8') #电脑上的.decode('string_escape')行不通
    return input.encode('utf-8').decode('utf-8')

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
            s = stringToString(line);

            ret = Solution().longestPalindrome(s)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()