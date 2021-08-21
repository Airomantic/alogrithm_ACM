import io
import json
import sys
from typing import List


def stringToIntegerList(input):
    return json.loads(input)


class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right



def TreeNodeToString(root): #利用队列
    if not root:
        return '[]'
    output=""
    current=0
    Queue=[root]
    while current != len(Queue):
        node=Queue[current]
        current+=1

        if not node:
            output += "null, "
            continue

        output+= str(node.value) + ", " #注意这里是node.val
        Queue.append(node.left)
        Queue.append(node.right)
    return "["+output[:-2]+"]"


def EnterMain():
    def readlines():
        for lines in io.TextIOWrapper(sys.stdin.buffer,encoding='utf-8'):
            yield lines.strip('\n')
            
    lines=readlines()
    while True:
        try:
            line = next(lines)
            pre = stringToIntegerList(line)
            line = next(lines)
            post= stringToIntegerList(line)
            TN=Solution().constructFromPrePost(pre,post)
            result=TreeNodeToString(TN)
            print(result)
        except StopIteration:
            break


if __name__ == '__main__':
    EnterMain()