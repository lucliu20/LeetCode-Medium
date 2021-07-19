# https://leetcode.com/problems/queue-reconstruction-by-height/

"""
Example 1:
Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
Explanation:
Person 0 has height 5 with no other people taller or the same height in front.
Person 1 has height 7 with no other people taller or the same height in front.
Person 2 has height 5 with two persons taller or the same height in front, which is person 0 and 1.
Person 3 has height 6 with one person taller or the same height in front, which is person 1.
Person 4 has height 4 with four people taller or the same height in front, which are people 0, 1, 2, and 3.
Person 5 has height 7 with one person taller or the same height in front, which is person 1.
Hence [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] is the reconstructed queue.

Example 2:
Input: people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
"""


people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
# people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]


from typing import List
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = []
        people = sorted(people, key = lambda x: (-x[0], x[1]))
        for p in people:
            res.insert(p[1], p)
        return res


# Runtime: 92 ms, faster than 89.10% of Python3 online submissions for Queue Reconstruction by Height.
# Memory Usage: 14.8 MB, less than 84.00% of Python3 online submissions for Queue Reconstruction by Height.



solution = Solution()
print(solution.reconstructQueue(people))

