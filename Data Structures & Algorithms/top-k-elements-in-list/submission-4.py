class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Input -> Array nums, int k
        #Output -> Return k most frequent elements in array

        #Approach 1:
        #We can use a dict to map number -> frequencies
        #Sort the frequencies in the dict and return the k most frequent
        #Sorting costs O(nlogn) time through

        #Approach 2:
        #We can still use the dict to map number -> frequencies
        #Use frequency buckets to hold the numbers with their frequencies
        #Pick the top k numbers from the buckets start the end (most freq.)

        res = []
        #Dict mapping number -> frequencies
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        #Frequency buckets [ [], [], [], ... ]
        frequencies = [[] for _ in range(len(nums) + 1)]

        #Populate frequency buckets using dict
        for n, c in counts.items():
            frequencies[c].append(n)
        
        #Get the k most frequent from buckets
        for i in range(len(frequencies) - 1, 0, -1):
            for num in frequencies[i]:
                res.append(num)
                if len(res) == k:
                    return res
                    
        return res
        