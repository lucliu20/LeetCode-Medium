# https://leetcode.com/problems/insert-delete-getrandom-o1/
# My post:
# https://leetcode.com/problems/insert-delete-getrandom-o1/discuss/1045488/Python-3-using-defaultdict-default_factory-attribute-explained


"""
Example 1:
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
"""

import collections
import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.pos = collections.defaultdict()
        self.pos.default_factory = self.pos.__len__

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.pos:
            self.arr.append(val)
            self.pos[val]
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.pos:
            return False
        else:
            indx = self.pos[val]
            last = self.arr[-1]
            self.arr[-1], self.arr[indx] = self.arr[indx], self.arr[-1]
            self.arr.pop()
            self.pos[last] = indx
            self.pos.pop(val)
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        indice = random.randrange(0, len(self.pos)) # Stop point of the range. This parameter is mandatory. This would be excluded from the range.
        return self.arr[indice]

        
randomizedSet = RandomizedSet()
print(randomizedSet.insert(1)) # Inserts 1 to the set. Returns true as 1 was inserted successfully.
print(randomizedSet.remove(2)) # Returns false as 2 does not exist in the set.
print(randomizedSet.insert(2)) # Inserts 2 to the set, returns true. Set now contains [1,2].
print(randomizedSet.getRandom()) # getRandom() should return either 1 or 2 randomly.
print(randomizedSet.remove(1)) # Removes 1 from the set, returns true. Set now contains [2].
print(randomizedSet.insert(2)) # 2 was already in the set, so return false.
print(randomizedSet.getRandom()) # Since 2 is the only number in the set, getRandom() will always return 2.


# Runtime: 96 ms, faster than 76.39% of Python3 online submissions for Insert Delete GetRandom O(1).
# Memory Usage: 18.5 MB, less than 28.76% of Python3 online submissions for Insert Delete GetRandom O(1).


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()