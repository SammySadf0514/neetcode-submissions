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


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        studentQueue = Queue()

        for student in students:
            studentQueue.enqueue(student)

        sandwichIndex = 0
        count = 0

        while count < studentQueue.size:
            student = studentQueue.dequeue()
            if student != sandwiches[sandwichIndex]:
                studentQueue.enqueue(student)
                count += 1
            else:
                sandwichIndex += 1
                count = 0

        return count



        
            