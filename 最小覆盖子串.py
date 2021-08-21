import collections
import io
import sys

"""
"ADOBECODEBANC"
"ABC"
输出
"BANC"
"""
def stringToString(input):
    return input[1:-1].encode('utf-8').decode('utf-8')

class Solution:

    def MinOverridSubstring(self, s, t):
        need=collections.defaultdict(int) #字典
        for c_t in t:
            need[c_t]+=1 #一个元素value赋予一个key作为频数 {'A': 1, 'B': 1, 'C': 1} 注意⚠️都是1
        needCnt=len(t) #额外变量，用于代替每次访问need字典的时间损耗
        i=0
        res=(0,float('inf')) #res[0]=0，res[1] =inf
        for j,c_all in enumerate(s):
            if need[c_all]>0: #如果s中有t中的元素
                needCnt-=1
            need[c_all]-=1 #同时需要的对应元素频数降为0
            if needCnt==0: #当减到为0时，滑动窗口包含了所有T元素
                while True: #增加左边界i，排除多余元素
                    c_windows=s[i]
                    if need[c_windows]==0: #如果新增到元素不是t需要的元素，也就是在这里面找的频数为0
                        break
                    need[c_windows]+=1 #
                    i+=1
                if j - i < res[1] - res[0]:  # 记录结果长度
                    res = (i, j)
                need[s[i]] += 1  # 步骤三：i增加一个位置，寻找新的满足条件滑动窗口
                needCnt += 1
                i += 1
        return '' if res[1] > len(s) else s[res[0]:res[1] + 1]  # 如果res始终没被更新过，代表无满足条件的结果





def EnterMain():
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer,encoding='utf-8'):
            yield line.strip('\n')

    lines=readlines()
    while True:
        try:
            line=next(lines)
            origin_S=stringToString(line)
            line = next(lines)
            T=stringToString(line)
            result=Solution().MinOverridSubstring(origin_S,T)
            print(str(result))
        except StopIteration:
            break


if __name__ == '__main__':
    EnterMain()