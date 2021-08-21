import json
from typing import List

class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        def func(number, res, index):
            if len(res) >= 3 and index == len(number):
                return True
            #print("len(number)=",len(number))
            for i in range(index, len(number)):
                print("index=",index,"i=",i)
                if number[index] == '0' and i > index:
                    break
                num = subDight(number, index, i + 1) #通过index和i将一串数字进行分块
                if num > 2 ** 31 - 1:
                    break
                size = len(res)
                if size >= 2 and num > (res[size-1] + res[size-2]):
                    break
                if size <= 1 or num == res[size-1] + res[size-2]:
                    res.append(num)
                    if func(number, res, i + 1):
                        #print("number=",number,"res=",res,"i+1=",i+1) #res存储分块后的数字，i+1记录分块长度
                        return True
                    res.pop(-1)
            return False  #不进入for i in range(index, len(number))

        def subDight(digital, start, end):
            num= 0
            for i in range(start,end):

                num = num*10 + int(digital[i]) #dight[i]逐个获取单个数字
                print("digital[i]=", digital[i])
            return num

        l1 = list()
        func(num,l1,0)
        return l1


def stringToString(input):
    return input[1:-1].encode('utf-8').decode('utf-8') #这里去除首位的双引号

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])

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
            num = stringToString(line)

            ret = Solution().splitIntoFibonacci(num)

            out = integerListToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()