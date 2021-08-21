import json


def stringToInetegerList(input):
    return json.loads(input) ##一维和二维都可以，遇到[]就会自动生成list



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
            a=stringToInetegerList(line)

            ret=Solution().abSum(a)
            out=(ret)
            print(out)
        except StopIteration: #停止迭代时跳出
            break

if __name__ == '__main__':
    main()