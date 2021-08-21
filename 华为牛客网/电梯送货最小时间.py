class Solution:

    def MinTime(self, start, end):
        time=0
        cha=abs(end-start)+1
        while cha!=0:

            cha = abs(end - start) + 1
            if cha>0:
                start+=1
                time+=1
            else:
                start -= 1
            start*=2
            start/=2

        return minTime


while True:
    try:
        n=list(map(int,input().split(' ')))
        start=n[0]
        end=n[1]
        res=Solution().MinTime(start,end)
    except:
        break

