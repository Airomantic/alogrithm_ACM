import json
import sys
import io


def stringToIntegerList(input):
    return json.loads(input)


class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next


def stringToListNode(input):
    numbers=stringToIntegerList(input)
    dummyRoot=ListNode(0)
    ptr=dummyRoot
    for number in numbers:
        ptr.next =ListNode(number)
        ptr=ptr.next
    new =dummyRoot.next
    return new


class Solution:
    def addTwoNumbers(self, l1:ListNode, l2:ListNode):
        head=ListNode()
        p=head
        carry=0
        while carry or l1 or l2:
            var=carry
            if l1:
                var1=l1.val+var
                l1=l1.next
            if l2:
                var2=l2.val+var1
                l2=l2.next
            carry,var3=divmod(var2,10)
            p.next=ListNode(var3)
            p=p.next
        return head.next


def ListNodeToString(node):
    if not node:
        return None
    result=""
    while node:
        result+=str(node.val)+', '
        node=node.next
    return "["+result[:-2]+"]"


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