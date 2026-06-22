class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # array -> nums
        # int -> k
        # return k most frequent -> returning top k frequent nums

        res = []
        count = defaultdict(int)
        buckets = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] += 1
        
        for n, c in count.items():
            buckets[c].append(n)
        
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                if len(res) == k:
                    break
                res.append(n)
        return res
