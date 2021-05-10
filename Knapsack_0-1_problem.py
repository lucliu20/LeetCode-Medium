# https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/RM1BDv71V60



# profits, weights, capacity = [1, 6, 10, 16], [1, 2, 3, 5], 7 # 22
# profits, weights, capacity = [1, 6, 10, 16], [1, 2, 3, 5], 6 # 17
# profits, weights, capacity = [1, 6, 10, 16], [1, 2, 3, 5], 5 # 16
profits, weights, capacity = [60, 100, 120], [10, 20, 30], 50


# Recursive
# Top-down Dynamic Programming with Memoization
# educative.io version
from typing import List
class Solution:
    def knapsack(self, profits: List[int], weights: List[int], capacity) -> int:
        def dfs(memo, capacity, currentIndex):
            if currentIndex >= len(profits) or capacity <= 0:
                return 0
            if memo[currentIndex][capacity] != -1:
                return memo[currentIndex][capacity]
            profit1 = 0
            if weights[currentIndex] <= capacity:
                profit1 = profits[currentIndex] + dfs(memo, capacity-weights[currentIndex], currentIndex+1)
            profit2 = dfs(memo, capacity, currentIndex+1)
            memo[currentIndex][capacity] = max(profit1, profit2)
            return memo[currentIndex][capacity]

        memo = [[-1 for _ in range(capacity + 1)] for _ in range(len(profits))]
        res = dfs(memo, capacity, 0)
        return res



# Recursive
# Top-down Dynamic Programming with Memoization
# It lines up with the DP bottom-up solution below.
# Time complexity: O(N*C) where ‘N’ is the number of items and ‘C’ is the knapsack capacity
# Space complexity: O(N∗C)
from typing import List
class Solution:
    def knapsack(self, profits: List[int], weights: List[int], capacity) -> int:
        def dfs(memo, capacity, currentIndex):
            if currentIndex >= len(profits) or capacity <= 0:
                return 0
            if memo[currentIndex][capacity] != -1:
                return memo[currentIndex][capacity]
            elif weights[currentIndex-1] > capacity:
                memo[currentIndex][capacity] = dfs(memo, capacity, currentIndex+1)
            elif weights[currentIndex-1] <= capacity:
                memo[currentIndex][capacity] = max(dfs(memo, capacity, currentIndex+1), dfs(memo, capacity-weights[currentIndex-1], currentIndex+1)+profits[currentIndex-1])
            return memo[currentIndex][capacity]

        memo = [[-1 for _ in range(capacity + 1)] for _ in range(len(profits)+1)]
        res = dfs(memo, capacity, 0)
        return res



# DP
# Bottom-up with Tabulation
# Time complexity: O(N*C) where ‘N’ is the number of items and ‘C’ is the knapsack capacity
# Space complexity: O(N∗C)
# Illustration of the example profits = [1, 6, 10, 16], weights = [1, 2, 3, 5], capacity = 7
# 			                    capacity -->
# profit []	weight []	index	0	1	2	3	4	5	6	7
#   -	        -	        0	0	0	0	0	0	0	0	0
#   1	        1	        1	0	1	1	1	1	1	1	1
#   6	        2	        2	0	1	6	7	7	7	7	7
#   10	        3	        3	0	1	6	10	11	16	17	17
#   16	        5	        4	0	1	6	10	11	16	17	22(6+16)
# 
# dp[len(profits)][capacity] = dp[4][7] = max(dp[4-1][7], dp[4-1][7-2]+profits[4-1]) = max(17, 6+16) = max(17, 22) = 22



class Solution:
    def knapsack(self, profits: List[int], weights: List[int], capacity) -> int:
        dp = [[0 for _ in range(capacity + 1)] for _ in range(len(profits) + 1)]
        for i in range(1, 2):
            for j in range(1, capacity+1):
                if weights[0] <= j:
                    dp[i][j] = profits[0]

        for i in range(2, len(weights)+1):
            for c in range(1, capacity+1):
                if weights[i-1] > c:
                    dp[i][c] = dp[i-1][c]
                else:
                    # what c-weights[i-1] refers to: it refers to the left available weight if we take the object with weight equal to weights[i-1]
                    # say we are at the capacity of 7, and weight is weights[4]=5. if we take the weight 5 object, then the left available weight is 7-5=2.
                    # so the total profit when we take the weitht 5 is (profits[4]=16) + whatever the profit is at the capacity 2 without this object weight=5.
                    # the computed profit at capacity 2 is maximized as we are aware of, and it is 6.
                    # so the total profit when we take the weight 5 object is 6+16=22.
                    dp[i][c] = max(dp[i-1][c], dp[i-1][c-weights[i-1]]+profits[i-1])
        return dp[len(profits)][capacity]
    

solution = Solution()
print(solution.knapsack(profits, weights, capacity))




