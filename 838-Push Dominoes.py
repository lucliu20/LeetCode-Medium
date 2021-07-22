# https://leetcode.com/problems/push-dominoes/

"""
Example 1:
Input: dominoes = "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.

Example 2:
Input: dominoes = ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."
"""

# dominoes = "RR.L"
# dominoes = ".L.R...LR..L.."
# dominoes = ".L.R." # "LL.RR"
dominoes = "R." # "RR"
# dominoes = "R.R.L" # "RRR.L"



class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        p1, p2 = -1, -1 # p1 is to track the location of "R", p2 is to track the location of "L"
        for i in range(len(dominoes)):
            if dominoes[i] == "R":
                if p1 >= 0 and p1 != i:
                    while p1 < i:
                        p1 += 1
                        dominoes = "R".join([dominoes[0:p1],dominoes[p1+1:]])
                p1 = i
            elif dominoes[i] == "L":
                p2 = i
                if p1 >= 0:
                    while p2 > 0 and p1 + 2 < p2:
                        p1 += 1
                        p2 -= 1
                        dominoes = "R".join([dominoes[0:p1],dominoes[p1+1:]])
                        dominoes = "L".join([dominoes[0:p2],dominoes[p2+1:]])
                    p1 = -1
                else:
                    while p2 > 0:
                        p2 -= 1
                        if dominoes[p2] == ".":
                            dominoes = "L".join([dominoes[0:p2],dominoes[p2+1:]])
                        else:
                            break
        if p1 >= 0 and p1 != i:
            while p1 < i:
                p1 += 1
                dominoes = "R".join([dominoes[0:p1],dominoes[p1+1:]])
        return dominoes


# Runtime: 2076 ms, faster than 5.25% of Python3 online submissions for Push Dominoes.
# Memory Usage: 15.7 MB, less than 94.23% of Python3 online submissions for Push Dominoes.


solution = Solution()
print(solution.pushDominoes(dominoes))

