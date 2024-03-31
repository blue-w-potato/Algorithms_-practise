#算 1 ~ 1000 階乘
base_1 = [ 0, 1 ]
def DP_1( n, base = base_1 ):
    if n < len(base):
        return base[n]
    base_1.append( n*DP_1(n-1) )
    return DP_1(n)

def test_1():
    num = 1000
    for i in range(num):
        DP_1( i )

#test_1()
#print(base_1)
        
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#算費氏數列 1 ~ 1000 項
base_2 = [ 0, 1, 1 ]
def DP_2( n, base = base_2 ):
    if n < len(base):
        return base[n]
    base_2.append( DP_2(n-1) + DP_2(n-2) )
    return DP_2(n)

def test_2():
    num = 1000
    for i in range(num):
        DP_2( i )
#test_2()
#print(base_2)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 背包問題
# 現在有個背包，地上有很多大大小小的東西，要放哪些才能最大的利用背包的空間
# 輸出 最大占用的總體積

# 例:
# 背包大小為 8
# 東西重量為 [ 1, 3, 4 ]

# 列為 背包大小，行為 東西體積

#      0  1  2  3  4  5  6  7  8
#    
#  X   0  0  0  0  0  0  0  0  0  此列為方便程式計算用
#  1   0  1  1  1  1  1  1  1  1
#  3   0  1  1  3  4  4  4  4  4
#  4   0  1  1  3  4  5  5  5  8

# 思路:
# 假如最多是 0 ， 直接輸出 0
# 假如最多是 1 ， 1 放得進去 ， 1 放進去之後剩下 0 ， 再來看 3 在 最多是 0 時能放多少 ， 然後 "1 放不進去時的最大體積" 跟 "這次計算結果" 中 比較大的就是 "當前背包大小的最大體積"
# 假如最多是 2 ， 1 放得進去 ， 1 放進去之後剩下 1 ， 再來看 3 在 最多是 1 時能放多少 ， 然後 "1 放不進去時的最大體積" 跟 "這次計算結果" 中 比較大的就是 "當前背包大小的最大體積"
# 假如最多是 3 ， 1,3 放得進去 ， 3 放進去之後剩下 0 ， 再來看 1 在 最多是 0 時能放多少 ， 然後 "3 放不進去時的最大體積" 跟 "這次計算結果" 中 比較大的就是 "當前背包大小的最大體積"
# 假如最多是 4 ， 1,3,4 放得進去 ， 4 放進去之後剩下 0 ， 再來看 3 在 最多是 0 時能放多少 ， 然後 "4 放不進去時的最大體積" 跟 "這次計算結果" 中 比較大的就是 "當前背包大小的最大體積"
# 假如最多是 5 ， 1,3,4 放得進去 ， 4 放進去之後剩下 1 ， 再來看 3 在 最多是 1 時能放多少 ， 然後 "4 放不進去時的最大體積" 跟 "這次計算結果" 中 比較大的就是 "當前背包大小的最大體積"
# 假如最多是 6 ， 1,3,4 放得進去 ， 4 放進去之後剩下 2 ， 再來看 3 在 最多是 2 時能放多少 ， 然後 "4 放不進去時的最大體積" 跟 "這次計算結果" 中 比較大的就是 "當前背包大小的最大體積"
# 假如最多是 7 ， 1,3,4 放得進去 ， 4 放進去之後剩下 3 ， 再來看 3 在 最多是 3 時能放多少 ， 然後 "4 放不進去時的最大體積" 跟 "這次計算結果" 中 比較大的就是 "當前背包大小的最大體積"
# 假如最多是 8 ， 1,3,4 放得進去 ， 4 放進去之後剩下 4 ， 再來看 3 在 最多是 4 時能放多少 ， 然後 "4 放不進去時的最大體積" 跟 "這次計算結果" 中 比較大的就是 "當前背包大小的最大體積"
# 重複的部分明顯 ， 為避免重複計算 ， 紀錄每個背包大小能裝的量 ， 然後直接拿出來

def backpack_dp( backpack, *arg ):
    
    # 紀錄每個背包大小能裝的量 的二維串列
    dp = [ [ 0 for i in range( backpack ) ] for j in range( len( arg ) ) ]
    
    for i in range( 1, len( arg ) ):    # i 為 每個東西的體積
        for j in range( 1, backpack ):  # j 為 背包的容量
            
            if j < arg[i]:  # 如果放不進去
                dp[i][j] = dp[i-1][j]   # 那就不要放
            else:   # 如果放得進去
                nohtyp = dp[i-1][j-arg[i]] + arg[i]    # "背包容量 減掉 這東西本身的體積" 之後能放的 加上 "這東西本身的體積"
                dp[i][j] = max( dp[i-1][j], nohtyp )   # 比較 nohtyp 跟 "當前背包大小的最大體積" ， 比較大的就是 "當前背包大小的最大體積"
    
    # 輸出結果
    print( dp[-1][-1] )

def test_backpack_dp():
    
    for i in [ [ 43, 5, 8, 46, 37, 20 ], [ 59, 12, 19, 33, 20, 10, 17, 11, 13 ], [ 88, 22, 14, 13, 2, 56, 60, 20 ], [ 29, 21, 25, 19, 1, 5, 23, 20, 27 ] ]:
        backpack_dp( i[0], *i[1:] )

test_backpack_dp()