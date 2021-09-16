# https://leetcode.com/problems/longest-turbulent-subarray/

"""
Example 1:
Input: arr = [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]

Example 2:
Input: arr = [4,8,12,16]
Output: 2

Example 3:
Input: arr = [100]
Output: 1
"""


arr = [9,4,2,10,7,8,8,1,9]
# arr = [4,8,12,16]
# arr = [100]
# arr = [0,8,45,88,48,68,28,55,17,24] # Expected: 8



from typing import List
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res, tmp, flip = 1, 1, "undefined"
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                if flip == "undefined":
                    flip = "positive"
                    tmp += 1
                elif flip == "positive":
                    res = max(res, tmp)
                    tmp = 2
                elif flip == "negagive":
                    flip = "positive"
                    tmp += 1
            elif arr[i] < arr[i-1]:
                if flip == "undefined":
                    flip = "negagive"
                    tmp += 1
                elif flip == "negagive":
                    res = max(res, tmp)
                    tmp = 2
                elif flip == "positive":
                    flip = "negagive"
                    tmp += 1
            elif arr[i] == arr[i-1]:
                res = max(res, tmp)
                flip = "undefined"
                tmp = 1
        res = max(res, tmp)
        return res


# Runtime: 460 ms, faster than 92.17% of Python3 online submissions for Longest Turbulent Subarray.
# Memory Usage: 18.4 MB, less than 87.99% of Python3 online submissions for Longest Turbulent Subarray.



# DP iteratively
# Refer to the LeetCode post:
# https://leetcode.com/problems/longest-turbulent-subarray/discuss/222511/DP-Thinking-Process-(Java)
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        dp = [[0 for _ in range(2)] for _ in range(len(arr))]
        res = 0
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                dp[i][1] = dp[i-1][0] + 1
                res = max(res, dp[i][1])
            elif arr[i] < arr[i-1]:
                dp[i][0] = dp[i-1][1] + 1
                res = max(res, dp[i][0])
        return res + 1

# Runtime: 1031 ms, faster than 5.22% of Python3 online submissions for Longest Turbulent Subarray.
# Memory Usage: 19.8 MB, less than 8.62% of Python3 online submissions for Longest Turbulent Subarray.



solution = Solution()
print(solution.maxTurbulenceSize(arr))
