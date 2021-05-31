# https://leetcode.com/problems/search-suggestions-system/

"""
Example 1:
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]

Example 2:
Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]

Example 3:
Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]

Example 4:
Input: products = ["havana"], searchWord = "tatiana"
Output: [[],[],[],[],[],[],[]]
"""

# products, searchWord = ["mobile","mouse","moneypot","monitor","mousepad"], "mouse"
# products, searchWord = ["havana"], "havana"
# products, searchWord = ["bags","baggage","banner","box","cloths"], "bags"
# products, searchWord = ["havana"], "tatiana"
products, searchWord = ["mobile","mouse","moneypot","monitor","mousepad"], "mousekkkkkk"



# 40 / 41 test cases passed.
# Status: Time Limit Exceeded
from typing import List
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        products.sort()
        # Optimized with the below two lines code, resolved the TLE issue
        mysorted = sorted(products, key = len)
        longest = len(mysorted[-1])
        word = ""
        for c in searchWord:
            word += c
            i, j = 0, 0
            suggested = []
            if len(word) <= longest:
                while i <= 2 and j < len(products):
                    tmp = ""
                    for k in products[j]:
                        tmp += k
                        if word == tmp:
                            suggested.append(products[j])
                            i += 1
                            break
                        if len(tmp) >= len(word):
                            break
                    j += 1
            res.append(suggested)
        return res

# Runtime: 584 ms, faster than 20.98% of Python3 online submissions for Search Suggestions System.
# Memory Usage: 17.1 MB, less than 73.34% of Python3 online submissions for Search Suggestions System.


solution = Solution()
print(solution.suggestedProducts(products, searchWord))



