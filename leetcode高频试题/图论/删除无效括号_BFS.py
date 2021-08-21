import io
import sys
"""
https://leetcode-cn.com/problems/remove-invalid-parentheses/solution/bfsjian-dan-er-you-xiang-xi-de-pythonjiang-jie-by-/

()())()
"""

class Solution:
    def removeInvalidParentheses(self, s):
        def isValid(s)->bool:
            count=0
            for c in s:
                if c=="(":
                    count+=1
                elif c==")":
                    count-=1

                if count<0:
                    return False ## 只用中途cnt出现了负值，你就要终止循环，已经出现非法字符了
            return count==0  #count==0相当于True
        """BFS"""
        level={s}
        while True: #filter 满足count==0可传递给valid，即是 (和)的对称
            valid=list(filter(isValid,level)) # 所有合法字符都筛选出来,isValid=True才能筛出当前level
            if valid:return valid   # 关键点1: 如果当前valid是非空的，说明已经有合法的产生了，答案就是valid
            """关键点2：用于valid list中元素不重复 ##无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集"""
            next_level=set()   #新add的元素放在{}中的顺序不用顾及，set导致(总是在左边
            for item in level:
                for i in range(len(item)): #BFS 典型方法，在相邻的图结点先蔓延
                    if item[i] in "()": # 如果item[i]这个char是个括号就删了，如果不是括号就留着

                        next_level.add(item[:i]+item[i+1:]) #就是跳过item[i]这个字符的意思，以最原始的构造进行删除
            level=next_level #循环，继续检测刚刚跳过的无效括号后是否满足有效



def main():
    def readlines():
        for lines in io.TextIOWrapper(sys.stdin.buffer,encoding='utf-8'):
            yield lines.strip('\n')
    lines=readlines()
    while True:
        try:
            line=next(lines)
            s=str(line)
            res=Solution().removeInvalidParentheses(s)
            print(res)
        except StopIteration:
            break


if __name__ == '__main__':
    main()