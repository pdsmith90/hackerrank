import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        nodeQ=[]
        nodeStr=''
        nodeQ.append(root)
        while len(nodeQ) > 0:
            node = nodeQ.pop(0)
            if node.left:
                nodeQ.append(node.left)
            if node.right:
                nodeQ.append(node.right)
            nodeStr += str(node.data) + ' '
        print(nodeStr)
                
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
