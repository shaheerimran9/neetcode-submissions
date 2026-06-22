class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        res = []

        for num in nums:
            counts[num] += 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for n, c in counts.items():
            buckets[c].append(n)

        for i in range(len(buckets) -1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res