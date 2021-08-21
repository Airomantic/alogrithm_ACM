import heapq
import json
# from Cython.Compiler.ExprNodes import ListNode #自定义ListNode不要这句
from typing import List
'''
把所有元素push到最小堆里面，放进最小堆的性质是等拿出来等时候就是自动有序的了（数据结构）
每次从堆里面取出一个元素，构造出一个链表
(可直接通过封装好的heapq函数来构建一个最小堆)
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # 可变，数值
        self.next = next  # 节点，指向列表的下一个数字

class Solution: #输入list列表里面放ListNode
    def mergeKLists(self, lists: List[ListNode]) -> ListNode: #lists为别名
        h=[] #构建minheap
        '''1.读入所有结点的值到最小堆里面'''
        for head in lists: #遍历列表里面的每一个表头，多个链表
            node=head #让表头赋值给node结点
            while node: #遍历node，当它不为空时，找到它的下一个值，并把它放到minheap里面
                h.append(node.val) #把当前结点的值加进去
                node=node.next #结点往后移
        '''2.构造minheap'''
        if not h: #[ [] ],这一步不能少，有可能会出现链表里面包含一个空值
            return None
        heapq.heapify(h) #这里接受的是h列表List，要先判空
        '''3.构造链表，从minheap拿出来是有序的'''
        root=ListNode(heapq.heappop(h)) #声明或说构造一个root的类型满足：放到链表是ListNode类型，括号里就是放进去的最小堆元素（堆最小值作为头结点）
        curnode=root #定义一个当前结点，让它不断下移，一开始是指向头结点

        while h: #如果最小堆还是不为空的话，就去构造下一个结点
            nextNode=ListNode(heapq.heappop(h))# 声明或说构造一个nextnode类型满足：从最小堆拿出来的元素放到ListNode类型里面
            curnode.next=nextNode #使当前结点的下一个指向新构造的这个nextNode
            curnode=nextNode #当前结点指向下一个结点
        return root #返回这个链表的头结点

def stringToIntegerList(input):
    return json.loads(input)

def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input) #先定义成List[int]

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers: #再
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


def ListNodeToIntegerList(LN):
    pass


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            IL=ListNodeToIntegerList(line)
            LN = stringToListNode(line);#输入字符转成listNode类型
            L_LN= ListNodeToIntegerList(LN) #转成List[ListNode]类型

            ret = Solution().mergeKLists(L_LN)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()

