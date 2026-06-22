class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # array -> nums
        # int -> k
        # return k most frequent -> returning top k frequent nums

        # Initialize hashmap -> {num: freq}
        # Loop through nums
            # Increment frequency for each num

        # Create buckets for each frequency max till len(nums)
        # Reverse loop through buckets
            # While len(res) <= k:
                # Append num to res array

        res = []
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        buckets = [[] for i in range(len(nums) + 1)]
        for n, c in counts.items():
            buckets[c].append(n)

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res