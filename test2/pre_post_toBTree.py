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

class Solution:
    def constructToBT(self, pre:List[int], post:List[int]):

        if not pre:
            return None
        root = TreeNode(pre[0])

        if len(pre) == 1:
            return root

        L = post.index(pre[1]) + 1
        root.left = self.constructToBT(pre[1:L + 1], post[:L])
        root.right = self.constructToBT(pre[L + 1:], post[L:-2]) #注意是L:-2

        return root

def TreeNodeTostring(root):

    if not root:
        return '[]'
    output=""
    queue=[root]
    current=0

    while current!=len(queue):
        node=queue[current]
        current+=1

        if not node:
            output+='null, '
            continue       #continue只放在while下

        output +=str(node.val)+", "
        queue.append(root.left)
        queue.append(root.right)

    return "["+output[:-2]+"]"



def main():
    def readlines():
        for lines in io.TextIOWrapper(sys.stdin.buffer,encoding='utf-8'):
            yield lines.strip('\n')

    lines=readlines()
    while True:
        try:
            line=next(lines)
            pre=stringToIntegerList(line)
            line2 = next(lines)
            post = stringToIntegerList(line2)
            result=Solution().constructToBT(pre,post)
            out=TreeNodeTostring(result)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()