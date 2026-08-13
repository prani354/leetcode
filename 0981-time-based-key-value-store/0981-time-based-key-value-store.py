from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        t_store = self.map.get(key,[])
        l,h = 0, len(t_store)-1

        while l <= h:
            m = (l+h) // 2

            if t_store[m][0] <= timestamp:
                res = t_store[m][1]
                l = m + 1
            else:
                h = m - 1

        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)