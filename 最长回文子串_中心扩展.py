

"""
control+r 运行快捷键
中心扩展算法
"""
class Solution:
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]: #关键点：s[left] == s[right] 回文数相同字符元素
            left -= 1  #中心扩展
            right += 1 #中心扩展
        return left + 1, right - 1 #缩回

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            """目的是得到半径"""
            left1, right1 = self.expandAroundCenter(s, i, i) #奇数子回文串 P(i,i)=true 边界条件
            left2, right2 = self.expandAroundCenter(s, i, i + 1) #偶数子回文串  P(i,i+1) 边界条件
            print("left1, right1 =",left1, right1 )
            print("left2, right2 =",left2, right2 )
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start: #如果两个if同时成立，第二个if会覆盖第一if的结果start-end 是直径
                start, end = left2, right2
        return s[start: end + 1]

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