# https://leetcode.com/problems/largest-values-from-labels/

"""
Example 1:
Input: values = [5,4,3,2,1], labels = [1,1,2,2,3], num_wanted = 3, use_limit = 1
Output: 9
Explanation: The subset chosen is the first, third, and fifth item.

Example 2:
Input: values = [5,4,3,2,1], labels = [1,3,3,3,2], num_wanted = 3, use_limit = 2
Output: 12
Explanation: The subset chosen is the first, second, and third item.

Example 3:
Input: values = [9,8,8,7,6], labels = [0,0,0,1,1], num_wanted = 3, use_limit = 1
Output: 16
Explanation: The subset chosen is the first and fourth item.

Example 4:
Input: values = [9,8,8,7,6], labels = [0,0,0,1,1], num_wanted = 3, use_limit = 2
Output: 24
Explanation: The subset chosen is the first, second, and fourth item.
"""

# values, labels, num_wanted, use_limit = [5,4,3,2,1], [1,1,2,2,3], 3, 1 # 9
# values, labels, num_wanted, use_limit = [5,4,3,2,1], [1,3,3,3,2], 3, 2 # 12
# values, labels, num_wanted, use_limit = [9,8,8,7,6], [0,0,0,1,1], 3, 1 # 16
# values, labels, num_wanted, use_limit = [9,8,8,7,6], [0,0,0,1,1], 3, 2 # 24
values, labels, num_wanted, use_limit = [4,7,4,6,3], [2,0,0,2,2], 1, 2

# Problem Explained
"""
Example: values = [5,4,3,2,1], labels = [1,1,2,2,3], num_wanted = 3, use_limit = 1

In this example, subset size <= 3 (as num_wanted = 3)
Listing members in each label
Label 1 -> [5,4]
Label 2 -> [3,2]
Label 3 -> [1]

Now from each label we can use only 1 element because use_limit for each label is 1.
The question asks us to find the largest possible sum of the subset, so we take from each label group, the largest element available.
So in this example,
from label 1 : we take 5,
from label 2: we take 3
from label 3: we take 1 (since label 1 has only one element)
5+3+1=9

Example
We can see in given example :
Input: values = [9,8,8,7,6], labels = [0,0,0,1,1], num_wanted = 3, use_limit = 1
Output: 16
Explanation: The subset chosen is the first and fourth item.
Listing members in each label
Label 0 -> [9,8,8]
Label 1 -> [7,6]
Here we are allowed to take 3 elements for the subset(num_wanted=3) but we cannot take more than two because the use limit for each label group is ONE(use_limit = 1) and there are only two label groups. Hence we take maximum element from each label group i.e. - 9+7 = 16

Example
Input: values = [5,4,3,2,1], labels = [1,3,3,3,2], num_wanted = 3, use_limit = 2
Output: 12
Listing members in each label
Label 1 -> [5]
Label 3 -> [4,3,2]
Label 2 -> [1]

Here use_limit is 2 hence we are allowed to take two elements from each label group,
Hence we take 5 from label 1 and [4, 3] from label 2 that satisfies our need for the subset of length <= 3
"""


from typing import List
import collections
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        md = collections.defaultdict(list)
        for i in range(len(labels)):
            md[labels[i]].append(values[i])
        res = []
        # Iterate the dict values, sort the values in descending order
        # Save the top "use_limit" number of elements to res array
        for values in md.values():
            values.sort(reverse=True)
            res.extend(values[:use_limit])
        # Sort the res array in decending order
        res.sort(reverse=True)
        return sum(res[:num_wanted])

solution = Solution()
print(solution.largestValsFromLabels(values, labels, num_wanted, use_limit))

# Runtime: 128 ms, faster than 96.33% of Python3 online submissions for Largest Values From Labels.
# Memory Usage: 18.2 MB, less than 93.67% of Python3 online submissions for Largest Values From Labels.

