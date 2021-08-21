
t = int(input())
for i in range(t):
    while True:
        try:
            num=list(map(int,input().split(" ")))
            print(sum(num[1:]))
        except:
            break

