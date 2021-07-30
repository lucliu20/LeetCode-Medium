# https://leetcode.com/problems/map-sum-pairs/

"""
Example 1:
Input
["MapSum", "insert", "sum", "insert", "sum"]
[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
Output
[null, null, 3, null, 5]

Explanation
MapSum mapSum = new MapSum();
mapSum.insert("apple", 3);  
mapSum.sum("ap");           // return 3 (apple = 3)
mapSum.insert("app", 2);    
mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)
"""



# Brute Force
# Use built-in function str.startswith()
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = dict()

    def insert(self, key: str, val: int) -> None:
        self.map[key] = val

    def sum(self, prefix: str) -> int:
        res = 0
        for k, v in self.map.items():
            if k.startswith(prefix):
                res += v
        return res



mapSum = MapSum()
mapSum.insert("apple", 3)
print(mapSum.sum("ap"))           # return 3 (apple = 3)
mapSum.insert("app", 2)
print(mapSum.sum("ap"))           # return 5 (apple + app = 3 + 2 = 5)
pass


# Runtime: 28 ms, faster than 88.40% of Python3 online submissions for Map Sum Pairs.
# Memory Usage: 14.3 MB, less than 80.27% of Python3 online submissions for Map Sum Pairs.


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)