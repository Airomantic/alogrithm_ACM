
from typing import List
"""
if后面的括号可要可不要
参数设置的固定类型可要可不要
"""
class Solution:
    def __init__(self):
        self.res = []  # 用self是为了把二维list返回
    # 新加入的皇后是否符合要求
    def isvalidqueen(self, trace: List[str], row: int, col: int) -> bool:
        nLen = len(trace)
        # 列
        for item in trace: #先一行一行（即一个元素一个元素的检查）注意不是二维数组
            if item[col] == 'Q': #该"列"上的第col+1个字符有没有Q
                return False #有返回False对应not False，没有Q,就跳出该if语句，继续执行下一行放上Q
        # 右上 (row -1,col +1)上右
        for i ,j in zip(range(row -1, -1, -1), range(col +1, nLen)): #zip合并两个list（不是加），把范围弄成k-v一样分别赋给i,j
            #-1表示倒序，右上时需要行到序，从尾往前，row 是从0开始的，col也是从0开始的
            print(i ,j)
            if(trace[i][j] == 'Q'):
                return False
        # 左上 (row -1,col -1)左上
        for i ,j in zip(range(row -1 ,-1 ,-1), range(col -1, -1, -1)): #左上时需要行列都倒序
            if(trace[i][j] == 'Q'):
                return False
        return True #返回后的条件是not True=False 即if语句不执行，跳出，进行下一行代码
    def replacechar(self, string :str, idx :int, char: str )-> str: # trace[row] ,col ,'Q'
        strList = list(string) #字符串变成一维数组
        strList[idx] = char #相当于trace[row][col=idx] = char
        s = ''.join(strList)
        return s
    def backtrace(self, trace: List[str], row: int):
        #print(row ,end="")
        # 停止条件 针对方阵
        if(len(trace) == row): #如果进行完成，就把字符全部放入数组
            ret = list(trace)  # list加入list 形成二维list，实际上还是一维list，只不过元素有n个字符
            self.res.append(ret) #注意这调用self.res
            return
        for col in range(len(trace)): #只针对方块
            if(not self.isvalidqueen(trace, row, col)):  # 判断列 正对角线 副对角线 上是否存在Q，这个continue方法是个关键点
                continue #not false时即True ，有Q满足continue则往上返回到for循环条件col+1，否则跳过col不变进行下一行代码运行放上Q并row+1，没有Q就往下执行
            # 注意下面三行代码要放在for循环里面
            """not True"""
            trace[row] = self.replacechar(trace[row] ,col ,'Q')  # 将当前坐标上的.换成Q
            self.backtrace(trace, row +1)  #这里可不是退回上一步，而是保证row+1 使得新的行查看是否满足放Q
            trace[row] = self.replacechar(trace[row] ,col ,'.')  # 检查上一行，将Q重新换成. 这一步放在backtrace函数后面才真正完整的构成回溯

    def solveNQueens(self, n: int) -> List[List[str]]:
        s = '. ' *n #一个元素构成n个字符
        trace = [s] *n #有[]但目前还不是数组，实际上还是一位数组，只不过每个元素有n个字符
        print("一维的7 × 7结构" ,trace)  # 后续还需要再把里面的'.......'进行[]起来
        self.backtrace(trace, 0)  # 0表示row初始，从第一行开始
        return self.res

if __name__ == '__main__':
    n=int(input("please input n="))  # 直接  入的内容会当作字符串形式，需int强转
    result=Solution().solveNQueens(n)  # 注意  用类时要加上()
    for i in range(0,len(result[0])):
        print(result[i])