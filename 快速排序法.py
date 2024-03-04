def quick_sort( array, reverse = False ):
    if array is None:
        return array
    
    if len( array ) <= 1:
        return array
    
    num = array[0]
    
    big = []
    small = []
    
    array= array[1:]
    
    for i in array:
        if i > num:
            big.append( i )
        else:
            small.append( i )
    
    if reverse:
        return quick_sort( big, reverse=reverse ) + [num] + quick_sort( small, reverse=reverse )
    else:
        return quick_sort( small, reverse=reverse ) + [num] + quick_sort( big, reverse=reverse )
    
print( quick_sort( [ 5, 3, 1, 2, 4, 7, 8, 6, 9 ] ) )