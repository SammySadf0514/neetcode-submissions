class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.nums = [0] * capacity

    def get(self, i: int) -> int:
        return self.nums[i]

    def set(self, i: int, n: int) -> None:
        self.nums[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.nums[self.length] = n
        self.length += 1

    def popback(self) -> int:
        self.length -= 1
        return self.nums[self.length]
 

    def resize(self) -> None:
        self.capacity *= 2
        new_nums = [0] * self.capacity
        for i in range(self.length):
            new_nums[i] = self.nums[i]
        self.nums = new_nums

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity