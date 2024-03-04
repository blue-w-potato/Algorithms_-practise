#   鏈結串列
class linked_list():

    def __init__( self, val, next = None ): #   建立鏈結串列
        '''
        val can be everything
        next can be everthing, usually a linked_list
        '''
        if self is None:    #   除錯 
            return None
        
        self.val = val
        self.next = next

    def print_all( self , end = '\n' ):  #   說出所有值
        '''
        end can be any string
        '''
        if self is None:    #   除錯 
            return None
        if not type( end ) is str:    #   除錯 , end can be any string
            print( 'TypeError：', 'end have to be a string,', 'but end is ', type( end ) )
            return None
        
        if self.next is not None:
            print( self.val , end = end )
            self.next.print_all( end = end )
        else:
            print( self.val )

    def append( self, num ):   #   添加到最後
        '''
        num can be everything, without None.
        '''
        if self is None:    #   除錯 
            return None
        if num is None:    #   除錯 , num can be everything, witcout None
            print( 'TypeError： num can be everything, without None.' )
            return None
        
        if not self.next is None:   #   找到最後一個 
            self.next.append( num )
        else:
            self.next = num if type( num ) == linked_list else linked_list( num )   #   如果 num 是鏈結串列，不用動 num ; 如果 num 不是鏈結串列，就把它變鏈結串列

    def insert( self, num ): # 添加到最前
        '''
        num can be everything.
        '''
        return linked_list( num, self )
    
    def remove( self, num, key = None ):#   移除最左邊的某值
        '''
        num can be everything.
        '''
        if self is None:    # 如果 self 是 None，直接回傳
            return None
        
        if self.val == num: #如果找到了
            
            if key is None: #如果 self 是 第0個值
                return self.next    #直接回傳下一個
            
            else:
                key.next = self.next #如果 self 不是
                return key # 把上一個值和下一個接起來
            
        #   如果還沒找到
        self.next = self.next.remove( num )
        return self

nums = [ 1, 2, 3, 4, 5 ]

a = linked_list( 0 )

for num in nums:
    a.append( num )

for num in nums:
    a = a.insert( num )

a.print_all( end = '-' )

for num in nums:
    a = a.remove( num )
    a.print_all( end = '+' )

