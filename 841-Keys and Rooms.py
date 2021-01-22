# https://leetcode.com/problems/keys-and-rooms/

"""
Example 1:
Input: [[1],[2],[3],[]]
Output: true
Explanation:  
We start in room 0, and pick up key 1.
We then go to room 1, and pick up key 2.
We then go to room 2, and pick up key 3.
We then go to room 3.  Since we were able to go to every room, we return true.

Example 2:
Input: [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can't enter the room with number 2.
"""
rooms = [[1],[2],[3],[]]
# rooms = [[1,3],[3,0,1],[2],[0]]
# rooms = [[2],[],[1]] # True
# rooms = [[1,3],[1,4],[2,3,2,4,1],[],[4,3,2]] # True

class Solution:
    def canVisitAllRooms(self, rooms: list(list())) -> bool:
        keys = [0]
        visited = [False] * len(rooms)
        while keys:
            i = keys.pop()
            if visited[i] == False:
                for t in rooms[i]:
                    keys.append(t)
                visited[i] = True
            if all(visited):
                return True
        return all(visited)

solution = Solution()
print(solution.canVisitAllRooms(rooms))

# Runtime: 60 ms, faster than 91.67% of Python3 online submissions for Keys and Rooms.
# Memory Usage: 14.7 MB, less than 81.64% of Python3 online submissions for Keys and Rooms.


