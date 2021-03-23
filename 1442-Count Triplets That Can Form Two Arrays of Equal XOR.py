# https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/
# Refer to the video https://www.youtube.com/watch?v=30A0Z2KDvaA


"""
Example 1:
Input: arr = [2,3,1,6,7]
Output: 4
Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)

Example 2:
Input: arr = [1,1,1,1,1]
Output: 10

Example 3:
Input: arr = [2,3]
Output: 0

Example 4:
Input: arr = [1,3,5,7,9]
Output: 3

Example 5:
Input: arr = [7,11,12,9,5,2,7,17,22]
Output: 8
"""

# arr = [2,3,1,6,7]
# arr = [1,1,1,1,1]
# arr = [2,3]
# arr = [1,3,5,7,9]
arr = [7,11,12,9,5,2,7,17,22]



"""
a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
Condition is a == b
One way of deriving a and b is such:
A = 0 ^ A, B ^ B = 0; thus
A = B ^ B ^ A.
Keep this in mind.

So, let's derive a first.
  arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
= (arr[0] ^ arr[1] ^ ... ^ arr[i - 1]) ^ (arr[0] ^ arr[1] ^ ... ^ arr[i - 1]) ^ (arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1])

Assume xors[i] = arr[0] ^ arr[1] ^ ... ^ arr[i - 1] (note there are n elements). Thus xors[j] = arr[0] ^ arr[1] ^ ... ^ arr[j - 1].
Then the above equation becomes:
  arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
= (arr[0] ^ arr[1] ^ ... ^ arr[i - 1]) ^ (arr[0] ^ arr[1] ^ ... ^ arr[i - 1] ^ arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1])
= xors[i] ^ xors[j]

So, a = xors[i] ^ xors[j].

Now let's derive b.
  arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
= (arr[0] ^ arr[1] ^ ... ^ arr[j - 1]) ^ (arr[0] ^ arr[1] ^ ... ^ arr[j - 1]) ^ (arr[j] ^ arr[j + 1] ^ ... ^ arr[k])
= (arr[0] ^ arr[1] ^ ... ^ arr[j - 1]) ^ (arr[0] ^ arr[1] ^ ... ^ arr[j - 1] ^ arr[j] ^ arr[j + 1] ^ ... ^ arr[k])
= xors[j] ^ xors[k+1]  # why is it xors[k+1], instead of xors[k]? Because there are (k+1) elements.

So, b = xors[j] ^ xors[k+1]

"""
# Time complexicy: O(n^3)
from typing import List
# class Solution:
#     def countTriplets(self, arr: List[int]) -> int:
#         res = 0
#         # Here use a new array for the prefix.
#         # Note that the first element is initialized a zero.
#         xors = [0]
#         for n in range(len(arr)):
#             xors.append(xors[n] ^ arr[n])
# 
#         # Or just use the original array
#         # arr.insert(0, 0)
#         # for n in range(len(arr)-1):
#         #     arr[n+1] ^= arr[n]
# 
#         for i in range(len(arr)):
#             for j in range(i+1, len(arr)):
#                 for k in range(j, len(arr)): # Note that j <= k
#                     a = xors[i] ^ xors[j]
#                     b = xors[j] ^ xors[k+1]
#                     if a == b:
#                         res += 1
#         return res

# Runtime: 4552 ms, faster than 7.34% of Python3 online submissions for Count Triplets That Can Form Two Arrays of Equal XOR.
# Memory Usage: 14.3 MB, less than 66.43% of Python3 online submissions for Count Triplets That Can Form Two Arrays of Equal XOR.


"""
Kee the below in mind.
If A = B, then A ^ B = 0 ----- (1)
A ^ 0 = A -------------------- (2)

Assume a = b, i.e.,
arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1] = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
Then use the above first equation, we get:
(arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]) ^ (arr[j] ^ arr[j + 1] ^ ... ^ arr[k]) = 0 ----- (3)

Refer to the above second equation
(arr[0] ^ arr[1] ^ ... ^ arr[i - 1]) ^ 0 = (arr[0] ^ arr[1] ^ ... ^ arr[i - 1])
Replace 0 with the above third equation; then we get:
(arr[0] ^ arr[1] ^ ... ^ arr[i - 1]) ^ (arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]) ^ (arr[j] ^ arr[j + 1] ^ ... ^ arr[k]) = (arr[0] ^ arr[1] ^ ... ^ arr[i - 1])
Thus, we still assume xors[i] = arr[0] ^ arr[1] ^ ... ^ arr[i - 1]. Then, the above equation becomes:
xors[k+1] = xors[i]

So our goal becomes to find the two equal xors elements that satisfy the condition: xors[k+1] = xors[i].
For each pair of (i, k), we can just pick any j from i+1 to k (i < j <= k), i.e., k-(i+1)+1 = k-i slots.
"""
# Time complexicy: O(n^2)
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        res = 0
        xors = [0]
        for n in range(len(arr)):
            xors.append(xors[n] ^ arr[n])
        
        for i in range(len(arr)):
            for k in range(i+1, len(arr)):
                if xors[k+1] == xors[i]:
                    res += (k-i)
        return res


# Runtime: 56 ms, faster than 72.38% of Python3 online submissions for Count Triplets That Can Form Two Arrays of Equal XOR.
# Memory Usage: 14.3 MB, less than 38.46% of Python3 online submissions for Count Triplets That Can Form Two Arrays of Equal XOR.

solution = Solution()
print(solution.countTriplets(arr))



