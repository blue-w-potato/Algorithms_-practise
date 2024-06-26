#架構
btree = [
    0,  #編號
    None,   #值
    None,   #左子節點
    None    #右子節點
        ]

####################################################################################################

#走訪

####################################################################################################

#前序走訪
t_f = []  #儲存走過的
def front(root):
    global t_f
    if not root is None:
        t_f.append(root[1])
        if not root[2] is None:
            front(root[2])
        if not root[3] is None:
            front(root[3])

#中序走訪
t_m = []  #儲存走過的
def mid(root):
    global t_m
    if not root is None:
        if not root[2] is None:
            mid(root[2])
        t_m.append(root[1])
        if not root[3] is None:
            mid(root[3])

#後序走訪

t_b = []  #儲存走過的
def back(root):
    global t_b
    if not root is None:
        if not root[2] is None:
            back(root[2])
        if not root[3] is None:
            back(root[3])
        t_b.append(root[1])

####################################################################################################

#二元搜尋樹

####################################################################################################

#新增元素
nums = set()#已用過的編號
def BST_add_node(root, node):
    global nums
    #node 已存在
    if node[0] in nums:
        return root
    #root 不存在
    if root is None:
        return node
    #node > root
    if root[0] > node[0]:
        if root[2] is None:
            root[2] = node[:]
        else:
            return BST_add_node(root[2], node)
    #node < root
    if root[0] < node[0]:
        if root[3] is None:
            root[3] = node[:]
        else:
            return BST_add_node(root[3], node)
    nums.add(node[0])
    return root

bst = [5, 5, None, None]
nums.add(5)
for i in [
          3,        7,
        1,  4,    6,  9,
      0,  2,         8, 10
        ]:
    BST_add_node(bst, [i,i,None,None])
print(bst)

####################################################################################################

#前序走訪
t_f = []
front(bst)
print(t_f)

#中序走訪
t_m = []
mid(bst)
print(t_m)

#後序走訪
t_b = []
back(bst)
print(t_b)

####################################################################################################

#二元堆積樹

####################################################################################################

#最大堆積樹

#新增元素
nums = set()#已用過的編號
def max_heap_tree_add_node(root, node):
    global nums
    #node 已存在
    if node[0] in nums:
        return root
    #root 不存在
    if root is None:
        return node
    #node = root
    if root[0] == node[0]:
        return root
    #node > root
    if root[0] < node[0]:
        node[2] = root
        return node
    #None in root
    if root[2] is None:
        root[2] = node
        return root
    elif root[3] is None:
        root[3] = node
        return root
    #子節點 < node
    if root[2][0] > node[0]:
        return max_heap_tree_add_node(root[2], node)
    elif root[3][0] > node[0]:
        return max_heap_tree_add_node(root[3], node)
    else:#子節點 > node
        root[2] = max_heap_tree_add_node(root[2], node)
    nums.add(node[0])
    return root
    
max_heap_tree = [5, 5, None, None]
nums.add(5)
for i in range(1, 11):
    max_heap_tree = max_heap_tree_add_node(max_heap_tree, [i,i,None,None])
print(max_heap_tree)

#前序走訪
t_f = []  #儲存走過的
front(max_heap_tree)
print(t_f)

#中序走訪
t_m = []  #儲存走過的
mid(max_heap_tree)
print(t_m)

#後序走訪
t_b = []  #儲存走過的
back(max_heap_tree)
print(t_b)

####################################################################################################

#最小堆積樹

#新增元素
nums = set()#已用過的編號
def min_heap_tree_add_node(root, node):
    global nums
    #node 已存在
    if node[0] in nums:
        return root
    #root 不存在
    if root is None:
        return node
    #node < root
    if root[0] > node[0]:
        node[2] = root
        return node
    #None in root
    if root[2] is None:
        root[2] = node
        return root
    elif root[3] is None:
        root[3] = node
        return root
    #子節點 < node
    if root[2][0] < node[0]:
        root[2] = min_heap_tree_add_node(root[2], node)
    elif root[3][0] < node[0]:
        root[3] =  min_heap_tree_add_node(root[3], node)
    else:#子節點 > node
        root[2] = min_heap_tree_add_node(root[2], node)
    nums.add(node[0])
    return root
    
min_heap_tree = [5, 5, None, None]
nums.add(5)
for i in range(1, 11):
    min_heap_tree = min_heap_tree_add_node(min_heap_tree, [i,i,None,None])
print(min_heap_tree)

#前序走訪
t_f = []  #儲存走過的
front(min_heap_tree)
print(t_f)

#中序走訪
t_m = []  #儲存走過的
mid(min_heap_tree)
print(t_m)

#後序走訪
t_b = []  #儲存走過的
back(min_heap_tree)
print(t_b)