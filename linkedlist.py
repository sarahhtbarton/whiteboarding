
class Node:
    """Node in a Linked List"""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Linked List w/head and tail"""

    def __init__(self):
        self.head = None
        self.tail = None
    
    def print_list(self):
        """Traverse and print nodes"""

        current = self.head

        while current is not None:
            print(current.data)
            current = current.next
    
    def data_in_list(self, data):
        """Find if data exists in list"""

        current = self.head

        while current.next is not None:
            if current.data == data:
                return True
            
            current = current.next
        
        return False

    def append_to_end(self, data):
        """Append new node to end of linked list"""

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        
        if self.tail is not None:
            self.tail.next = new_node
        
        self.tail = new_node
    
    def remove_node_by_data(self, data):
        """Remove a node by data"""

        if self.head is None:
            self.tail is None
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        current = self.head
        
        while current.next is not None: #goes till reaches the second to last node
            if current.next.data == data: #if the tail is the one you wnat to delete
                current.next = current.next.next #have next skip the tail, so current.next will equal None

                #if you did in fact delete the tail, then current.next is None, you have to set the tail to the current node
                if current.next is None:
                    self.tail = current
                return

            current = current.next








    

