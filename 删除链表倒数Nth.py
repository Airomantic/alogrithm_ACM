# Definition for singly-linked list.
import json
"""
删除链表的倒数第N个节点
解决：快慢针
从表头算就是 L-n+1
"""
class ListNode:
    def __init__(self, val=0, next=None): #后面两个都是初始化
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy=ListNode(0,head) #设置哑结点，就是在链表头之前的指向链表头的节点（如果不设置，链表只能从表头开始）
        first = head
        second = dummy
        for i in range(n):
            print("先让快指针走：",i)
            first = first.next
        print("当i=n+1时，快指针带动慢指针一起走")
        while first:
            first = first.next
            second = second.next
        #dummy假指针保证倒数第n个数前一个结点（倒数第n+1个数）的指针跳过倒数第n个数指向倒数第n-1个数
        second.next = second.next.next
        return dummy.next
def stringToIntegerList(input):
    return json.loads(input)
def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)
    print(numbers)
    # Now convert that list into linked list
    dummyRoot = ListNode(0) #还是那句思考，声明或构造一个ListNode，并且(0)，这里还只是头结点
    ptr = dummyRoot #这可不是赋值，指向头结点即ptr为哑结点 链表表头之前指向链表头的结点 同时为ptr声明或说构造一个ListNode类型
    for number in numbers:
        ptr.next = ListNode(number) #因为是哑结点的假指针指向的是头指针
        ptr = ptr.next #接着循环下去 即ptr = ptr.next链接替换掉ptr=dummyRoot
    ptr = dummyRoot.next #让它具有哑结点的假指针
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", " #注意它这里是逗号加空格
        node = node.next
    return "[" + result[:-2] + "]" #-2的意思是去掉最后一个数字后面的逗号，如" 5, "，再加上]，一维直接写列:-2

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines) #next(iterobject,defalt)
            head = stringToListNode(line);
            line = next(lines)
            n = int(line);

            ret = Solution().removeNthFromEnd(head, n)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()