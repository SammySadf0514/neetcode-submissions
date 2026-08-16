class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    def isEmpty(self) -> bool:
        if self.head is None or self.tail is None:
            return True
        return False
        

    def append(self, value: int) -> None:
        newNode = Node(value)

        if self.tail is None:
            self.head = self.tail = newNode
            return

        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode
        

    def appendleft(self, value: int) -> None:
        newNode = Node(value)

        if self.head is None:
            self.head = self.tail = newNode
            return

        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
        

    def pop(self) -> int:
        if self.head is None or self.tail is None:
            return -1
        current = self.tail
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        return current.value



    def popleft(self) -> int:
        if self.head is None or self.tail is None:
            return -1
        current = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        return current.value
        
