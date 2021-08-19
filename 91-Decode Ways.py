# https://leetcode.com/problems/decode-ways/

"""
Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:
Input: s = "0"
Output: 0
Explanation: There is no character that is mapped to a number starting with 0.
The only valid mappings with 0 are 'J' -> "10" and 'T' -> "20", neither of which start with 0.
Hence, there are no valid ways to decode this since all digits need to be mapped.

Example 4:
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
"""


# s = "12" # 2
# s = "226" # 3
# s = "0" # 0
# s = "06" # 0
# s = "3301213" # 0
# s = "2222315" # 16
# s = "315214916" # 12
# s = "3105213" # 3
s = "27" # 1

# Test case: #228
# s = "2101" # 1
# s = "22101" # 2
# Test case: #235
# s = "227" # 2
# Test case: #228
# s = "2611055971756562" # 4



# DP
# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s)
        for i in range(len(s)):
            if i == 0:
                if s[i] == "0":
                    return 0
                else:
                    dp[i] = 1
            else:
                if int(s[i-1]) > 2 and s[i] == "0":
                    return 0
                if s[i-1] == "0" and s[i] == "0":
                    return 0
                if int(s[i-1]) > 2 and int(s[i]) > 0:
                    dp[i] = dp[i-1]
                elif (s[i-1] == "2" or s[i-1] == "1") and s[i] == "0":
                    dp[i] = dp[i-1]
                elif i == 1:
                    if int(s[i-1]) > 1 and int(s[i]) > 6:
                        dp[i] = dp[i-1]
                    elif (i+1) in range(len(s)) and s[i+1] == "0":
                        dp[i] = dp[i-1]
                    else:
                        dp[i] = dp[i-1] + 1
                elif s[i-1] == "0":
                    dp[i] = dp[i-1]
                elif (i+1) in range(len(s)) and s[i+1] == "0":
                    dp[i] = dp[i-1]
                elif int(s[i-1]) > 1 and int(s[i]) > 6:
                    dp[i] = dp[i-1]
                else:
                    dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]


# Runtime: 28 ms, faster than 88.01% of Python3 online submissions for Decode Ways.
# Memory Usage: 14.4 MB, less than 21.83% of Python3 online submissions for Decode Ways.


solution = Solution()
print(solution.numDecodings(s))

