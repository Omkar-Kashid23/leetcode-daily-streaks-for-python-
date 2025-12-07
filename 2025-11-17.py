from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        # Get the indices of all occurrences of 1 in the list
        indices_of_ones = [i for i, x in enumerate(nums) if x == 1]

        # If there are 0 or 1 instances of 1, the condition is always met.
        if len(indices_of_ones) < 2:
            return True

        # Iterate through the indices list starting from the second element
        for i in range(1, len(indices_of_ones)):
            # Calculate the distance between the current '1' and the previous '1'
            distance = indices_of_ones[i] - indices_of_ones[i-1]
            
            # If the distance is less than or equal to k, the condition is violated
            if distance <= k:
                return False

        # If the loop completes without finding any violations, the condition is met
        return True
