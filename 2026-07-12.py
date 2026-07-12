class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        # Step 1: Remove duplicates and sort
        unique_sorted = sorted(set(arr))
        
        # Step 2: Map each unique value to its rank
        # enumerate gives us (index, value). 
        # We add 1 to the index because ranks start at 1, not 0.
        rank_map = {val: i + 1 for i, val in enumerate(unique_sorted)}
        
        # Step 3: Replace each original element with its rank
        return [rank_map[num] for num in arr]
