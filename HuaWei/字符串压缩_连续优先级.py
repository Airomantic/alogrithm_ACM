import io
import sys


class Solution:

    def calString(self, line):
        # lineList=list(line)
        # print(lineList,type(lineList))
        count=0
        ans=''

        #i作为中枢，AB|C|ABCABC，i就指着｜c｜
        for i in range(len(line)):
            for j in range(i):
                continue_char=line[j:i]
                left=i + 1
                right=i-j+left
                for c in line[left:]:
                    count=1
                    if c==continue_char and continue_char==line[left:right]:
                        count+=1
                else:
                    ans+=continue_char+str(count)
                    count=1
                ans+=continue_char+str(count)
        return ans



def EnterMain():
    def readlines():
        for lines in io.TextIOWrapper(sys.stdin.buffer,encoding='utf-8'):
            yield lines.strip('\n')
    lines=readlines()
    while True:
        try:
            line=next(lines)
            res=Solution().calString(line)
            print(res)
        except:
            break

if __name__ == '__main__':
    EnterMain()
