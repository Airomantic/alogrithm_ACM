


"""
control+r 运行快捷键
中心扩展算法
"""
class Solution:


    def longestPalindrome(self, s: str) -> str:
        start,end=0,0
        for i in range(len(s)):
            left1,right1=self.expandAroundCenter(s,i,i)
            left2, right2 = self.expandAroundCenter(s, i, i+1)
            if right1-left1>end-start: #注意要到for循环里面
                start,end=left1,right1
            if right2-left2>end-start:
                start,end=left2,right2
        return s[start:end+1] #注意+1

    def expandAroundCenter(self, s, left, right):
        while left>=0 and right<len(s) and s[left]==s[right]:#中心扩展必须用while
            left-=1
            right+=1
        return left+1,right-1


def stringToString(input):
    return input[1:-1].encode('utf-8').decode('utf-8') #电脑上的.decode('string_escape')行不通

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