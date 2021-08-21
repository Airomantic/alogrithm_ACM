# import sys  # 导入sys模块
# sys.setrecursionlimit(3000)  # 将默认的递归深度修改为3000

class Solution:
    def compressString(self, S: str) -> str:
        if not S:
            return ''

        ans=''
        count=0
        isChar=S[0]
        for c in S:
            if c==isChar:
                count+=1
            else:
                ans+=isChar+str(count)
                isChar=c
                count=1 #新检测到的字母从1开始

        """整合"""
        ans+=isChar+str(count) #保证之后有和前面一样的数字也能加入，而for c in S的形式无法判断间断重复的数字
        return ans if len(S)>len(ans) else S


def stringToString(input):
    return input[1:-1].encode('utf-8').decode('utf-8')


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
            S = stringToString(line);

            ret = Solution().compressString(S)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()