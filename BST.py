class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def insert(root,node):
    if root is None:
        root=node
    else:
        if root.val<node.val:
            if root.right is None:
                root.right=node
            else:
                insert(root.right,node)
        else:
            if root.left is None:
                root.left=node
            else:
                insert(root.left,node)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
def postorder(root):
    if root:
        
        postorder(root.left)
        postorder(root.right)
        print(root.val)

def preorder(root):
    if root:
        print(root.val)
        postorder(root.left)
        postorder(root.right)
               
        
r = Node(44) 
insert(r,Node(30)) 
insert(r,Node(20)) 
insert(r,Node(40)) 
insert(r,Node(70)) 
insert(r,Node(60)) 
insert(r,Node(80)) 
print("INORDER : ")
inorder(r)
print("------------------------------------------------")
print("POSTORDER : ")
postorder(r)
print("------------------------------------------------")
print("PREORDER : ")
preorder(r)
