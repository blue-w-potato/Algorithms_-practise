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
        