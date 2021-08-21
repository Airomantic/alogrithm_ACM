import io
import sys

#
# class Solution:
#
#     def calString(self, line):
#         lineList=list(line)
#         # print(lineList,type(lineList))
#         newStr=''
#         count=0
#         for i in range(len(lineList)):
#             if lineList[i]!=lineList[i+1]:
#                 if count>0:
#                     newStr+=count
#                     count=0
#                 newStr+=lineList[i]
#             else:
#                 count+=1
#         if count!=0:
#             newStr+=count
#         newStr+=lineList[len(line)-1]
#         print(newStr)
#
# def EnterMain():
#     def readlines():
#         for lines in io.TextIOWrapper(sys.stdin.buffer,encoding='utf-8'):
#             yield lines.strip('\n')
#     lines=readlines()
#     while True:
#         try:
#             line=next(lines)
#             res=Solution().calString(line)
#             print(res)
#         except:
#             break
#
#
# if __name__ == '__main__':
#     EnterMain()
# 定义解码函数
def decode(s):
    i = 0
    x, y, z = -1, -1, -1
    # 遍历字符串s
    while i < len(s):
        # 记录'['的索引位置
        if s[i] == '[':
            x = i
        # 记录'|'的索引位置
        elif s[i] == '|':
            y = i
        # 记录']'的索引位置
        elif s[i] == ']':
            z = i            # 扫描到']'字符时，跳出循环
            break
        i += 1
        # 处理重复的字符串
        if x != -1 and y != -1 and z != -1:
            # 从字符串s获取重复次数
            times = int(s[x + 1:y])
            # 从字符串s获取重复子串
            sub = s[y + 1:z]
            # 计算需要再次递归处理的字符串
            decode_str = s[:x] + times * sub + s[z + 1:]
            # 递归处理字符串
            return decode(decode_str)
    # 若没有重复的字符串，返回s
    return s
if __name__=='__main__':
    s="HG[3|B[2|CA]]F"
    print(decode(s), end='')