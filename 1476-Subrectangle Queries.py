# https://leetcode.com/problems/subrectangle-queries/

"""
Example 1:
Input
["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue","getValue"]
[[[[1,2,1],[4,3,4],[3,2,1],[1,1,1]]],[0,2],[0,0,3,2,5],[0,2],[3,1],[3,0,3,2,10],[3,1],[0,2]]
Output
[null,1,null,5,5,null,10,5]
Explanation
SubrectangleQueries subrectangleQueries = new SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]]);  
// The initial rectangle (4x3) looks like:
// 1 2 1
// 4 3 4
// 3 2 1
// 1 1 1
subrectangleQueries.getValue(0, 2); // return 1
subrectangleQueries.updateSubrectangle(0, 0, 3, 2, 5);
// After this update the rectangle looks like:
// 5 5 5
// 5 5 5
// 5 5 5
// 5 5 5 
subrectangleQueries.getValue(0, 2); // return 5
subrectangleQueries.getValue(3, 1); // return 5
subrectangleQueries.updateSubrectangle(3, 0, 3, 2, 10);
// After this update the rectangle looks like:
// 5   5   5
// 5   5   5
// 5   5   5
// 10  10  10 
subrectangleQueries.getValue(3, 1); // return 10
subrectangleQueries.getValue(0, 2); // return 5

Example 2:
Input
["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue"]
[[[[1,1,1],[2,2,2],[3,3,3]]],[0,0],[0,0,2,2,100],[0,0],[2,2],[1,1,2,2,20],[2,2]]
Output
[null,1,null,100,100,null,20]
Explanation
SubrectangleQueries subrectangleQueries = new SubrectangleQueries([[1,1,1],[2,2,2],[3,3,3]]);
subrectangleQueries.getValue(0, 0); // return 1
subrectangleQueries.updateSubrectangle(0, 0, 2, 2, 100);
subrectangleQueries.getValue(0, 0); // return 100
subrectangleQueries.getValue(2, 2); // return 100
subrectangleQueries.updateSubrectangle(1, 1, 2, 2, 20);
subrectangleQueries.getValue(2, 2); // return 20
"""


from typing import List
class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle.copy()

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                self.rectangle[i][j] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]



# subrectangleQueries = SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]])
# print(subrectangleQueries.getValue(0, 2)) # return 1
# subrectangleQueries.updateSubrectangle(0, 0, 3, 2, 5)
# print(subrectangleQueries.getValue(0, 2)) # return 5
# print(subrectangleQueries.getValue(3, 1)) # return 5
# subrectangleQueries.updateSubrectangle(3, 0, 3, 2, 10)
# print(subrectangleQueries.getValue(3, 1)) # return 10
# print(subrectangleQueries.getValue(0, 2)) # return 5
# pass


subrectangleQueries = SubrectangleQueries([[1,1,1],[2,2,2],[3,3,3]])
print(subrectangleQueries.getValue(0, 0)) # return 1
subrectangleQueries.updateSubrectangle(0, 0, 2, 2, 100)
print(subrectangleQueries.getValue(0, 0)) # return 100
print(subrectangleQueries.getValue(2, 2)) # return 100
subrectangleQueries.updateSubrectangle(1, 1, 2, 2, 20)
print(subrectangleQueries.getValue(2, 2)) # return 20
pass


# Runtime: 372 ms, faster than 5.19% of Python3 online submissions for Subrectangle Queries.
# Memory Usage: 16 MB, less than 74.78% of Python3 online submissions for Subrectangle Queries.



# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)


