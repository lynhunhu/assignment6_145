

class node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LList(object):
    def __init__(self):
        self._size = 0  # how many elements in the stack
        self._head = None  # the node chain starts here; initially empty
        self._tail = None

    def is_empty(self):
        """
        Purpose
            Checks if the given list has no data in it
        Return:
            :return True if the list has no data, or False otherwise
        """
        
        if self._head == None:
            return True
        
        if self._tail == None:
            return True
        
        if self.size == 0:
            return True
        
        else:
            return False


    def size(self):
        """
        Purpose
            Returns the number of data values in the given list
        Return:
            :return The number of data values in the list
        """
        
        return self._size
    

    def prepend(self, val):
        """
        Purpose
            Insert val at the front of the node chain
        Preconditions:
            :param val:   a value of any kind
        Post-conditions:
            The list increases in size.
            The new value is at index 0.
            The values previously in the list appear after the new value.
        Return:
            :return None
        """
        
        currentList = self._head
        
        newNode = node(val)
        
        newNode.next = currentList
        self._head = newNode

        self._size += 1
        
        if self._size == 1:
            self._tail = newNode
        return self._head

    def append(self, val):
        """
        Purpose
            Insert val at the end of the node chain
        Preconditions:
            :param val:   a value of any kind
        Post-conditions:
            The list increases in size.
            The new value is last in the list.
        Return:
            :return None
        """
        #currentHead = self._head
        
        #newHead = node(currentHead, val)

        #self._head = newHead

        #self._tail = node(val)
        if not self._tail is None:
            newNode = node(val)
            currentTail = self._tail
            currentTail.next = newNode
            self._tail = newNode
        # node chain rỗng
        
        if self._size == 0 or self._head is None or self._tail is None:
            newNode = node(val)
            self._tail = newNode
            self._head = newNode

        self._size +=1    

    def get_index_of_value(self, val):
        """
        Purpose
            Return the smallest index of the given val.
        Preconditions:
            :param val:   a value of any kind
        Post-conditions:
            none
        Return:
            :return True, idx if the val appears in self
            :return False, None if the vale does not appear in self
        """
        index = 0
        if self._size == 0:
            return (False, None)
        
        if self._size == 1:
            if self._head.data == val:
                return (True,index)
            
            if self._head.data != val:
                return (False,None)
        
        else:
            
            while self._head is not None:
                if self._head.data == val:
                    return (True, index)
                
                index += 1
                self._head = self._head.next

            return (False,None)
        

    
    def remove_from_front(self):
        """
        Purpose
            Removes and returns the first value 
        Post-conditions:
            The list decreases in size.
            The returned value is no longer in in the list.
        Return:
            :return The pair (True, value) if self is not empty
            :return The pair (False, None) if self is empty
        """
        if self._size == 0:
            return (False,None)
        
        if self._size == 1:
            temporary = self._head.data
            self._head = None
            self._tail = None
            self._size -= 1

            return (True, temporary)
        
        else:
            temporary = self._head.data
            self._head = self._head.next
            self._size -= 1

            return (True, temporary)
            
    def remove_from_back(self):
        """
        Purpose
            Removes and returns the last value
        Post-conditions:
            The list decreases in size.
            The returned value is no longer in in the list.
        Return:
            :return The pair True, value if self is not empty
            :return The pair False, None if self is empty
        """
        if self._size == 0:
            return (False,None)
        
        elif self._size == 1:
            temporary = self._head.data
            self._tail = None
            self._head = None
            self._size -= 1

            return (True, temporary)
        elif self._size == 2:
            temporary = self._head.next.data
            if self._head.next.next == None:
                self._head.next = None
                self._tail = self._head 
                self._size -=1

            return (True, temporary)

        else:
            temp = LList()
            temp = self._head
            temp._tail = self._tail
            while temp.next.next != None:
                temp = temp.next
                if temp.next.next is None:
                    temporary = temp.next
                    temp.next = None
                    self._size -= 1
                    return (True, temporary)
            return (False,None)
               

            # if self._tail.next == None:
            #     temporary = self._tail.data
            #     while self._head is not None:
            #         if self._head.next == None:
            #             self._tail.data = self._head.data
            #             self._size -= 1
            #         self._head = self._head.next
                
        
            # future_temp = LList()
            # while self._tail is not None:
            #     future_temp = self._tail
            #     if future_temp.next == None:
            #         return (True, future_temp)
                
            #     self._tail = self._tail.next
            
            
              

    def retrieve_data(self, idx):
        """
        Purpose
            Return the value stored at the index idx
        Preconditions:
            :param idx:   a non-negative integer
        Post-conditions:
            none
        Return:
            :return (True, val) if val is stored at index idx and idx is valid
            :return (False, None) if the idx is not valid for the list
        """
        count = 0

        if self._size == 0:
            return (False, None)
        
        if self._size == 1:
            if idx == count:
                return (True, self._head.data)
            else:
                return (False,None)
            
        else:
            while self._head is not None:
                if count == idx:
                    return (True, self._head.data)
                count += 1
                self._head = self._head.next
                
            
            return (False, None)


    def set_data(self, idx, val):
        """
        Purpose
            Store val at the index idx
        Preconditions:
            :param val:   a value of any kind
            :param idx:   a non-negative integer
        Post-conditions:
            The value stored at index idx changes to val
        Return:
            :return True if the index was valid, False otherwise
        """
        
        count = 0

        if self._size == 0:
            return False
        
        elif self._size == 1:
            if idx == count:
                self._head.data = val
                return True

            else:
                return False
            
        if self._size == 2:
            if idx == count:
                self._head.data = val
                return True
            
            if idx == 1:
                self._tail.data = val
                return True
            
            if idx > 1:
                return False
            
        
        else:
            temp = LList()
            temp._size = self._size
            temp._head = self._head
            temp._tail = self._tail
            flag = False

            while temp._head is not None:
                if idx == count:
                    temp._head.data = val
                    return True
                
                if idx != count and temp._head.next is None:
                    return flag
                count+=1
                temp._head = temp._head.next
     
            # while self._head is not None:

            #     if idx == count: 
            #         flag =True
            #         self._head.data = val

            #     temp.append(node(self._head.data))
            #     if self._head.next is None:
            #         temp._tail = self._head
            #     count +=1
            #     self._head = self._head.next

            # self._head = temp
            # self._tail = temp._tail
            # return flag



