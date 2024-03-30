# # 108 年技藝競賽 第 4-2 題


# 有一個迷宮長這樣
# | 1  2  3  4|
# | 5  6  7  8|
# | 9 10 11 12|
# |13 14 15 16|
# 每個數字代表那格的成本
# 要求出左上角跑到右下角所需的最小成本
# 只能 往左 或 往右

# 輸入說明
# 第一列的數字 n 代表有幾筆資料要測試 ( 2 <= n <= 20 )
# 每筆資料第一列的數字 N 代表列數 ( 1 <= N <= 999 )
# 第二列的數字 M 代表行數 ( 1 <= M <= 999 )
# 接下來 N 列 代表迷宮每一列的數字，每個數字用空白隔開

# 輸出說明
# 輸出 最小成本

# n筆資料
for r in range(int(input())):
    
    # 共 wei 列
    wei = int(input())
    # 共 ru 行
    ru = int(input())
    # 每一列的數字
    array = [ list(map( int, input().strip().split() )) for i in range(wei) ]
    
    # 轉成圖形
    
    
    graph = {}  # { 父節點 : { 子節點 : 權重 } }
    
    # 起點
    graph["start"] = {}
    graph['start']['0-0'] = array[0][0]
    
    # 各節點
    for i in range( wei ):
        for j in range( ru ):
            
            # 當前節點會是其他節點的父節點
            graph[f'{i}-{j}'] = {} 
            
            # 如果當前節點是 左上角，已經設定為起點了， 所以不用再設定為 別的節點 的子節點
            if i == j == 0:
                continue
            
            # 每個節點都是 正上方一格的子節點 或 正左方一格的子節點
            if not (i == 0):    # 假如是第一列，沒有上方的父節點
                graph[f'{i-1}-{j}'][f'{i}-{j}'] = array[i][j]
            if not (j == 0):    # 假如是第一欄，沒有左方的父節點
                graph[f'{i}-{j-1}'][f'{i}-{j}'] = array[i][j]
    
    # 終點
    graph[f'{len(array)-1}-{len(array[0])-1}']
    graph[f'{i}-{j}']['fin'] = 0
    graph['fin'] = {}
    
    # 記錄各節點 的 最小累計成本
    
    
    infinity = float("inf")
    
    costs = {}  # { 節點 : 最小累計成本 }
    
    for i in range( len(array)):
        for j in range( len(array[0])):
            
            if i == j == 0:
                
                # 起點的最小累計成本為自己本身
                costs[f'{i}-{j}'] = array[0][0]
                
            else:
                
                # 其他節點預設為無限大
                costs[ f'{i}-{j}' ] = infinity
                
    # 終點預設為無限大
    costs["fin"] = infinity

    # 紀錄各節點產生最小成本時的父節點，以產生最佳解的路徑 ( 本題不需要 )
    
    
    parents = {}    # { 節點 : 父節點 }
    
    # 起點
    parents['0-0'] = 'start'
    
    # 終點
    parents["fin"] = f'{len(array)-1}-{len(array[0])-1}'


    # 開始處理資料
    
    
    # 紀錄已經更新過的節點
    processed = []

    # 找出成本最小的節點
    def find_lowest_cost_node(costs):
        
        # 還沒找到 最小成本的節點 的成本 ，預設無限
        lowest_cost = float("inf")
        # 還沒找到 最小成本的節點，預設 None ，這樣找不到就回傳 None
        lowest_cost_node = None
        
        # 查看所有節點
        for node in costs:
            
            # 當前節點的成本
            cost = costs[node]
            
            # 假如 ( 當前節點成本 小於 當前最小成本的節點 ) 且 ( 當前節點 尚未更新成本 )
            if cost < lowest_cost and node not in processed:
                
                # 把最小成本節點 的成本 設為 當前節點成本
                lowest_cost = cost
                # 把最小成本的節點 設為 當前節點
                lowest_cost_node = node
        
        # 回傳最小成本節點
        return lowest_cost_node

    # 成本最小的節點
    node = find_lowest_cost_node(costs)
    
    # 不斷重複，直到所有節點都更新成本
    while node is not None:
        
        # 當前最小成本節點 的成本
        cost = costs[node]
        
        # 所有 當前最小成本節點 的 子節點 及 權重
        neighbors = graph[node]
        
        # 所有 當前最小成本節點 的 子節點
        for n in neighbors.keys():
            
            # 假如往這個節點走，產生的成本
            new_cost = cost + neighbors[n]
            
            # 如果往這走的成本比當前成本小
            if costs[n] > new_cost:
                
                # 更新 當前節點 的成本
                costs[n] = new_cost
                # 把 這節點的父節點 設為 當前節點
                parents[n] = node
                
        # 紀錄已經更新此節點
        processed.append(node)
        # 找下一個節點
        node = find_lowest_cost_node(costs)

    # 輸出終點的成本
    print(costs["fin"])