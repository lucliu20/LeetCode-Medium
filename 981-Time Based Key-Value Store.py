# https://leetcode.com/problems/time-based-key-value-store/

"""
Example 1:
Input: inputs = ["TimeMap","set","get","get","set","get","get"], inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
Output: [null,null,"bar","bar",null,"bar2","bar2"]
Explanation:   
TimeMap kv;   
kv.set("foo", "bar", 1); // store the key "foo" and value "bar" along with timestamp = 1   
kv.get("foo", 1);  // output "bar"   
kv.get("foo", 3); // output "bar" since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie "bar"   
kv.set("foo", "bar2", 4);   
kv.get("foo", 4); // output "bar2"   
kv.get("foo", 5); //output "bar2"   

Example 2:
Input: inputs = ["TimeMap","set","set","get","get","get","get","get"], inputs = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
Output: [null,null,null,"","high","high","low","low"]

["TimeMap","set","set","set","set","get","get","get","get","get","get","set","get","get","get","set","set","set","set","get","get"]
[[],["ctondw","ztpearaw",1],["vrobykydll","hwliiq",2],["gszaw","ztpearaw",3],["ctondw","gszaw",4],["gszaw",5],["ctondw",6],["ctondw",7],["gszaw",8],["vrobykydll",9],["ctondw",10],["vrobykydll","kcvcjzzwx",11],["vrobykydll",12],["ctondw",13],["vrobykydll",14],["ztpearaw","zondoubtib",15],["kcvcjzzwx","hwliiq",16],["wtgbfvg","vrobykydll",17],["hwliiq","gzsiivks",18],["kcvcjzzwx",19],["ztpearaw",20]]

Expected: [null,null,null,null,null,"ztpearaw","gszaw","gszaw","ztpearaw","hwliiq","gszaw",null,"kcvcjzzwx","gszaw","kcvcjzzwx",null,null,null,null,"hwliiq","zondoubtib"]
Output:   [null,null,null,null,null,"gszaw","gszaw","gszaw","gszaw","gszaw","gszaw",null,"kcvcjzzwx","kcvcjzzwx","kcvcjzzwx",null,null,null,null,"gzsiivks","gzsiivks"]

"""


import collections
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key2time = collections.defaultdict(list)
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key2time[key].append(timestamp)
        self.d[(key, timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key2time.keys():
            return ""
        time = self.findTimestamp(self.key2time[key], timestamp)
        if not time:
            return ""
        return self.d[(key, time)]

    def findTimestamp(self, times, timestamp: int) -> int:
        if times[0] > timestamp:
            return None
        l, r = 0, len(times)
        while l+1 < r:
            mid = l+(r-l)//2
            if times[mid] == timestamp:
                return times[mid]
            elif times[mid] > timestamp:
                r = mid
            else:
                l = mid
        return times[l]

kv = TimeMap()
# print(kv.set("foo", "bar", 1)) # store the key "foo" and value "bar" along with timestamp = 1
# print(kv.get("foo", 1)) # output "bar"
# print(kv.get("foo", 3)) # output "bar" since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie "bar"
# print(kv.set("foo", "bar2", 4))
# print(kv.get("foo", 4)) # output "bar2"
# print(kv.get("foo", 5)) # output "bar2"
# pass


print(kv.set("love","high",10)) # store the key "love" and value "high" along with timestamp = 10
print(kv.set("love","low",20)) # store the key "love" and value "low" along with timestamp = 20
print(kv.get("love", 5)) # output ""
print(kv.get("love", 10)) # output "high"
print(kv.get("love", 15)) # output "high"
print(kv.get("love", 20)) # output "low"
print(kv.get("love", 25)) # output "low"
pass


# print(kv.set("ctondw","ztpearaw",1)) # store the key "ctondw" and value "ztpearaw" along with timestamp = 1
# print(kv.set("vrobykydll","hwliiq",2)) # store the key "vrobykydll" and value "hwliiq" along with timestamp = 2
# print(kv.set("gszaw","ztpearaw",3)) # store the key "gszaw" and value "ztpearaw" along with timestamp = 3
# print(kv.set("ctondw","gszaw",4)) # store the key "ctondw" and value "gszaw" along with timestamp = 4
# print(kv.get("gszaw",5)) # output "ztpearaw"
# print(kv.get("ctondw", 6)) # output "gszaw"
# print(kv.get("ctondw", 7)) # output "gszaw"
# print(kv.get("gszaw", 8)) # output "ztpearaw"
# print(kv.get("vrobykydll", 9)) # output "hwliiq"
# print(kv.get("ctondw", 10)) # output "gszaw"
# print(kv.set("vrobykydll","kcvcjzzwx",1)) # store the key "vrobykydll" and value "kcvcjzzwx" along with timestamp = 11
# print(kv.get("vrobykydll",12)) # output "kcvcjzzwx"
# print(kv.get("ctondw", 13)) # output "gszaw"
# print(kv.get("vrobykydll", 14)) # output "kcvcjzzwx"
# print(kv.set("ztpearaw","zondoubtib",15)) # store the key "ztpearaw" and value "zondoubtib" along with timestamp = 15
# print(kv.set("kcvcjzzwx","hwliiq",16)) # store the key "kcvcjzzwx" and value "hwliiq" along with timestamp = 16
# print(kv.set("wtgbfvg","vrobykydll",17)) # store the key "wtgbfvg" and value "vrobykydll" along with timestamp = 17
# print(kv.set("hwliiq","gzsiivks",18)) # store the key "hwliiq" and value "gzsiivks" along with timestamp = 18
# print(kv.get("kcvcjzzwx", 19)) # output "hwliiq"
# print(kv.get("ztpearaw", 20)) # output "zondoubtib"
# pass

# Runtime: 824 ms, faster than 30.11% of Python3 online submissions for Time Based Key-Value Store.
# Memory Usage: 76.6 MB, less than 5.10% of Python3 online submissions for Time Based Key-Value Store.


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

