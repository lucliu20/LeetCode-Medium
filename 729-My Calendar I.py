# https://leetcode.com/problems/my-calendar-i/


# class MyCalendar:
# 
#     def __init__(self):
#         self.arr = []
# 
#     def book(self, start: int, end: int) -> bool:
#         if len(self.arr) == 0:
#             self.arr.extend([start, end])
#             return True
#         else:
#             low, high = 0, len(self.arr)-1
#             left, right = 0, 0
#             while low <= high:
#                 mid = low + (high-low) // 2
#                 if self.arr[mid] < start:
#                     low = mid + 1
#                 elif self.arr[mid] > start:
#                     high = mid - 1
#                 else:
#                     high = mid
#                     break
#             if high < 0:
#                 if self.arr[0] > end:
#                     self.arr.insert(0, end)
#                     self.arr.insert(0, start)
#                     return True
#                 elif self.arr[0] == end:
#                     self.arr.remove(end)
#                     self.arr.insert(0, start)
#                     return True
#                 else:
#                     return False
#             elif high%2 != 0:    
#                 left = high
#                 high = len(self.arr)-1
#                 while low <= high:
#                     mid = low + (high-low) // 2
#                     if self.arr[mid] < end:
#                         low = mid + 1
#                     elif self.arr[mid] > end:
#                         high = mid - 1
#                     else:
#                         high = mid
#                         break
#                 if high%2 == 0:
#                     right = high
#                     self.arr.insert(left, start)
#                     self.arr.insert(right, end)
#                     return True
#                 elif high == len(self.arr)-1:
#                     if self.arr[high] == start:
#                         self.arr.pop()
#                         self.arr.append(end)
#                     elif self.arr[high] >= end:
#                         self.arr.append(start)
#                         self.arr.append(end)
#                     else:
#                         return False
#                     return True
#                 elif low%2 == 0:
#                     if self.arr[low] > end:
#                         if self.arr[left] == start:
#                             self.arr.remove(start)
#                             self.arr.insert(left, end)
#                         else:
#                             right = high
#                             self.arr.insert(right, start)
#                             self.arr.insert(left, end)
#                         return True
#                 else:
#                     return False
#             else:
#                 return False


# below approach doesn't work.
class MyCalendar:

    def __init__(self):
        self.arr = []

    def book(self, start: int, end: int) -> bool:
        if len(self.arr) == 0:
            self.arr.extend([start, end])
            return True
        else:
            low, high = 0, len(self.arr)-1
            while low <= high:
                mid = low + (high-low) // 2
                if self.arr[mid] < start:
                    low = mid + 1
                elif self.arr[mid] > start:
                    high = mid - 1
                else:
                    high = mid
                    break
            
            if high < 0:
                if self.arr[0] > end:
                    self.arr.insert(0, end)
                    self.arr.insert(0, start)
                    return True
                elif self.arr[0] == end: # merge two time slots
                    self.arr.remove(end)
                    self.arr.insert(0, start)
                    return True
                else:
                    return False
            elif low >= len(self.arr):
                if start == self.arr[len(self.arr)-1]:
                    self.arr.remove(start)
                    self.arr.append(end)
                else:
                    self.arr.append(start)
                    self.arr.append(end)
                return True
            elif high == mid and self.arr[high] == start:
                if high%2 == 0:
                    return False
                else:
                    if high == len(self.arr)-1:
                        if self.arr[high] == start:
                            self.arr.pop()
                            self.arr.append(end)
                        elif self.arr[high] >= end:
                            self.arr.append(start)
                            self.arr.append(end)
                        else:
                            return False
                        return True
                    elif end < self.arr[high+1]:
                        self.arr.remove(start)
                        self.arr.insert(high, end)
                        return True
                    elif end == self.arr[high+1]:
                        self.arr.remove(self.arr[high+1])
                        self.arr.remove(start)
                        return True
                    else:
                        return False
            elif start == self.arr[low]:
                    if end <= self.arr[low+1]:
                        self.arr.remove(end)
                        self.arr.insert(low+1, start)
                        return True
                    else:
                        return False
            elif self.arr[high] <= start < self.arr[low]:
                return False



class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start, end):
        for s, e in self.calendar:
            if s < end and start < e:
                return False
        self.calendar.append((start, end))
        return True



# Runtime: 660 ms, faster than 34.67% of Python3 online submissions for My Calendar I.
# Memory Usage: 14.5 MB, less than 98.69% of Python3 online submissions for My Calendar I.


solution = MyCalendar()
# print(solution.book(10, 20)) # returns true
# print(solution.book(15, 25)) # returns false
# print(solution.book(20, 30)) # returns true
# print(solution.book(0, 5)) # returns true
# print(solution.book(6, 35)) # returns false
# pass



# ["MyCalendar","book","book","book","book","book","book","book","book","book","book"]
# [[],[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]]
# output: [null,true,true,false,false,true,false,true,true,false,true]
# Expected: [null,true,true,false,false,true,false,true,true,true,false]

print(solution.book(47,50)) # returns true
print(solution.book(33,41)) # returns true
print(solution.book(39,45)) # returns false
print(solution.book(33,42)) # returns false
print(solution.book(25,32)) # returns true

print(solution.book(26,35)) # returns false
print(solution.book(19,25)) # returns true
print(solution.book(3,8)) # returns true
print(solution.book(8,13)) # returns true
print(solution.book(18,27)) # returns false
pass


# ["MyCalendar","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book"]
# [[],[20,29],[13,22],[44,50],[1,7],[2,10],[14,20],[19,25],[36,42],[45,50],[47,50],[39,45],[44,50],[16,25],[45,50],[45,50],[12,20],[21,29],[11,20],[12,17],[34,40],[10,18],[38,44],[23,32],[38,44],[15,20],[27,33],[34,42],[44,50],[35,40],[24,31]]
# output: [null,true,false,false,true,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false]
# Expected: [null,true,false,true,true,false,true,false,true,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false]
# print(solution.book(20,29)) # returns true
# print(solution.book(13,22)) # returns false
# print(solution.book(44,50)) # returns true
# print(solution.book(1,7)) # returns true
# print(solution.book(2,10)) # returns false
# pass



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)