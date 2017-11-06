

class node:
    # binary tree node 
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def get_deep_right(self):
        tmp = self.right

        while tmp != None:
            tmp = tmp.right
        
        return tmp



def pivot_right(root):
    if root.left != None:
        piv = root.left
        root.left = piv.right
        piv.right = root
        root = piv
    return root # return new root
        

        

