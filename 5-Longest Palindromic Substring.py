# https://leetcode.com/problems/longest-palindromic-substring/


"""
Example 1:
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Example 3:
Input: s = "a"
Output: "a"

Example 4:
Input: s = "ac"
Output: "a"
"""

# s = "babad"
# s = "baabd"
# s = "baaab"
# s = "aaa"
s = "cbbd"
# s = "a"
# s = "ac"

# Test case # 174
# Runtime: 156 ms
# s = "jaliztdispcppzgzjxnjxwbhhtbjrijyibqwrhwuscmokylygielwssuyretqnoiglvsltmhetvdoliwibrnwmdtauczcswuqxxokaykslfzgxovphdptgtrbbozdkdgawcegemkumgbyqzjrzurkdaibfwwvcxfcstvixisrcfxvnlzizlbnacxssetlsxrvcaqvzmbnzdfmtskmxmjblzgpdsjvhqhrihiajvwxbmjsncjhmilercbdbzyncrnlyrxrefaeuttkscfttqnedzvqisclbremuxmngrpgqjqkijpizkixkrgaarpknivrrirbkeddkulvlfuetbdnugzodbfufqhrpkyufhrhnnnzsenkvqsuhlbaimniusuxsnmavqbilzgsfxjykrxdkkpnneikwlucdghnikojythrpgwyzoqgraycavrivsbfuaonssmryhcykooivrxmeeowllsfeyxrznvkdpobohpzolnpbxjjxbpnlozphobopdkvnzrxyefsllwoeemxrviookychyrmssnoaufbsvirvacyargqozywgprhtyjokinhgdculwkiennpkkdxrkyjxfsgzlibqvamnsxusuinmiablhusqvknesznnnhrhfuykprhqfufbdozgundbteuflvlukddekbrirrvinkpraagrkxikzipjikqjqgprgnmxumerblcsiqvzdenqttfcskttueaferxrylnrcnyzbdbcrelimhjcnsjmbxwvjaihirhqhvjsdpgzlbjmxmkstmfdznbmzvqacvrxsltessxcanblzizlnvxfcrsixivtscfxcvwwfbiadkruzrjzqybgmukmegecwagdkdzobbrtgtpdhpvoxgzflskyakoxxquwsczcuatdmwnrbiwilodvtehmtlsvlgionqteryusswleigylykomcsuwhrwqbiyjirjbthhbwxjnxjzgzppcpsidtzilaj"




# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
#         res = s[-1]
#         for j in range(len(s)):
#             dp[0][j] = 1
# 
#         for j in range(1, len(s)):
#             if s[j] == s[j-1]:
#                 dp[1][j] = 1
#                 res = s[j-1]+s[j]
#         
#         for l in range(2, len(s)):
#             i = 0
#             j = l
#             while j < len(s):
#                 if s[i] == s[j]:
#                     if dp[j-i+1-1-2][j-1]: # Track back previously computed palindrome
#                         dp[l][j] = 1
#                         res = s[i:j+1]
#                 i += 1
#                 j += 1
#         return res


# 176 / 176 test cases passed, but took too long.
# Status: Time Limit Exceeded
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        res = [0,0]
        for j in range(len(s)):
            dp[0][j] = 1

        for j in range(1, len(s)):
            if s[j] == s[j-1]:
                dp[1][j] = 1
                res[0] = j-1
                res[1] = j
                # res = s[j-1]+s[j]
        
        for l in range(1, len(s)):
            i = 0
            j = l
            while j < len(s):
                if s[i] == s[j]:
                    if dp[j-i+1-1-2][j-1]: # Track back previously computed palindrome
                        dp[l][j] = 1
                        # if len(res) < len(s[i:j+1]):
                        if res[1]-res[0] < j-i:
                            res[0] = i
                            res[1] = j
                            # res = s[i:j+1]
                i += 1
                j += 1
        return s[res[0]:res[1]+1]



class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # Form a bottom-up dp 2d array
        # dp[i][j] will be 'true' if the string from index i to j is a palindrome. 
        dp = [[False for _ in range(n)] for _ in range(n)]
        
        ans = ''
        # every string with one character is a palindrome
        for i in range(n):
            dp[i][i] = True
            ans = s[i]
            
        maxLen = 1
        for start in range(n-1, -1, -1):
            for end in range(start+1, n):             
				# palindrome condition
                if s[start] == s[end]:
                    # if it's a two char. string or if the remaining string is a palindrome too
                    if end - start == 1 or dp[start+1][end-1]:
                        dp[start][end] = True
                        if maxLen < end - start + 1:
                            maxLen = end - start + 1
                            ans = s[start: end+1]
        
        return ans


# Runtime: 6620 ms, faster than 23.18% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 22.8 MB, less than 6.77% of Python3 online submissions for Longest Palindromic Substring.



"""
Using this way: dp = [[False] * n  for _ in range(n)] is faster than this way: dp = [[False for _ in range(n)] for _ in range(n)]
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # Form a bottom-up dp 2d array
        # dp[i][j] will be 'true' if the string from index i to j is a palindrome. 
        dp = [[False] * n  for _ in range(n)]
        
        ans = ''
        # every string with one character is a palindrome
        for i in range(n):
            dp[i][i] = True
            ans = s[i]
            
        maxLen = 1
        for start in range(n-1, -1, -1):
            for end in range(start+1, n):             
				# palindrome condition
                if s[start] == s[end]:
                    # if it's a two char. string or if the remaining string is a palindrome too
                    if end - start == 1 or dp[start+1][end-1]:
                        dp[start][end] = True
                        if maxLen < end - start + 1:
                            maxLen = end - start + 1
                            ans = s[start: end+1]
        
        return ans



# Runtime: 4152 ms, faster than 32.37% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 22.1 MB, less than 14.35% of Python3 online submissions for Longest Palindromic Substring.

solution = Solution()
print(solution.longestPalindrome(s))

