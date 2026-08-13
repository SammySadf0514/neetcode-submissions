class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.head = None
        

    def get(self, index: int) -> int:
        curr = self.head
        for i in range(index):
            if curr is None:
                return -1
            curr = curr.next
        if curr is None:
            return -1
        
        return curr.val

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)

        if self.head is None:
            self.head = newNode
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            return
        
        if index == 0:
            self.addAtHead(val)
            return
        
        current = self.head
        for i in range(index - 1):
            if current is None:
                return
            current = current.next
            
            if current is None:
                return
        newNode = Node(val)
        newNode.next = current.next
        current.next = newNode
            

        

    def deleteAtIndex(self, index: int) -> None:
        if self.head is None:
            return False

        if index == 0:
            self.head = self.head.next
            return True
        
        current = self.head

        for i in range(index - 1):
            if current is None:
                return False
            current = current.next

        if current is None or current.next is None:
            return False

        current.next = current.next.next
        return True
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)