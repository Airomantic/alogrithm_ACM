


class Solution:

    def generateParenthesis(self, n):
        ans=[]

        def backtrace(S, left, right):
            if len(S)==2*n:
                #当递归时满足该条件的S压入ans后会由return空走到right的S.pop()弹出s[-1],s[-2],s[-3],再到left弹出s[-4],即后面的4个[((()))]=>[((]
                ans.append(''.join(S)) #ans list接入S list
                return #满足2n长度即可跳出，输出ans
            if left<n: #第一步处理
                S.append('(')
                backtrace(S,left+1,right)
                S.pop() #用于回溯弹出之前压入的，来建立新的方案
            if right<left:  #关键点 回溯有新的方案重要步骤
                S.append(')')
                backtrace(S,left,right+1)
                S.pop()

        backtrace([],0,0)
        return ans

while True:
    try:
        n=int(input())
        res=Solution().generateParenthesis(n)
        print(res)
        print(' '.join(res))
    except:
        break