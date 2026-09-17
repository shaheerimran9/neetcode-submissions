class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        freq_buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in counts.items():
            freq_buckets[count].append(num)

        for freq in range(len(freq_buckets)-1, 0, -1):
            for num in freq_buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res