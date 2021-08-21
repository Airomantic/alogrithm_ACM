def judge(a):
    sum, page = 0, 0
    for i in range(len(a)):
        sum+=a[i]
        # print("sum=",sum)
        if sum<60:
            page += 1
        else:
            sum %= 60  # 剩余的时间继续计算
            page = 0

    if page>4:
        return 0
    else:
        return 1

t=int(input())
while t>0:
    a=[]
    n=list(map(int,input().split(" ")))
    a=n[1:]
    print(a)
    print(judge(a))
    a.clear()
    t-=1
