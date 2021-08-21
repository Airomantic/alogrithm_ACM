while True:
    try:
        num = list(input().split(" "))  # 直接转化成列表类型就可以了，map是用来绑定字符类型的
        num.sort()
        print(" ".join(num))
    except:
        break