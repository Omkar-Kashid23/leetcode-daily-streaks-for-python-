class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        # Step 1: Create a hash set for O(1) lookups
        num_set = set(nums)
        
        # Step 2: Enumerate multiples of k
        i = 1
        while True:
            candidate = k * i
            
            # Step 3: First missing multiple is our answer
            if candidate not in num_set:
                return candidate
            
            i += 1
