
"""
三个空瓶子换一瓶新的
输入：
10
输出
5
输入：
3
输出
1
"""

while True:
    try:
        n = int(input())
        if n:
            print(n//2)
    except:
        break