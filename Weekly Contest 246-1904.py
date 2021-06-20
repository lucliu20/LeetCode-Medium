#  https://leetcode.com/problems/the-number-of-full-rounds-you-have-played/



# startTime, finishTime = "00:00", "23:59" # 95
# startTime, finishTime = "20:00", "06:00" # 40
# startTime, finishTime = "12:01", "12:44" # 1
# startTime, finishTime = "00:01", "00:00" # 95
# startTime, finishTime = "20:30", "06:15" # 39
# startTime, finishTime = "20:30", "06:45" # 41
# startTime, finishTime = "20:01", "06:00" # 39
# startTime, finishTime = "04:54", "18:51" # 55
# startTime, finishTime = "23:46", "00:01" # 0
# startTime, finishTime = "23:48", "23:16" # 93
startTime, finishTime = "14:59", "09:01"


class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        myset = {0, 15, 30, 45}
        offset = 0
        startMin, startHr = int(startTime[3:5]), int(startTime[0:2])
        finishMin, finishHr = int(finishTime[3:5]), int(finishTime[0:2])
        if startMin in myset:
            first = startMin
        elif startMin in range(0,15):
            first = 15
        elif startMin in range(15,30):
            first = 30
        elif startMin in range(30,45):
            first = 45
        elif startMin in range(45,60):
            first = 0
            offset = 1
        
        r1, r2 = 0, 0
        if finishHr < startHr:
            if finishMin < first:
                r1 = (60-(first-finishMin))//15
                tmp = 24-startHr-1+offset
                r2 = (finishHr+tmp)*4
            else:
                r1 = (finishMin-first)//15
                tmp = 24-(startHr+offset)
                r2 = (finishHr+tmp)*4
        elif finishHr > startHr:
            if finishMin < first:
                r1 = (60-(first-finishMin))//15
                r2 = (finishHr-startHr-1)*4
            else:
                r1 = (finishMin-first)//15
                r2 = (finishHr-(startHr+offset))*4
        elif finishHr == startHr:
            if finishMin < first:
                r1 = 95
            else:
                r1 = (finishMin-first)//15
                if offset != 0:
                    r2 = 92
        return r1+r2

# Runtime: 28 ms, faster than 100.00% of Python3 online submissions for The Number of Full Rounds You Have Played.
# Memory Usage: 14.5 MB, less than 33.33% of Python3 online submissions for The Number of Full Rounds You Have Played.


solution = Solution()
print(solution.numberOfRounds(startTime, finishTime))

