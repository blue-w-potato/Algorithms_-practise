# zerojudge f310 war


# 給定 N 個人( 編號為 0, 1, 2,..., N-1 )和 4 種操作方式，模擬一系列的操作並輸出過程中的結果。
# 只有一筆測資，指令的形式一定是 c X Y ，c 代表類型，X Y 代表不同編號的人員且保證 0 ≦ X, Y < N 。
# 操作的指令以 0 0 0 作為該次輸入的結尾，人數限制 N < 10,000。

# 操作方式：
#      c = 1, setFriends( X, Y )   設定 X, Y 為朋友關係 ( 屬於同個國家 )
#      c = 2, setEnemies( X, Y )  設定X, Y 為敵對關係 ( 屬於不同國家 )
#      c = 3, areFriends( X, Y )   確認 X, Y 是否為朋友關係？
#      c = 4, areEnemies( X, Y )  確認 X, Y 是否為敵對關係？
#       前兩個操作 setFriends( X, Y ) / setEnemies( X, Y ) 設定關係時如果存在矛盾時則該次設定無效 且 輸出 -1 作為代表。 
#       後兩個操作 areFriends( X, Y ) / areEnemies( X, Y ) 時若 X Y 關係「不清楚」(設定並未提到)一樣是輸出 0。

# 關係皆具有下列７項性質，符號說明：Ａ~Ｂ代表ＡＢ為朋友關係而Ａ*Ｂ代表ＡＢ為敵對關係。
#       1. 朋友的朋友也是朋友： If x ~ y and y ~ z then x ~ z
#       2. 敵人的敵人會是朋友： If x * y and y * z then x ~ z 
#       3. 朋友的敵人也是敵人：If x ~ y and y * z then x * z 
#       4. 朋友關係為相互性    ：If x ~ y then y ~ x      
#       5. 敵對關係為相互性   ： If x * y then y * x
#       6. 自己和自己一定是朋友關係：x ~ x 
#       7.  自己和自己一定不是敵對關係：Not x * x 

# 關係一定但設定後為永久性質，發生矛盾時則順序越後面設定的關係則視為無效。


# 並查集心法
# 1. 以 集合 處理資料
# 2. 合併有共通點的集合
# 3. 只查找有共通點的集合
# 4. 利用共通點節省時間

class DSU:
    
    # 合併集合
    def union(self,va,vb,A):
        self[str(va)]=self[str(va)]|A[str(vb)]
        A[str(vb)]=self[str(va)]
        
    # 合併 兩個為朋友關係的人 的 朋友名單 及 敵人名單
    def union_friend_set(va,vb):
        DSU.union(f,va,vb,f)
        DSU.union(e,va,vb,e)
    
    # 兩個為敵人關係的人 交錯合併 朋友名單 和 敵人名單 
    def union_enemy_set(va,vb):
        DSU.union(f,va,vb,e)
        DSU.union(f,vb,va,e)
    
    # 合併朋友的朋友
    def _FF_(va,vb):
        for aaa in f[str(va)]:  # 迭代 va 的朋友名單
            DSU.union_friend_set(aaa,vb)    # 跟朋友的朋友是朋友 ， 合併 朋友名單 及 敵人名單
        for aaa in f[str(vb)]:  # 迭代 vb 的朋友名單
            DSU.union_friend_set(aaa,va)    # 跟朋友的朋友是朋友 ， 合併 朋友名單 及 敵人名單
    
    # 合併朋友的敵人
    def _FE_(va,vb):
        for aaa in e[str(va)]:  # 迭代 va 的敵人名單
            DSU.union_enemy_set(aaa,vb)     # 跟朋友的敵人是敵人 ， 交錯合併 朋友名單 和 敵人名單 
        for aaa in e[str(vb)]:  # 迭代 vb 的敵人名單
            DSU.union_enemy_set(aaa,va)     # 跟朋友的敵人是敵人 ， 交錯合併 朋友名單 和 敵人名單 
    
    # 合併敵人的敵人
    def _EE_(va,vb):
        for aaa in e[str(va)]:  # 迭代 va 的敵人名單
            DSU.union_friend_set(aaa,vb)     # 跟敵人的敵人是朋友 ， 合併 朋友名單 及 敵人名單
        for aaa in e[str(vb)]:  # 迭代 vb 的敵人名單
            DSU.union_friend_set(aaa,va)     # 跟敵人的敵人是朋友 ， 合併 朋友名單 及 敵人名單
    
    # 合併敵人的朋友
    def _EF_(va,vb):
        for aaa in f[str(va)]:  # 迭代 va 的敵人名單
            DSU.union_enemy_set(aaa,vb)     # 跟敵人的朋友是敵人 ， 交錯合併 朋友名單 和 敵人名單
        for aaa in f[str(vb)]:  # 迭代 vb 的敵人名單
            DSU.union_enemy_set(aaa,va)     # 跟敵人的朋友是敵人 ， 交錯合併 朋友名單 和 敵人名單

# 朋友名單 及 敵人名單
f={};e={}

# 人數，用以建立名單
o=int(input())
for aaa in range(0,o):
    e[str(aaa)]=set();f[str(aaa)]={aaa,}

while True:
    
    # 輸入
    a=list(map(int,input().split()))
    
    # 如果輸入是 0 ， 結束迴圈
    if a[0]==0:
        break
    
    if a[0]==1:     # 如果要設定兩人為朋友
        
        # 如果要把兩個為敵人關係的人設定為朋友 ， 不要合併
        if a[2] in e[str(a[1])]:    
            print(-1)
            continue
    
        # 如果兩個不為敵人關係
        DSU.union_friend_set(a[1],a[2])
            
        # 合併朋友的朋友 
        DSU._FF_(a[1],a[2])
        
        # 合併朋友的敵人
        DSU._FE_(a[1],a[2])
        
    elif a[0]==2:   # 如果要設定兩人為敵人
        
        # 如果要把兩個為朋友關係的人設定為敵人 ， 不要合併
        if a[2] in f[str(a[1])]:
            print(-1)
            continue
        
        # 如果兩個不為朋友關係
        DSU.union_enemy_set(a[1],a[2])
        
        # 合併敵人的敵人
        DSU._EE_(a[1],a[2])
        
        # 合併敵人的朋友
        DSU._EF_(a[1],a[2])
        
    elif a[0]==3:   # 如果要確認兩人是否為朋友
        if a[1]in f[str(a[2])]:
            print(1)
        else:
            print(0)
            
    else:   # 如果要確認兩人是否為敵人
        if a[1]in e[str(a[2])]:
            print(1)
        else:
            print(0)