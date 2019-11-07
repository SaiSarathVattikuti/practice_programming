import sys


class Node:
    def __init__(self,value=None):
        self.value=value
        self.right_child=None
        self.left_child=None
        
def validate_Bst(root,min=-sys.maxsize,max=sys.maxsize):
     if root==None:
         return True
     if(root.value>min 
        and root.value<max 
        and validate_Bst(root.left_child,min,root.value)
        and validate_Bst(root.right_child,root.value,max)):
         return True
     else:
         return False
     
root=Node(5)
r=Node(6)
l=Node(5)        
root.left_child=l
root.right_child=r

print(validate_Bst(root))