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


    return ptr #输出的是ListNode指针

class Solution:
    def hasCycler(self,head: ListNode):
        if not head or not head.next:
            return False

        slow =head
        fast =head.next

        while slow!=fast:
            if not fast or fast.next:
                return False

            slow=slow.next
            fast=fast.next.next

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