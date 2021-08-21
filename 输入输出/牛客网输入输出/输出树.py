class Node(object):
    '''树节点'''
    def __init__(self, item):
        self.elem = item
        self.lchild = None
        self.rchild = None


class Tree(object):
    '''二叉树'''

    def __init__(self, node=None):
        '''初始化，根节点为None'''
        self.root = node

    def add(self, item):
        '''添加节点，广度遍历找出可以添加的位置'''
        node = Node(item)

        # 如果二叉树为空，则直接往根节点添加
        if self.root is None:
            self.root = node
        else:
            # 创建一个队列，即列表
            queue = []
            queue.append(self.root)

            # 只要队列不为空，就不断从队列头端取出节点进行判断
            while queue:
                cur_node = queue.pop(0)
                # 如果节点的左孩子为空，说明有位置存放节点
                if cur_node.lchild is None:
                    cur_node.lchild = node
                    return
                # 如果节点的左孩子不为空，就将左孩子节点往队列后端添加
                else:
                    queue.append(cur_node.lchild)

                # 如果节点的右孩子为空，说明有位置存放节点
                if cur_node.rchild is None:
                    cur_node.rchild = node
                    return
                # 如果节点的右孩子不为空，就将左孩子节点往队列后端添加
                else:
                    queue.append(cur_node.rchild)
    """广度优先遍历(层次遍历)"""
    def breadth_travel(self):
        '''广度遍历'''
        # 如果二叉树为空，则直接结束函数
        if self.root is None:
            return
        # 遍历树的每个节点
        else:
            queue = [self.root]
            # 只要树不为空，就循环打印出节点的元素
            while queue:
                # 从队列的头端取出节点，进行判断是否空
                cur = queue.pop(0)
                print(cur.elem, end=' ')
                # 判断左右孩子节点如果不为空，就往队列的后端添加元素，达到遍历的效果
                if cur.lchild:
                    queue.append(cur.lchild)
                if cur.rchild:
                    queue.append(cur.rchild)

    """深度遍历包括：先序遍历、中序遍历、后序遍历"""
    def preorder_taravel(self, root):
        '''先序遍历， 根节点->左子树->右子树，
        先序遍历 在先序遍历中，我们先访问根节点，然后递归使用先序遍历访问左子树，再递归使用先序遍历访问右子树
        '''
        if root is None:
            return
        else:
            print(root.elem, end=' ')
            self.preorder_taravel(root.lchild)
            self.preorder_taravel(root.rchild)

    def inorder_taravel(self, root):
        '''中序遍历， 左子树->根节点->右子树，
        中序遍历 在中序遍历中，我们递归使用中序遍历访问左子树，然后访问根节点，最后再递归使用中序遍历访问右子树
        '''
        if root is None:
            return
        else:
            self.inorder_taravel(root.lchild)
            print(root.elem, end=' ')
            self.inorder_taravel(root.rchild)

    def postorder_taravel(self, root):
        '''后序遍历， 左子树->右子树->根节点，
        后序遍历 在后序遍历中，我们先递归使用后序遍历访问左子树和右子树，最后访问根节点
        '''
        if root is None:
            return
        else:
            self.postorder_taravel(root.lchild)
            self.postorder_taravel(root.rchild)
            print(root.elem, end=' ')


# 测试
if __name__ == '__main__':
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)

    print('广度遍历: ', end='')
    tree.breadth_travel()
    print()
    print('先序遍历: ', end='')
    tree.preorder_taravel(tree.root)
    print()
    print('中序遍历: ', end='')
    tree.inorder_taravel(tree.root)
    print()
    print('后序遍历: ', end='')
    tree.postorder_taravel(tree.root)