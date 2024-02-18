def binary_search_1( array, key ):
    l = len(array)

    if l == 0:
        return None
    if l == 1:
        if array[0] == key:
            return True
        return False

    '''
    print(f'array is {array}')
    print()
    print(f'key is {key}')
    print()
    '''
    
    search = array[ l//2 ]

    '''
    print(f'search {search}')
    print()
    '''

    if search == key:
        return True
    if search < key:
        return binary_search_1(
             array[ l//2 + 1: ], key )
    return binary_search_1( array[ :l//2 ], key )

def test_1():
    array = [
        [ i for i in range( 0, 100 ) ],     #True
        [ i*2 for i in range( 0, 100 ) ],   #False
        [ i**2 for i in range( 0, 100 ) ]   #True
    ]
    for i in range(3):
        print( binary_search_1( array[i], 9 ) )

#test_1()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def binary_search_2( array, high, low, key ):
    if len(array) == 0:
        return None
    
    '''
    print(f'height = {heigh}')
    print(f'low = {low}')

    '''
    l = high - low
    if l == 0:
        if array[low] == key:
            return low
        return False
    
    '''
    print(f'array is {array}')
    print()
    print(f'key is {key}')
    print()
    '''

    find = (high + low)//2
    search = array[ find ]

    '''
    print(f'search {find}, {search}')
    print()
    '''

    if search == key:
        return find
    if search < key:
        return binary_search_2(
            array, high, find+1, key )
    return binary_search_2( array, find-1, low, key )

def test_2():
    array = [
        [ i for i in range( 0, 100 ) ],     #9
        [ i*2 for i in range( 0, 100 ) ],   #False
        [ i**2 for i in range( 0, 100 ) ]   #3
    ]
    for i in range(3):
        print( binary_search_2( array[i], 99, 0, 9 ) )

test_2()

