"""
10 9 2 5 3 7 101 18 19 20 14 21
https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-by-leetcode-soluti/
希望每次在上升子序列最后加上的那个数尽可能的小
"""
class Solution:

    def lengthOfLIS(self, num):
        d=[]
        for n in num:
            if not d or n>d[-1]:
                d.append(n)
            else:
                left,right=0,len(d)-1
                cur_location=right
                while left<=right:
                    mid=(left+right)//2
                    if d(mid)>=n:
                        cur_location=mid
                        right=mid-1
                    else:
                        left=mid+1
                d[cur_location]=n
        return len(d)


while True:
    try:
        num=list(map(int,input().strip().split(" ")))
        print(num)
        res=Solution().lengthOfLIS(num)
        print(res)
    except:
        break