# https://leetcode.com/problems/design-circular-queue/

"""
Example 1:

Input
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 3, true, true, true, 4]

Explanation
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4
"""

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.queue = [None]*self.k
        self.head = -1
        self.tail = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.tail == -1:
            self.head = 0
        self.tail = (self.tail+1)%self.k
        self.queue[self.tail] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.head == self.tail:
            self.__init__(self.k)
        else:
            self.head = (self.head+1)%self.k
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        if self.head == self.tail == -1:
            return True
        return False

    def isFull(self) -> bool:
        if (self.tail+1)%self.k == self.head:
            return True
        return False

myCircularQueue = MyCircularQueue(3) # retrun None
print(myCircularQueue.enQueue(1)) # return True
print(myCircularQueue.enQueue(2)) # return True
print(myCircularQueue.enQueue(3)) # return True
print(myCircularQueue.enQueue(4)) # return False
print(myCircularQueue.Rear())     # return 3
print(myCircularQueue.isFull())   # return True
print(myCircularQueue.deQueue())  # return True
print(myCircularQueue.enQueue(4)) # return True
print(myCircularQueue.Rear())     # return 4

"""
["MyCircularQueue","enQueue","Rear","Rear","deQueue","enQueue","Rear","deQueue","Front","deQueue","deQueue","deQueue"]
[[6],[6],[],[],[],[5],[],[],[],[],[],[]]
"""
# myCircularQueue = MyCircularQueue(6) # retrun None
# print(myCircularQueue.enQueue(6)) # return True
# print(myCircularQueue.Rear())     # return 6
# print(myCircularQueue.Rear())     # return 6
# print(myCircularQueue.deQueue())  # return True
# print(myCircularQueue.enQueue(5)) # return True
# print(myCircularQueue.Rear())     # return 5
# print(myCircularQueue.deQueue())  # return True
# print(myCircularQueue.Front())    # return -1
# print(myCircularQueue.deQueue())  # return False
# print(myCircularQueue.deQueue())  # return False
# print(myCircularQueue.deQueue())  # return False

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()


# Runtime: 68 ms, faster than 74.04% of Python3 online submissions for Design Circular Queue.
# Memory Usage: 15 MB, less than 26.07% of Python3 online submissions for Design Circular Queue.
