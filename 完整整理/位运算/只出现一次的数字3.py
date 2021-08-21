
"""
任何数和本身 异或 则为1，异为1，同为0
空间复杂度：O(1)O(1)，只需要常数的空间存放若干变量，没有存储数组list或哈希dict等
functools.reduce()
https://blog.csdn.net/qq_31347869/article/details/105816793
位运算：左移 高位丢弃，低位补0    a<<n   =>   a*(2^n)

1 2 1 3 2 5
"""
import functools


class Solution:

    def singleNumber(self, number):

        res=functools.reduce(lambda x,y:x^y,number) #x与y的异或

        div=1  #二进制就是00000001=>00000010即2^1=2
        while div & res==0:
            div<<=1 #2 4 8 16 ...
        a,b=0,0
        for n in number:
            if n & div: #按位与 00000001 & 00000010 =>00000000 则进行else，位与只有都是1才为1
                a^=n
            else:
                print("b1=",b)
                b^=n #注意这可不是次方，次方是**，这是按位异或，比如b=00000000^00000001=00000001

        return [a,b]



if __name__ == '__main__':
    while True:
        number=list(map(int,input().strip().split()))
        res=Solution().singleNumber(number)
        res=''.join(str(res))
        print(res)