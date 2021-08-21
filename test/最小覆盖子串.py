import collections
import io
import sys

def stringToString(input):
    return input[1:-1].encode('utf-8').decode('utf-8')

class Solution:

    def MinOverridSubstring(self, s, t):
        need=collections.defaultdict(int)
        for c_t in t:
            need[c_t]+=1
        needCnt=len(t)
        i=0
        res=(0,float('inf'))
        for j,s_all in enumerate(s):
            if need[s_all]>0:
                needCnt-=1
            need[s_all]-=1
            if needCnt==0:
                """左边界"""
                while True:
                    s_windows=s[i]
                    if need[s_windows]==0:
                        break

                    need[s_windows]+=1 #注意s_windows
                    i+=1

                if j-i <res[1]-res[0]:
                    res=(i,j)

                need[s[i]]+=1 #注意是s[i]
                needCnt+=1 #记得加
                i+=1
        return '' if res[1]>len(s) else s[res[0]:res[1]+1]




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