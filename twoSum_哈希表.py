import io
import json
import sys


def stringToList(line):
    return json.loads(line)


class Solution:
    def twoSum(self,nums:list[int],target):
        temp_dict={}
        for k,v in enumerate(nums):
            temp_dict[v]=k
            if target-v in temp_dict:
                return [temp_dict[target-v],k]

def integerToList(result,leng_of_list=None):
    if not leng_of_list:
        return json.dumps(result[:leng_of_list]) #注意dumps有s

def EnterMain():
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer,encoding='utf-8'):
            yield line.strip('\n')
            
    lines=readlines()
    while True:
        try:
            line=next(lines)
            LN=stringToList(line)
            line=next(lines)
            target=int(line)
            result=Solution().twoSum(LN,target)
            indexList=integerToList(result)
            print(indexList)
        except StopIteration:
            break

if __name__ == '__main__':
    EnterMain()