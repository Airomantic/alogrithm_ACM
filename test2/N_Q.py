class Solution:
    def __init__(self):
        self.res = []
    def isvalidqueen(self, trace, row, column):

        nLen=len(trace)
        #列
        for item in trace:
            if item[column]=='Q':
                return False
        #上右
        for i,j in zip(range(row-1,-1,-1),range(column+1,nLen)):
            if trace[i][j]=='Q':
                return False
        #上左
        for i,j in zip(range(row-1,-1,-1),range(column-1,-1,-1)):
            if trace[i][j]=='Q':
                return False
        return True
    def replaceChar(self, trace, idx, char):
        strList=list(trace)
        strList[idx]=char
        s=''.join(strList)
        return s
    def backtrace(self, trace, row):

        if (len(trace)==row):
            ret=list(trace)
            self.res.append(ret)
            return    #注意这里什么都不要返回，否则迭代不完
        for column in range(len(trace)):
            #判断
            if(not self.isvalidqueen(trace, row, column)):
                continue
            trace[row]=self.replaceChar(trace[row],column,'Q') #注意这里传入的是trace[row],column
            self.backtrace(trace,row+1)
            trace[row] = self.replaceChar(trace[row], column, '.')


    def solveNQueens(self, n):
        s='. '*n
        trace=[s]*n
        self.backtrace(trace,0)
        return self.res

if __name__ == '__main__':
    n=int(input("please input n="))  # 直接  入的内容会当作字符串形式，需int强转
    result=Solution().solveNQueens(n)  # 注意  用类时要加上()
    for i in range(0,len(result[0])):
        print(result[i])