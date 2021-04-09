# https://leetcode.com/problems/count-substrings-that-differ-by-one-character/
# My post:
# https://leetcode.com/problems/count-substrings-that-differ-by-one-character/discuss/1150651/Python-3-True-Brute-Force-Explained


"""
Example 1:
Input: s = "aba", t = "baba"
Output: 6
Explanation: The following are the pairs of substrings from s and t that differ by exactly 1 character:
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
The underlined portions are the substrings that are chosen from s and t.
​​
Example 2:
Input: s = "ab", t = "bb"
Output: 3
Explanation: The following are the pairs of substrings from s and t that differ by 1 character:
("ab", "bb")
("ab", "bb")
("ab", "bb")
​​​​The underlined portions are the substrings that are chosen from s and t.

Example 3:
Input: s = "a", t = "a"
Output: 0

Example 4:
Input: s = "abe", t = "bbc"
Output: 10
"""

# s, t = "aba", "baba"
# s, t = "ab", "bb"
# s, t = "a", "a"
s, t = "abe", "bbc"



class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        res = 0
        length_s, length_t = len(s), len(t)
        for i in range(1, length_s+1): # finding out all possbile substrings in "s" based on the "s" length.
            for j in range(length_s-i+1): # listing all possbile substrings in "s" with length been i.
                for k in range(length_t-i+1): # listing all possbile substrings in "t" with length been i.
                    # print("s:", s[j:j+i], "t:", t[k:k+i])
                    cnt = 0
                    for x, y in zip(s[j:j+i], t[k:k+i]):
                        if x != y:
                            cnt += 1
                        if cnt > 1:
                            break
                    if cnt <= 1 and cnt != 0:
                        res += 1
        return res


solution = Solution()
print(solution.countSubstrings(s, t))

# Runtime: 1240 ms, faster than 15.64% of Python3 online submissions for Count Substrings That Differ by One Character.
# Memory Usage: 14 MB, less than 96.92% of Python3 online submissions for Count Substrings That Differ by One Character.
