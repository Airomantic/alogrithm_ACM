
"""

"""
class Solution:

    def mergeSort(self, A):
        if len(A)<=1:
            return A

        half=int(len(A)/2)
        """递归"""
        first=self.mergeSort(A[:half])
        second=self.mergeSort(A[half:])
        """把两部分合并"""
        i,j=0,0
        newA=[]
        while i<len(first) or j<len(second):
            #合并时，把两个数组中较小的一个插入新数组
            if i<len(first) and j<len(second):
                if first[i]<=second[j]:
                    newA.append(first[i])
                    i+=1
                else:
                    newA.append(second[i])
                    j+=1
            else:
                #如果后半部分数组已经全部插入newA，那么把前半部分剩余元素插入新数组
                if i < len(first):
                    newA.append(first[i])
                    i+=1
                #如果前半部分数组全部插入，则剩余后半部分元素插入newA
                if j<len(second):
                    newA.append(second[j])
                    j+=1
        return newA

while True:
    try:
        A=list(map(int,input().split(" ")))
        print(A)
        res=Solution().mergeSort(A)
        print(res)
    except:
        break