# https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/


"""
Example 1:
Input: s = "1234"
Output: false
Explanation: There is no valid way to split s.

Example 2:
Input: s = "050043"
Output: true
Explanation: s can be split into ["05", "004", "3"] with numerical values [5,4,3].
The values are in descending order with adjacent values differing by 1.

Example 3:
Input: s = "9080701"
Output: false
Explanation: There is no valid way to split s.

Example 4:
Input: s = "10009998"
Output: true
Explanation: s can be split into ["100", "099", "98"] with numerical values [100,99,98].
The values are in descending order with adjacent values differing by 1.
"""


s = "1234"
# s = "050043"
# s = "9080701"
# s = "10009998"
# s = "5"
# s = "01"
# s = "10"
# s = "3202872336" # False



class Solution:
    def splitString(self, s: str) -> bool:
        if len(s) < 2: return False
        for i in range(len(s)):
            curr = int(s[:i+1])
            if curr == 0:
                continue
            cnt = 0
            q = curr
            while q > 0: # find out how many digits there are
                if q//10 != 0:
                    q //=10
                    cnt += 1
                else:
                    cnt += 1
                    break
            j = i+1
            tmp = ""
            myset = set()
            while j < len(s):
                if tmp == "" and s[j] == "0":
                    if curr == 1: # case: "10"
                        myset.add(1)
                        if len(s)-1 == j:
                            return True
                    j += 1
                else:
                    tmp += s[j]
                    if len(tmp) < cnt:
                        number = int(tmp) # case: "10099"
                        if number == curr-1:
                            myset.add(1)
                            j += 1
                            tmp = ""
                            curr = number
                        else:
                            j += 1
                    else:
                        number = int(tmp) # case: "4847"
                        if number == curr-1:
                            myset.add(1)
                            j += 1
                            tmp = ""
                            curr = number
                        else:
                            myset.add((number-(curr-1)))
                            break
            if len(myset) == 1 and 1 in myset and len(s) == j:
                return True
        return False


# 173 / 173 test cases passed.
# Status: Accepted
# Runtime: 36 ms
# Memory Usage: 14.3 MB

solution = Solution()
print(solution.splitString(s))
