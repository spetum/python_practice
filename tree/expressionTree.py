class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def init_tree():
    global root

    new_node = Node("-")
    root = new_node
    node = Node("A")
    root.left = node

    new_node = Node("/")
    root.right = new_node

    node_1 = Node("^")
    new_node.left = node_1
    node_2 = Node("E")
    new_node.right = node_2

    node_3 = Node("*")
    node_1.left = node_3
    node_4 = Node("D")
    node_1.right = node_4

    node_5 = Node("B")
    node_3.left = node_5
    node_6 = Node("C")
    node_3.right = node_6

def inorder_traverse(node) :
    if node is None: return
    inorder_traverse(node.left)
    print (node.data , end=' ')
    inorder_traverse(node.right)

def preorder_traverse(node) :
    if node is None: return
    print (node.data , end=' ')
    preorder_traverse(node.left)
    preorder_traverse(node.right)    

def postorder_traverse(node) :
    if node is None: return
    postorder_traverse(node.left)
    postorder_traverse(node.right)
    print (node.data , end=' ')

if __name__ =="__main__":
    init_tree()
    print('Infix')
    inorder_traverse(root)
    print('\nPrefix')
    preorder_traverse(root)
    print('\nPostfix')
    postorder_traverse(root)    



