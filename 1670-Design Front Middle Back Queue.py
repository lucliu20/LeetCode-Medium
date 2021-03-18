# https://leetcode.com/problems/design-front-middle-back-queue/

"""
Example 1:
Input:
["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle", "popMiddle", "popBack", "popFront"]
[[], [1], [2], [3], [4], [], [], [], [], []]
Output:
[null, null, null, null, null, 1, 3, 4, 2, -1]

Explanation:
FrontMiddleBackQueue q = new FrontMiddleBackQueue();
q.pushFront(1);   // [1]
q.pushBack(2);    // [1, 2]
q.pushMiddle(3);  // [1, 3, 2]
q.pushMiddle(4);  // [1, 4, 3, 2]
q.popFront();     // return 1 -> [4, 3, 2]
q.popMiddle();    // return 3 -> [4, 2]
q.popMiddle();    // return 4 -> [2]
q.popBack();      // return 2 -> []
q.popFront();     // return -1 -> [] (The queue is empty)
"""


import collections
class FrontMiddleBackQueue:

    def __init__(self):
        self.mq = collections.deque()

    def pushFront(self, val: int) -> None:
        self.mq.appendleft(val)

    def pushMiddle(self, val: int) -> None:
        self.mq.insert(len(self.mq)//2, val)

    def pushBack(self, val: int) -> None:
        self.mq.append(val)

    def popFront(self) -> int:
        return self.mq.popleft() if len(self.mq) else -1

    def popMiddle(self) -> int:
        if len(self.mq):
            i = (len(self.mq)-1)//2
            tmp = self.mq[i]
            self.mq.remove(tmp)
            return tmp
        return -1

    def popBack(self) -> int:
        return self.mq.pop() if len(self.mq) else -1




q = FrontMiddleBackQueue()
print(q.pushFront(1))    # [1]
print(q.pushBack(2))     # [1, 2]
print(q.pushMiddle(3))   # [1, 3, 2]
print(q.pushMiddle(4))   # [1, 4, 3, 2]
print(q.popFront())      # return 1 -> [4, 3, 2]
print(q.popMiddle())     # return 3 -> [4, 2]
print(q.popMiddle())     # return 4 -> [2]
print(q.popBack())       # return 2 -> []
print(q.popFront())      # return -1 -> [] (The queue is empty)

# Runtime: 76 ms, faster than 54.55% of Python3 online submissions for Design Front Middle Back Queue.
# Memory Usage: 15.1 MB, less than 30.30% of Python3 online submissions for Design Front Middle Back Queue.


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()

