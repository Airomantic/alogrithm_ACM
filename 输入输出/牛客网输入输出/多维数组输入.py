n=list(map(int,input().split(" "))) #如果直接input()，之后就无法输入新的数据了
col,row=n[0],n[1]
num=[[]*col]*row
print(num)
for i in range(row):
    num[i] = list(map(int, input().split(" ")))
print(num)
#输出的多维数组
# print(res)
# res=str(res).strip("[]").split(',') 取出纯数字（纯字符）
# print(' '.join(res))