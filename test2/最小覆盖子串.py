import collections
import io
import sys

def stringToString(input):
    return input[1:-1].encode('utf-8').decode('utf-8')

class Solution:

    def MinOverridSubstring(self, s, t):
        need=collections.defaultdict(int)
        for c_t in t:
            need[c_t]+=1 #频数赋为1
        needCnt=len(t)
        i=0
        res=(0,float('inf')) #用于记录变长的滑动窗口
        for j,s_all in enumerate(s): #这里的s_all不仅有need元素还有其他的
            if need[s_all]>0: #还没开始滑动窗口前先判断是否有频数大于1的
                needCnt-=1 #s_all只要有一个就要在需要needCnt记录器中减1，这里是循环
            need[s_all]-=1 #不是t中元素的记为-1
            if needCnt==0: #记录器刚好满足s的滑动窗口中对应t中元素的数量（一般是频数是1）
                """左边界"""
                while True:
                    s_windows=s[i] #从第一位开始识别
                    if need[s_windows]==0:
                        break
                    need[s_windows]+=1 #否则左边界收缩（向右）时就少了一个t中的元素，即需要的元素多一个
                    i+=1 #同时左边界继续向右收缩
                """窗口长度"""
                if j-i <res[1]-res[0]: #比较出最小长度的窗口
                    res=(i,j)
                """右边界"""
                need[s[i]]+=1
                needCnt+=1 #由右边界控制
                i+=1 #右边界右移
        return ''if res[1]>len(s) else s[res[0]:res[1]+1]



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