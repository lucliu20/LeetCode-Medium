# https://leetcode.com/problems/word-break/

"""
Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
"""


s, wordDict = "leetcode", ["leet","code"]
# s, wordDict = "applepenapple", ["apple","pen"]
# s, wordDict = "catsandog", ["cats","dog","sand","and","cat"]
# Test case #34: True
# s, wordDict = "aaaaaaa", ["aaaa","aaa"]

# Test case #35: Expected: False
# s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
# wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
# Simplified version:
# s, wordDict = "aaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

# Test case #38:
# s, wordDict = "catskicatcats", ["cats","cat","dog","ski"] # True

# Test case #40: Expected: False
# s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
# Simplified version:
# s, wordDict = "aaaabaaa", ["a","aa","aaa"]

# Test case #39: Expected: True
# s, wordDict = "aebbbbs", ["a","aeb","ebbbb","s","eb"]

# Test case #40: Expected: True
# s = "fohhemkkaecojceoaejkkoedkofhmohkcjmkggcmnami"
# wordDict = ["kfomka","hecagbngambii","anobmnikj","c","nnkmfelneemfgcl","ah","bgomgohl","lcbjbg","ebjfoiddndih","hjknoamjbfhckb","eioldlijmmla","nbekmcnakif","fgahmihodolmhbi","gnjfe","hk","b","jbfgm","ecojceoaejkkoed","cemodhmbcmgl","j","gdcnjj","kolaijoicbc","liibjjcini","lmbenj","eklingemgdjncaa","m","hkh","fblb","fk","nnfkfanaga","eldjml","iejn","gbmjfdooeeko","jafogijka","ngnfggojmhclkjd","bfagnfclg","imkeobcdidiifbm","ogeo","gicjog","cjnibenelm","ogoloc","edciifkaff","kbeeg","nebn","jdd","aeojhclmdn","dilbhl","dkk","bgmck","ohgkefkadonafg","labem","fheoglj","gkcanacfjfhogjc","eglkcddd","lelelihakeh","hhjijfiodfi","enehbibnhfjd","gkm","ggj","ag","hhhjogk","lllicdhihn","goakjjnk","lhbn","fhheedadamlnedh","bin","cl","ggjljjjf","fdcdaobhlhgj","nijlf","i","gaemagobjfc","dg","g","jhlelodgeekj","hcimohlni","fdoiohikhacgb","k","doiaigclm","bdfaoncbhfkdbjd","f","jaikbciac","cjgadmfoodmba","molokllh","gfkngeebnggo","lahd","n","ehfngoc","lejfcee","kofhmoh","cgda","de","kljnicikjeh","edomdbibhif","jehdkgmmofihdi","hifcjkloebel","gcghgbemjege","kobhhefbbb","aaikgaolhllhlm","akg","kmmikgkhnn","dnamfhaf","mjhj","ifadcgmgjaa","acnjehgkflgkd","bjj","maihjn","ojakklhl","ign","jhd","kndkhbebgh","amljjfeahcdlfdg","fnboolobch","gcclgcoaojc","kfokbbkllmcd","fec","dljma","noa","cfjie","fohhemkka","bfaldajf","nbk","kmbnjoalnhki","ccieabbnlhbjmj","nmacelialookal","hdlefnbmgklo","bfbblofk","doohocnadd","klmed","e","hkkcmbljlojkghm","jjiadlgf","ogadjhambjikce","bglghjndlk","gackokkbhj","oofohdogb","leiolllnjj","edekdnibja","gjhglilocif","ccfnfjalchc","gl","ihee","cfgccdmecem","mdmcdgjelhgk","laboglchdhbk","ajmiim","cebhalkngloae","hgohednmkahdi","ddiecjnkmgbbei","ajaengmcdlbk","kgg","ndchkjdn","heklaamafiomea","ehg","imelcifnhkae","hcgadilb","elndjcodnhcc","nkjd","gjnfkogkjeobo","eolega","lm","jddfkfbbbhia","cddmfeckheeo","bfnmaalmjdb","fbcg","ko","mojfj","kk","bbljjnnikdhg","l","calbc","mkekn","ejlhdk","hkebdiebecf","emhelbbda","mlba","ckjmih","odfacclfl","lgfjjbgookmnoe","begnkogf","gakojeblk","bfflcmdko","cfdclljcg","ho","fo","acmi","oemknmffgcio","mlkhk","kfhkndmdojhidg","ckfcibmnikn","dgoecamdliaeeoa","ocealkbbec","kbmmihb","ncikad","hi","nccjbnldneijc","hgiccigeehmdl","dlfmjhmioa","kmff","gfhkd","okiamg","ekdbamm","fc","neg","cfmo","ccgahikbbl","khhoc","elbg","cbghbacjbfm","jkagbmfgemjfg","ijceidhhajmja","imibemhdg","ja","idkfd","ndogdkjjkf","fhic","ooajkki","fdnjhh","ba","jdlnidngkfffbmi","jddjfnnjoidcnm","kghljjikbacd","idllbbn","d","mgkajbnjedeiee","fbllleanknmoomb","lom","kofjmmjm","mcdlbglonin","gcnboanh","fggii","fdkbmic","bbiln","cdjcjhonjgiagkb","kooenbeoongcle","cecnlfbaanckdkj","fejlmog","fanekdneoaammb","maojbcegdamn","bcmanmjdeabdo","amloj","adgoej","jh","fhf","cogdljlgek","o","joeiajlioggj","oncal","lbgg","elainnbffk","hbdi","femcanllndoh","ke","hmib","nagfahhljh","ibifdlfeechcbal","knec","oegfcghlgalcnno","abiefmjldmln","mlfglgni","jkofhjeb","ifjbneblfldjel","nahhcimkjhjgb","cdgkbn","nnklfbeecgedie","gmllmjbodhgllc","hogollongjo","fmoinacebll","fkngbganmh","jgdblmhlmfij","fkkdjknahamcfb","aieakdokibj","hddlcdiailhd","iajhmg","jenocgo","embdib","dghbmljjogka","bahcggjgmlf","fb","jldkcfom","mfi","kdkke","odhbl","jin","kcjmkggcmnami","kofig","bid","ohnohi","fcbojdgoaoa","dj","ifkbmbod","dhdedohlghk","nmkeakohicfdjf","ahbifnnoaldgbj","egldeibiinoac","iehfhjjjmil","bmeimi","ombngooicknel","lfdkngobmik","ifjcjkfnmgjcnmi","fmf","aoeaa","an","ffgddcjblehhggo","hijfdcchdilcl","hacbaamkhblnkk","najefebghcbkjfl","hcnnlogjfmmjcma","njgcogemlnohl","ihejh","ej","ofn","ggcklj","omah","hg","obk","giig","cklna","lihaiollfnem","ionlnlhjckf","cfdlijnmgjoebl","dloehimen","acggkacahfhkdne","iecd","gn","odgbnalk","ahfhcd","dghlag","bchfe","dldblmnbifnmlo","cffhbijal","dbddifnojfibha","mhh","cjjol","fed","bhcnf","ciiibbedklnnk","ikniooicmm","ejf","ammeennkcdgbjco","jmhmd","cek","bjbhcmda","kfjmhbf","chjmmnea","ifccifn","naedmco","iohchafbega","kjejfhbco","anlhhhhg"]



