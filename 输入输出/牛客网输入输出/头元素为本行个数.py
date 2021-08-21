

while True:
    try:

        num=list(map(int,input().split(" ")))
        if num[0]==0:
            break
        print(sum(num[1:]))
    except:
        break
