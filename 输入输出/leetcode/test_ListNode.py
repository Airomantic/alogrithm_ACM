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
        ptr = ptr.next #接着循环下去
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


class Node(object):
    """创建一个结点类"""
    def __init__(self, data):
        self.data = data
        self.next = None

class create_circular_linked_list(object):
    """创建一个创建循环链表的类"""

    def __init__(self):
        self.head = None

    def is_empty(self):
        """判断循环链表是否为空"""
        return self.head is None

    def length(self):
        """获取循环链表的长度"""
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            # 如果当前结点的下一个结点是头结点，说明这个结点就是尾结点
            # 如果不是，就将指针向后移动一个
            if cur.next == self.head:
                break
            else:
                cur = cur.next
        return count

    def add_first(self, data):
        """在头部添加结点"""
        node = Node(data)
        if self.is_empty():
            self.head = node
            node.next = self.head
        else:
            cur = self.head
            # 将指针移动到尾部结点
            while cur.next is not self.head:
                cur = cur.next
            # 尾部结点指向新节点
            cur.next = node
            # 新结点指向原来的头结点
            node.next = self.head
            # 再将头结点的称号给新结点
            self.head = node

        