# https://leetcode.com/problems/design-linked-list/
"""
Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3
"""

"""
Example 2:
["MyLinkedList","addAtHead","addAtHead","addAtHead","addAtIndex","deleteAtIndex","addAtHead","addAtTail","get","addAtHead","addAtIndex","addAtHead"]
[[],[7],[2],[1],[3,0],[2],[6],[4],[4],[4],[5,0],[6]]

Example 3:
["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
[[],[1],[3],[1,2],[1],[0],[0]]

Example 4:
["MyLinkedList","addAtIndex","addAtIndex","addAtIndex","get"]
[[],[0,10],[0,20],[1,30],[0]]

Example: 5
["MyLinkedList","addAtTail","get"]
[[],[1],[0]]
"""

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.len = 0
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.len: return -1
        currentNode = self.head
        ind = 0
        while ind < self.len:
            if ind == index:
                return currentNode.value
            currentNode = currentNode.nextNode
            ind += 1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = linkedListNode(val)
        currentNode = self.head
        self.head = node
        node.nextNode = currentNode
        self.len += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = linkedListNode(val)
        if not self.head:
            self.head = node
        else:
            currentNode = self.head
            while True:
                if currentNode.nextNode is None:
                    currentNode.nextNode = node
                    break
                currentNode = currentNode.nextNode
        self.len += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.len:
            return
        elif index == 0:
            self.addAtHead(val)
        elif index == self.len:
            self.addAtTail(val)
        else:
            node = linkedListNode(val)
            currentNode = self.head
            ind = 0
            while ind < index:
                if ind == index-1:
                    node.nextNode = currentNode.nextNode
                    currentNode.nextNode = node
                    break
                currentNode = currentNode.nextNode
                ind += 1
            self.len += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.len: return -1
        currentNode = self.head
        ind = 0
        while ind < self.len:
            if index == 0:
                self.head = currentNode.nextNode
                break
            if ind == index-1:
                if ind == self.len-2:
                    currentNode.nextNode = None
                else:
                    currentNode.nextNode = currentNode.nextNode.nextNode
                break
            currentNode = currentNode.nextNode
            ind += 1
        self.len -= 1

class linkedListNode:
    def __init__(self, value, nextNode = None):
        self.value = value
        self.nextNode = nextNode

# Runtime: 380 ms
# Memory Usage: 15.4 MB

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1, 2) # 1->2->3
print(obj.get(1)) # return 2
obj.deleteAtIndex(1) # becomes 1->3
print(obj.get(1)) # return 3

# Example 2:
# obj = MyLinkedList()
# obj.addAtHead(7)
# obj.addAtHead(2)
# obj.addAtHead(1)
# obj.addAtIndex(3, 0) # 1->2->7->0
# obj.deleteAtIndex(2) # becomes 1->2->0
# obj.addAtHead(6) # becomes 6->1->2->0
# obj.addAtTail(4) # becomes 6->1->2->0->4
# print(obj.get(4)) # return 4
# obj.addAtHead(4) # becomes 4->6->1->2->0->4
# obj.addAtIndex(5, 0) # becomes 4->6->1->2->0->0->4
# obj.addAtHead(6) # becomes 6->4->6->1->2->0->0->4

# Example 3:
# obj = MyLinkedList()
# obj.addAtHead(1)
# obj.addAtTail(3)
# obj.addAtIndex(1, 2) # 1->2->3
# print(obj.get(1)) # return 2
# obj.deleteAtIndex(0) # 2->3
# print(obj.get(0)) # return 2

# Example 4:
# obj = MyLinkedList()
# obj.addAtIndex(0, 10)
# obj.addAtIndex(0, 20) 
# obj.addAtIndex(1, 30) 
# print(obj.get(0))

# Example 5:
# obj = MyLinkedList()
# obj.addAtTail(1)
# print(obj.get(0))
# pass