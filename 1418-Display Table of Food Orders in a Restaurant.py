# https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/


"""
Example 1:
Input: orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
Output: [["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],["3","0","2","1","0"],["5","0","1","0","1"],["10","1","0","0","0"]] 
Explanation:
The displaying table looks like:
Table,Beef Burrito,Ceviche,Fried Chicken,Water
3    ,0           ,2      ,1            ,0
5    ,0           ,1      ,0            ,1
10   ,1           ,0      ,0            ,0
For the table 3: David orders "Ceviche" and "Fried Chicken", and Rous orders "Ceviche".
For the table 5: Carla orders "Water" and "Ceviche".
For the table 10: Corina orders "Beef Burrito". 

Example 2:
Input: orders = [["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]]
Output: [["Table","Canadian Waffles","Fried Chicken"],["1","2","0"],["12","0","3"]] 
Explanation: 
For the table 1: Adam and Brianna order "Canadian Waffles".
For the table 12: James, Ratesh and Amadeus order "Fried Chicken".

Example 3:
Input: orders = [["Laura","2","Bean Burrito"],["Jhon","2","Beef Burrito"],["Melissa","2","Soda"]]
Output: [["Table","Bean Burrito","Beef Burrito","Soda"],["2","1","1","1"]]
"""

orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
# orders = [["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]]
# orders = [["Laura","2","Bean Burrito"],["Jhon","2","Beef Burrito"],["Melissa","2","Soda"]]


from typing import List
import collections
class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        # tmp = sorted(orders, key = lambda x:int(x[1]))
        orders.sort(key = lambda x:int(x[1]))
        table = collections.defaultdict()
        table.default_factory = table.__len__
        for i in range(len(orders)):
            table[orders[i][1]]
        
        # tmp = sorted(orders, key = lambda x:x[-1])
        orders.sort(key = lambda x:x[-1])
        food = collections.defaultdict()
        food.default_factory = food.__len__
        for i in range(len(orders)):
            food[orders[i][2]]
        
        pairs = collections.Counter()
        for i in range(len(orders)):
            pairs[(orders[i][1], orders[i][2])] += 1

        # Initialize the result 2-D array with string "0"
        """
        For example,
        ["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],
        ["0","0","0","0","0"],
        ["0","0","0","0","0"],
        ["0","0","0","0","0"]
        """
        res = [["Table"] + [key for key in food.keys()]]
        res.extend([["0" for col in range(len(food)+1)] for row in range(len(table))])

        # Then iterate the dict pairs to update the table numbers and order numbers in string format
        for key, value in pairs.items():
            tab, item = key
            res[table[tab]+1][0] = tab
            res[table[tab]+1][food[item]+1] = str(value)
        return res

solution = Solution()
print(solution.displayTable(orders))

# Runtime: 408 ms, faster than 92.54% of Python3 online submissions for Display Table of Food Orders in a Restaurant.
# Memory Usage: 24.3 MB, less than 71.64% of Python3 online submissions for Display Table of Food Orders in a Restaurant.


