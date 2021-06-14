# https://leetcode.com/problems/task-scheduler/

"""
Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.

Example 2:
Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.

Example 3:
Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
"""


# tasks, n = ["A","A","A","B","B","B"], 2
# tasks, n = ["A","A","A","B","B","B"], 0
# tasks, n = ["A","A","A","A","A","A","B","C","D","E","F","G"], 2
tasks, n = ["A","A","A","B","B","B","C","C","C","D","D","E"], 2 # expected: 12



# Sorted
from typing import List
import collections
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mydict = collections.Counter(tasks)
        s = {k:v for k, v in sorted(mydict.items(), key=lambda item: item[1], reverse=True)}
        res = 0
        executed = 0
        while len(s) > 0:
            i = 0
            for key, _ in s.items():
                s[key] -= 1
                i += 1
                executed += 1
                res += 1
                if i == n+1:
                    break
                elif executed == len(tasks):
                    break
                elif i == len(s):
                    res += n-i+1
                    break
            s = {k:v for k,v in s.items() if v!=0} # deleting dict key&value pair while iterating
            s = {k:v for k, v in sorted(s.items(), key=lambda item: item[1], reverse=True)}

        return res


# Runtime: 572 ms, faster than 29.25% of Python3 online submissions for Task Scheduler.
# Memory Usage: 14.5 MB, less than 89.05% of Python3 online submissions for Task Scheduler.


solution = Solution()
print(solution.leastInterval(tasks, n))


