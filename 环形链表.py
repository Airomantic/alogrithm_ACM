import io
import json
import sys

def stringToIntegerInt(input):
    return json.loads(input)

class ListNode:
    def __init__(self,x):
        self.val=x #注意这里不要写成self.x=x
        self.next=None

""".next是结点"""
def stringToListNode(input,pos):
    numbers=stringToIntegerInt(input)

    dummyRoot=ListNode(0) #初始化出哑结点0
    print("ListNode(0)=",ListNode(0),"ListNode(0).next=",ListNode(0).next)
    ptr=dummyRoot #ptr指向哑结点，构造出头指针
    for number in numbers:
        ptr.next=ListNode(number) #实际头结点值，覆盖初始化哑结点的位置
        ptr=ptr.next

    newRoot=ListNode(0)
    newptr=newRoot
    newptr.next=ListNode(numbers[pos-1]) #在分叉处前一个结点 #注意数组名是numbers[]有和加[]
    ListNode(numbers[len(numbers)-1]).next=newptr.next #循环连接处，相当于指针重合，尾指针和pos-1的指针都指向pos

    ptr=dummyRoot.next
    return ptr #输出的是ListNode指针

class Solution:
    def hasCycler(self,head: ListNode):
        if not head or not head.next: #没有结点和只有一个结点的情况无法构成循环
            return False
        #定义两个指针（不是结点值）
        slow=head #头指针作为慢指针
        fast=head.next #注意这是快指针,当然也算头结点值
        # print("head.next=",head.next)
        while slow!=fast:
            if not fast or not fast.next:
                return False
            slow=slow.next
            fast=fast.next.next #每次走两步

        return True

def EnterMain():
    def readlines():
        for lines in io.TextIOWrapper(sys.stdin.buffer,encoding='utf-8'):
            yield lines.strip('\n')

    lines=readlines()
    while True:
        try:
            lineNode=next(lines)
            linePos=next(lines)
            pos=int(linePos)
            node=stringToListNode(lineNode,pos)
            result=Solution().hasCycler(node)
            out=str(result)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    EnterMain()