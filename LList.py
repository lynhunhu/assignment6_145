#Name: Nhu Nhu Ly
#NSID: cvd326
#instructor's name: Eric Neufeld
#student number: 11333935
#course number: 27177
#lab section: Monday 1:30 - 2:50 - 28623


class node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LList(object):
    def __init__(self):
        self._size = 0 
        self._head = None  
        self._tail = None

    def is_empty(self):
        
        if self._head == None:
            return True
        
        if self._tail == None:
            return True
        
        if self.size == 0:
            return True
        
        else:
            return False


    def size(self):
        return self._size
    

    def prepend(self, val):
        currentList = self._head
        
        newNode = node(val)
        
        newNode.next = currentList
        self._head = newNode

        self._size += 1
        
        if self._size == 1:
            self._tail = newNode
        return self._head

    def append(self, val):
        if not self._tail is None:
            newNode = node(val)
            currentTail = self._tail
            currentTail.next = newNode
            self._tail = newNode

        if self._size == 0 or self._head is None or self._tail is None:
            newNode = node(val)
            self._tail = newNode
            self._head = newNode

        self._size +=1    

    def get_index_of_value(self, val):
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

    def retrieve_data(self, idx):
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
     