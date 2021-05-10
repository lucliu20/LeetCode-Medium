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
                    dp[i][c] = max(dp[i-1][c], dp[i-1][c-weights[i-1]]+profits[i-1])
        return dp[len(profits)][capacity]
    

solution = Solution()
print(solution.knapsack(profits, weights, capacity))




