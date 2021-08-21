def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

while True:
    try:
        arr=list(map(int,input().strip().split(" "))) #split(" ")按空格区分元素，strip()strip()函数只能删除头和尾内容
        res=quicksort(arr) #要int型的list
        # '.join()去除字符list，按间隔空格输出
        print(' '.join(str(i) for i in res)) #要把内部元素先转成字符在去除，不能从外部str(res)
    except:
        break