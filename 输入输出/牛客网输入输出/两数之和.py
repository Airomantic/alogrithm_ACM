import sys

while True:
    try:
        #方法一
        num=list(map(int,input().split(" ")))
        print(sum(num))
        #方法二
        num=sys.stdin.readline().strip().strip(" ") #注意readline没有s
        a=int(num[0])
        b=int(num[1])
    except:
        break