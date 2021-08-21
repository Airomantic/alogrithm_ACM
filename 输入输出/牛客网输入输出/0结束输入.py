
while True:
    try:
        num=list(map(int,input().split(" "))) #map是用来绑定输入为int类型，然后list再转化成列表类型
        if num[0]==num[1]==0:
            break
        print(sum(num))
    except:
        break