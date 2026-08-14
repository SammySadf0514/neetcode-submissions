class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.left = None
        self.right = None
        self.size = 0

    def enqueue(self, val):
        newNode = Node(val)

        if self.right:
            self.right.next = newNode
            self.right = newNode
        else:
            self.left = self.right = newNode

        self.size += 1

    def dequeue(self):
        if not self.left:
            return None

        val = self.left.val
        self.left = self.left.next

        if not self.left:
            self.right = None

        self.size -= 1

        return val

class MyStack:

    def __init__(self):
        self.stack = Queue()
        

    def push(self, x: int) -> None:
        self.stack.enqueue(x)

        for i in range(self.stack.size - 1):
            val = self.stack.dequeue()
            self.stack.enqueue(val)   

    def pop(self) -> int:
        num = self.stack.dequeue()
        return num
        

    def top(self) -> int:
        return self.stack.left.val
        

    def empty(self) -> bool:
        if self.stack.size == 0:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()