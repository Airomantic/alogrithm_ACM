
"""
https://leetcode-cn.com/problems/climbing-stairs/solution/pa-lou-ti-by-leetcode-solution/
https://blog.csdn.net/Jaggar_csdn/article/details/106544120
https://blog.csdn.net/bianxia123456/article/details/105167294/  整数快速幂和矩阵快速幂
斐波那锲
https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/solution/kuai-su-mi-fa-xiang-jie-by-mambafaithor-3fqw/
数列递归：f(n)=f(n-1)+f(n-2) 类似 斐波那契
「矩阵快速幂」
1.数列的递推关系转化为矩阵的递推关系
2.构造出一个矩阵的 n 次方乘以一个列向量得到一个列向量
3.列向量中包含我们要求的 f(n)
f(n)=IA*A*A*A*A*A.......
    1 0 | 1 1
    0 1 | 1 0
"""
import numpy as np
class Solution:
    def matrixPow(self, power):

        res=[[1,0],[0,1]]  # res初始值为单位矩阵
        A = [[1, 1], [1, 0]]
        # 开始矩阵运算，次幂按位右移
        while power != 0:
            if power & 1 != 0: #
                fn_res = self.multiMatrix(res, A) #[f(n+1) ,f(n)]=[f(1) f(0)]*矩阵幂，每次遇到幂不为0时，当前结果就要和矩阵幂乘一下
            print("整数幂前：",power)
            power >>= 1 # power =power>>1
            print("整数幂后：",power)
            A = self.multiMatrix(A, A) #矩阵幂
            # print(res,type(res))
        return fn_res

    def climbStairs(self, n):
        if n<2: #n是从0开始的
            return n
        res_matrix=self.matrixPow(n-1) ##跟斐波那契数列n-2不一样的地方是n-1
        res_matrix=res_matrix[0][0]+res_matrix[0][1] #最后[f(n+1) ,f(n)]的值就等于f(n+1)+f(n)
        # res_matrix=res_matrix % 1000000007 # #斐波那契数列需要这行"防止溢出"，爬楼梯不需要，否则在n=44就会报错
        return res_matrix

    def multiMatrix(self, x, y):
        n=len(x) #注意是x
        # ans = [[0]*n]*n  #这个不行
        ans=[[0]*n for i in range(n)] #记得要初始化
        print(ans)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    # print(ans[i][j], x[i][k] ,y[k][j])
                    ans[i][j] += x[i][k] * y[k][j] #k=0和1时叠加一次
        # ans= np.dot(x,y)
        # print("x=",x,"y=",y,"ans=",ans)
        # ans1 = x[0][0] * y[0][0] + x[0][1] * y[1][0] #ans1=ans[0][0]=k的左0右1之和
        # ans2 = x[0][0] * y[0][1] + x[0][1] * y[1][1] #ans2=ans[0][1]
        # ans3 = x[1][0] * y[0][0] + x[1][1] * y[1][0] #ans3=ans[1][0]
        # ans4 = x[1][0] * y[0][1] + x[1][1] * y[1][1] #ans4=ans[1][1]
        #ans[i][j]=[x,y,z,w]=x+y+z+w
        return ans

while True:
    try:
        n=int(input())
        res=Solution().climbStairs(n)
        print(res)
    except StopIteration:
        break