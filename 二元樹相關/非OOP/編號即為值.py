#架構
btree = [
    None,   #值
    None,   #左子節點
    None    #右子節點
        ]

####################################################################################################

#走訪

####################################################################################################

#前序走訪
t_f = []  #儲存走過的
def pre_order(root):
    global t_f
    if not root is None:
        t_f.append(root[0])
        if not root[1] is None:
            pre_order(root[1])
        if not root[2] is None:
            pre_order(root[2])

#中序走訪
t_m = []  #儲存走過的
def in_order(root):
    global t_m
    if not root is None:
        if not root[1] is None:
            in_order(root[1])
        t_m.append(root[0])
        if not root[2] is None:
            in_order(root[2])

#後序走訪

t_b = []  #儲存走過的
def post_order(root):
    global t_b
    if not root is None:
        if not root[1] is None:
            post_order(root[1])
        if not root[2] is None:
            post_order(root[2])
        t_b.append(root[0])

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
        if root[1] is None:
            root[1] = node[:]
        else:
            return BST_add_node(root[1], node)
    #node < root
    if root[0] < node[0]:
        if root[2] is None:
            root[2] = node[:]
        else:
            return BST_add_node(root[2], node)
    nums.add(node[0])
    return root

bst = [5, None, None]
nums.add(5)
for i in [
          3,        7,
        1,  4,    6,  9,
      0,  2,         8, 10
        ]:
    BST_add_node(bst, [i,None,None])
#print(bst)

####################################################################################################

#前序走訪
t_f = []
pre_order(bst)
#print(t_f)

#中序走訪
t_m = []
in_order(bst)
#print(t_m)

#後序走訪
t_b = []
post_order(bst)
#print(t_b)

####################################################################################################

#二元堆積樹

####################################################################################################

#最大堆積樹

#新增元素
nums = set()#已用過的編號
def post_inax_h_add_node(root, node):
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
        node[1] = root
        return node
    #None in root
    if root[1] is None:
        root[1] = node
        return root
    elif root[2] is None:
        root[2] = node
        return root
    #子節點 < node
    if root[1][0] > node[0]:
        return post_inax_h_add_node(root[1], node)
    elif root[2][0] > node[0]:
        return post_inax_h_add_node(root[2], node)
    else:#子節點 > node
        root[1] = post_inax_h_add_node(root[1], node)
    nums.add(node[0])
    return root
    
post_inax_h = [5, None, None]
nums.add(5)
for i in range(1, 11):
    post_inax_h = post_inax_h_add_node(post_inax_h, [i,None,None])
#print(post_inax_h)

#前序走訪
t_f = []  #儲存走過的
pre_order(post_inax_h)
#print(t_f)

#中序走訪
t_m = []  #儲存走過的
in_order(post_inax_h)
#print(t_m)

#後序走訪
t_b = []  #儲存走過的
post_order(post_inax_h)
#print(t_b)

####################################################################################################

#最小堆積樹

#新增元素
nums = set()#已用過的編號
def post_inin_h_add_node(root, node):
    global nums
    #node 已存在
    if node[0] in nums:
        return root
    #root 不存在
    if root is None:
        return node
    #node < root
    if root[0] > node[0]:
        node[1] = root
        return node
    #None in root
    if root[1] is None:
        root[1] = node
        return root
    elif root[2] is None:
        root[2] = node
        return root
    #子節點 < node
    if root[1][0] < node[0]:
        root[1] = post_inin_h_add_node(root[1], node)
    elif root[2][0] < node[0]:
        root[2] =  post_inin_h_add_node(root[2], node)
    else:#子節點 > node
        root[1] = post_inin_h_add_node(root[1], node)
    nums.add(node[0])
    return root

post_inin_h = [5, None, None]
nums.add(5)
for i in range(1, 11):
    post_inin_h = post_inin_h_add_node(post_inin_h, [i,None,None])
#print(post_inin_h)

#前序走訪
t_f = []  #儲存走過的
pre_order(post_inin_h)
#print(t_f)

#中序走訪
t_m = []  #儲存走過的
in_order(post_inin_h)
#print(t_m)

#後序走訪
t_b = []  #儲存走過的
post_order(post_inin_h)
#print(t_b)

####################################################################################################

#已知兩中走訪結果，創建二元樹
#兩種必包含 中序走訪

#前序走訪： 根 左 右 ， 可得到第一個值為 根節點
#中序走訪： 左 根 右 ， 可得到 根節點 左側為 左子樹，右側為 右子樹
#後序走訪： 左 右 根 ， 可得到最後一個值為 根節點

class mktree_by_Traversal():
    #   三種走訪都要以串列表示

    #已知 前 + 中
    def pre_in( pre_order, in_order ):
        
        #如果長度 < 2
        if len( pre_order ) == 0:
            return None
        if len( pre_order ) == 1:
            return pre_order + [ None, None ]
        
        # 前序走訪 第一個值為 根節點
        root = pre_order[0]
        
        # 中序走訪 根節點 左側為 左子樹，右側為 右子樹
        root_m_index = in_order.index( root )
        m_left = in_order[ : root_m_index ]
        m_right = in_order[ root_m_index+1 : ]
        
        # 前序走訪 順序為 根 左 右
        left_long = len( m_left )
        f_left = pre_order[ 1 : left_long + 1 ]
        f_right = pre_order[ left_long + 1 : ]
        
        #建立左子樹
        left = mktree_by_Traversal.pre_in( f_left, m_left )
        
        #建立右子樹
        right = mktree_by_Traversal.pre_in( f_right, m_right )
        
        #建立樹
        tree = [ root, left, right ]
        return tree
    
    #已知 後 + 中
    def post_in( post_order, in_order ):
        
        #如果長度 < 2
        if len( post_order ) == 0:
            return None
        if len( post_order ) == 1:
            return post_order + [ None, None ]
        
        # 後序走訪 最後一個值為 根節點
        root = post_order[-1]
        
        # 中序走訪 根節點 左側為 左子樹，右側為 右子樹
        root_m_index = in_order.index( root )
        m_left = in_order[ : root_m_index ]
        m_right = in_order[ root_m_index+1 : ]
        
        # 後序走訪 順序為 左 右 根
        left_long = len( m_left )
        b_left = post_order[ : left_long ]
        b_right = post_order[ left_long : -1 ]
        
        #建立左子樹
        left = mktree_by_Traversal.post_in( b_left, m_left )
        
        #建立右子樹
        right = mktree_by_Traversal.post_in( b_right, m_right )
        
        #建立樹
        tree = [ root, left, right ]
        return tree

b_tree_pre_order = '0,1,3,6,4,7,2,5,8,9'.split(',')
b_tree_in_order   = '6,3,1,7,4,0,2,8,5,9'.split(',')
b_tree_post_order  = '6,3,7,4,1,8,9,5,2,0'.split(',')

b_tree = mktree_by_Traversal.pre_in( b_tree_pre_order, b_tree_in_order )
#print(b_tree)

pre_order( b_tree ) 
in_order( b_tree )
post_order( b_tree )

#print( t_f )
#print( t_m )
#print( *t_b)

b_tree = mktree_by_Traversal.post_in( b_tree_post_order, b_tree_in_order )
#print(b_tree)

pre_order( b_tree ) 
in_order( b_tree )
post_order( b_tree )

#print( *t_f )
#print( t_m )
#print( t_b)