# DP
# Iteratively
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[0] = True
        wordDict.sort(key=len, reverse=True)
        mword = len(wordDict[0])
        myset = set(wordDict)
        j = 0 # to track the start position of a to-be-scanned string
        for i in range(len(s)):
            if s[i] in myset:
                if dp[i] == True:
                    dp[i+1] = True
                    j = i+1
            if s[j:i+1] in myset:
                if dp[j] == True:
                    dp[i+1] = True
                    j = i+1
            else:
                for k in range(mword-1): # only need to iterate the max length of a wordDict element
                    start = max(k, i-mword+k+1)
                    if s[start:i+1] in myset:
                        if dp[start] == True:
                            dp[i+1] = True
                            j = i+1
                            break
        return dp[-1]


# Runtime: 48 ms, faster than 14.95% of Python3 online submissions for Word Break.
# Memory Usage: 14.5 MB, less than 23.67% of Python3 online submissions for Word Break.


# Initial attempt, it failed at test case #34
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         myset = set(wordDict)
#         word = ""
#         for i in range(len(s)):
#             word += s[i]
#             if word in myset:
#                 word = ""
#         return len(word) == 0



# Backtracking
# Recursively
# 35 / 42 test cases passed.
# Status: Time Limit Exceeded
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         def isValid(i, j, myset):
#             print(s[i:j+1])
#             if s[i:j+1] in myset:
#                 return True
#             return False
#         
#         def fountSolution(memo):
#             return len(memo) == len(s)
#         
#         def placing(memo, i, j):
#             memo += s[i:j+1]
#             return memo
# 
#         def removing(memo, i, j):
#             memo = memo[:-(j-i+1)]
#             return memo
# 
#         def backtracking(memo, i, myset):
#             if fountSolution(memo):
#                 return True
#             for j in range(i, len(s)):
#                 if isValid(i, j, myset):
#                     memo = placing(memo, i, j)
#                     tmp = backtracking(memo, j+1, myset)
#                     if tmp == True:
#                         return True
#                     memo = removing(memo, i, j)
#             return False
#         
#         memo, res = "", False
#         myset = set(wordDict)
#         res = backtracking(memo, 0, myset)
#         return res



# DP
# Iteratively
# Using heapq
# 39 / 42 test cases passed.
# Status: Wrong Answer
# import heapq
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         dp = [False]*(len(s)+1)
#         dp[0] = True
#         myset = set(wordDict)
#         heap, j = [], 0
#         heapq.heappush(heap, 0)
#         for i in range(len(s)):
#             if s[i] in myset or s[j:i+1] in myset:
#                 if dp[j] == True:
#                     dp[i+1] = True
#                     if i != 0:
#                         # heapq.heappush(heap, -i)
#                         heapq.heappush(heap, -(i+1))
#                     j = i+1
#             else:
#                 for k in range(len(heap)):
#                     if (s[(-heap[k]):i] + s[i]) in myset:
#                         if dp[(-heap[k])] == True:
#                             dp[i+1] = True
#                             # heapq.heappush(heap, -i)
#                             heapq.heappush(heap, -(i+1))
#                             # j = i+1
#                             break
#                 j = i+1
#         return dp[-1]





solution = Solution()
print(solution.wordBreak(s, wordDict))



