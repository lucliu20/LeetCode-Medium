# https://leetcode.com/problems/open-the-lock/

"""
Example 1:
Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".

Example 2:
Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation:
We can turn the last wheel in reverse to move from "0000" -> "0009".

Example 3:
Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation:
We can't reach the target without getting stuck.

Example 4:
Input: deadends = ["0000"], target = "8888"
Output: -1
"""


deadends, target = ["0201","0101","0102","1212","2002"], "0202"
# deadends, target = ["8888"], "0009"
# deadends, target = ["8887","8889","8878","8898","8788","8988","7888","9888"], "8888"
# deadends, target = ["0000"], "8888"

# Refer to the post:
# https://leetcode.com/problems/open-the-lock/discuss/110232/Accepted-PythonJava-BFS-%2B-how-to-avoid-TLE
# From one of the comments
import collections
# class Solution:
#     def openLock(self, deadends: list(), target: str) -> int:
#         # Concept - You need to think this as a graph and once that is visualized, the problem just
#         # Translates to finding a shortest path from source ('0000') to destination (target)
#         # that also incorporates the constraints (deadends)
#         
#         # For constant Lookups and avoiding TLE
#         deadends = set(deadends)
#         # For checking visited nodes
#         seen = set()
#         # Start point
#         seen.add('0000')
#         # Put it in queue
#         q = collections.deque(['0000'])
#         # Our final result aka shortest path
#         minSteps = 0
#         
#         while q:
#             size = len(q)
#             
#             for i in range(size):
#                 lockPos = q.popleft()
#                 # We should continue in case of deadends
#                 if lockPos in deadends:
#                     continue
#                 # If you have reached the target in thuis process, return from here only 
#                 if lockPos == target:
#                     return minSteps
#                 
#                 temp = lockPos
#                 # Else make the other 2 strings(nodes) that are possible by adding or subtracting 1
#                 for i in range(4):
#                     curPos = int(temp[i])
#                     s1 = temp[0:i] + ('0' if curPos == 9 else str((curPos + 1)%10)) + temp[i+1:]
#                     s2 = temp[0:i] + ('9' if curPos == 0 else str((curPos - 1)%10)) + temp[i+1:]
#                     
#                     # Only add this into queue once you verify the constraints
#                     if s1 not in seen and s1 not in deadends:
#                         seen.add(s1)
#                         q.append(s1)
#                     
#                     if s2 not in seen and s2 not in deadends:
#                         seen.add(s2)
#                         q.append(s2)
#             # Add 1 to steps to go to the next level as we were not able to find target in this level            
#             minSteps += 1
#         return -1

class Solution:
    def openLock(self, deadends: list(), target: str) -> int:
        res = 0
        deadends = set(deadends)
        q = collections.deque(["0000"])
        v = set()
        while q:
            l = len(q)
            for _ in range(l):
                curState = q.popleft()
                if curState == target:
                    return res
                if curState in deadends:
                    continue
                for i in range(4):
                    p = int(curState[i])
                    # print(curState[0:i], curState[i+1:])
                    # print results when i = 0
                    #  000
                    # 0 00
                    # 00 0
                    # 000
                    s1 = curState[0:i] + ("0" if p == 9 else str((p+1)%10)) + curState[i+1:]
                    s2 = curState[0:i] + ("9" if p == 0 else str((p-1)%10)) + curState[i+1:]
                    if s1 not in deadends and s1 not in v:
                        q.append(s1)
                        v.add(s1)
                    if s2 not in deadends and s2 not in v:
                        q.append(s2)
                        v.add(s2)
            res += 1
        return -1

solution = Solution()
print(solution.openLock(deadends, target))

# Runtime: 564 ms, faster than 73.54% of Python3 online submissions for Open the Lock.
# Memory Usage: 15.6 MB, less than 38.72% of Python3 online submissions for Open the Lock.

