import io
import json
import sys
""" 链表逆序之和 """
class ListNode:
    def __init__(self,value=0,next=None):
        self.value=value
        self.next=next

def stringToIntegerList(line):
    return json.loads(line)

def stringToListNode(line):
    numbers=stringToIntegerList(line)

    dummyRoot=ListNode(0) #哑结点的指针
    ptr=dummyRoot #声明与构造 ptr具备ListNode类型并被赋予哑结点的指针，即具备指向头结点的性能，则头结点就是ptr.next
    for number in numbers:
        ptr.next=ListNode(number) #结点的赋值
        ptr=ptr.next #结点值依次传递
    new=dummyRoot.next #哑结点值传递（这样能保证从头到尾都能循环）
    return new #这里的new是结点值，因为它是.next赋值过来的

class Solution:
    def addTwoNumbers(self,l1:ListNode,l2:ListNode):
        head=ListNode() #注意这里不用赋予(0)，无需哑结点，只需具备ListNode类型
        p=head #等下利用p进行循环
        carry=0
        while carry or l1 or l2:
            var = carry  # 关键点：val为0或1，满10进1，商作为进位
            if l1:
                var1= l1.value + var
                l1=l1.next
            if l2:
                var2 = l2.value + var1
                l2=l2.next
            carry,var3=divmod(var2,10) #商，余数
            p.next=ListNode(var3)
            p=p.next
        return head.next #p只能一个一个的带值，用全部存入ListNode后，赋给head来读出

def ListNodeToString(node):
    if not node:
        return "[]"
    result=""
    while node:
        result+=str(node.val)+","
        node=node.next
    return "["+result[:-1]+"]"

def EnterMain():
    def readline():
        for line in io.TextIOWrapper(sys.stdin.buffer,encoding='utf-8'):
            yield line.strip('\n')
    lines=readline()

    while True:
        try:
            line=next(lines)
            l1=stringToListNode(line)
            line=next(lines)
            l2=stringToListNode(line)
            node=Solution().addTwoNumbers(l1, l2)
            out=ListNodeToString(node)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    EnterMain()