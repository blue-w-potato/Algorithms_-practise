def search_sort( array, reverse = False ):
    if array is None:
        return None
    
    if len( array ) < 2:
        return array
    
    if reverse:
        search_num = max( array )
    else:
        search_num = min( array )
    
    array.remove( search_num )
    
    return [search_num] + search_sort( array , reverse = reverse)

print(search_sort( [ 5, 6, 3, 2, 7, 8, 4 ,9 ,1 ] , reverse = True ))