import json
from typing import List
"""
eval()函数
"""
def stringToStrList(input): #输入进来的input虽然有[]但不是list所以处理取值之后inputValues需加上[]
    input=input.strip()

    input=input[1:-1] #去掉首位中括号
    print(input)
    if not input:
        return None
    inputValues=[s.strip() for s in input.split(',')] #去除逗号,但有加入到[]会自动生成新的逗号，逗号后多一个空格，每一个元素会带上单引号
    return inputValues

class Solution:

    def evalRPN(self, tokens: List[str]):
        f1 = lambda a, b: a + b #相当于一个匿名函数get(a,b): return a + b
        f2 = lambda a, b: a - b
        f3 = lambda a, b: a * b
        f4 = lambda a, b: int(a / b)
        maps = {'+': f1, '-': f2, '*': f3, '/': f4}

        stack = [] #或定义成list()
        for i in tokens:

            if i in maps: #当遇到符号时
                a = stack.pop() #这个弹出的顺序不能弄错，a先弹出，在进行减法和除法时，应b-a或b-a
                b = stack.pop()
                stack.append(maps[i](b, a)) #maps[i](b, a) 就是b+a 或b-a 或 b*a 或 b-a 符号根据i选择
            else: #不是符号时，把数值给提取出来，这样stack里面就都是数值
                i = int(i)
                stack.append(i)

        return stack[-1] #弹出计算好的元素刚好是栈顶元素

    def solve(self, s):
        _=0
        brackets=[]
        for _ in range(len(s)-1):
            if s[_]!='(':

                value = self.evalRPN(s)
            else:
                brackets.append(s[_])


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
            hours = stringToStrList(line)
            print(hours)
            ret = Solution().evalRPN(hours)
            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
