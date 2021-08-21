

class Solution:
    def interpret(self,command:str)->str:
        return command.replace("()","o").replace("(al)","al")

def stringToString(input):
    return input[1:-1].encode('utf-8').decode('unicode_escape')

def main():
    import io
    import sys
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer,encoding='utf-8'): #类似于C++中的using namespace std;输入std::cin
            yield line.strip('\n') #当遇到换行终止本次输入

    lines=readlines()
    while True:
        try:
            line=next(lines)
            command=stringToString(line)

            ret =Solution().interpret(command)

            out=(ret)
            print(out)
        except StopIteration: #停止迭代时跳出
            break

if __name__ == '__main__':
    main()