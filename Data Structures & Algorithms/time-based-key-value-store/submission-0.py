class TimeMap:
    # {
    #     'status': [[10, 'happy'], [20, 'sad']]
    # }

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        values = self.store.get(key)
        if not values: return ''
        res = ''
        #Binary Search
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l+r)//2
            # Timestamp found
            if values[mid][0] == timestamp: return values[mid][1]
            # Timestamp less than given timestamp -> look right
            elif values[mid][0] < timestamp:
                res = values[mid][1]
                l = mid + 1
            # Timestamp greater than given one -> look left
            elif values[mid][0] > timestamp: r = mid - 1
        return res