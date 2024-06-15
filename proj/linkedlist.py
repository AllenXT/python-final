class ListNode:
    """
    ListNode class is used to represent each node in the linked list
    
    Attributes:
    key: the key of the node
    value: the value of the node
    next: the next node pointed to
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    """
    LinkedList class is used to represent a linked list
    
    Attributes:
    head: the head node of the linked list
    
    methods:
    insert(): insert a new node to the linked list
    find(): find a node in the linked list
    delete(): delete a node from the linked list
    """
    def __init__(self):
        self.head = None
      
        
    def insert(self, key, value):
        # insert to the front of the list
        newNode = ListNode(key, value)
        newNode.next = self.head
        self.head = newNode
    
    
    def find(self, key):
        curr = self.head
        while curr:
            if curr.key == key:
                return curr
            curr = curr.next
        return None
    
    
    def delete(self, key):
        curr = self.head
        prev = None
        while curr:
            if curr.key == key:
                if prev: # more than one node
                    prev.next = curr.next
                    curr.next = None
                else: # only one node
                    self.head = None
                return True
            prev = curr
            curr = curr.next
        return False