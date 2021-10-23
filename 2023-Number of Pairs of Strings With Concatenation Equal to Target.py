# https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/

"""
Example 1:
Input: nums = ["777","7","77","77"], target = "7777"
Output: 4
Explanation: Valid pairs are:
- (0, 1): "777" + "7"
- (1, 0): "7" + "777"
- (2, 3): "77" + "77"
- (3, 2): "77" + "77"

Example 2:
Input: nums = ["123","4","12","34"], target = "1234"
Output: 2
Explanation: Valid pairs are:
- (0, 1): "123" + "4"
- (2, 3): "12" + "34"

Example 3:
Input: nums = ["1","1","1"], target = "11"
Output: 6
Explanation: Valid pairs are:
- (0, 1): "1" + "1"
- (1, 0): "1" + "1"
- (0, 2): "1" + "1"
- (2, 0): "1" + "1"
- (1, 2): "1" + "1"
- (2, 1): "1" + "1"
"""


nums, target = ["777","7","77","77"], "7777"
# nums, target = ["123","4","12","34"], "1234"
# nums, target = ["1","1","1"], "11"


from typing import List
import collections
class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        mydict = collections.Counter(nums)
        res = 0
        for k, v in mydict.items():
            if target.startswith(k):
                suffix = target[len(k):]
                res += v * mydict[suffix]
                if suffix == k:
                    res -= mydict[suffix]
        return res

# Runtime: 56 ms, faster than 77.66% of Python3 online submissions for Number of Pairs of Strings With Concatenation Equal to Target.
# Memory Usage: 14.3 MB, less than 59.58% of Python3 online submissions for Number of Pairs of Strings With Concatenation Equal to Target.


# Refer to LeetCode post:
# https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/discuss/1499081/JavaPython-3-One-pass-O(NM)-HashTable-codes-w-analysis.
class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        prefix, suffix = collections.Counter(), collections.Counter()
        res = 0
        for n in nums:
            if target.startswith(n):
                res += suffix[len(target) - len(n)]
            if target.endswith(n):
                res += prefix[len(target) - len(n)]
            if target.startswith(n):
                prefix[len(n)] += 1
            if target.endswith(n):
                suffix[len(n)] += 1
        return res


# Runtime: 36 ms, faster than 97.28% of Python3 online submissions for Number of Pairs of Strings With Concatenation Equal to Target.
# Memory Usage: 14.5 MB, less than 30.15% of Python3 online submissions for Number of Pairs of Strings With Concatenation Equal to Target.


solution = Solution()
print(solution.numOfPairs(nums, target))
