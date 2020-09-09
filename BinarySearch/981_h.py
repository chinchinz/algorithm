class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        bisect.insort_left(self.d[key], (timestamp, value)), (timestamp, value)
        # print(self.d)

    def get(self, key: str, timestamp: int) -> str:
        i = bisect.bisect_left(self.d[key], (timestamp,))
        if i == 0 and self.d[key][0][0] > timestamp: return ''
        if i == len(self.d[key]) or timestamp != self.d[key][i][0] : i -= 1
        return self.d[key][i][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)