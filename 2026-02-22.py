class Solution:
    def binaryGap(self, n: int) -> int:
        # Convert to binary string, removing the '0b' prefix
        binary_str = bin(n)[2:]
        
        # Store the positions of all '1's
        indices = [i for i, digit in enumerate(binary_str) if digit == '1']
        
        # If there's fewer than two '1's, the gap is 0
        if len(indices) < 2:
            return 0
        
        # Find the max difference between consecutive indices
        max_gap = 0
        for k in range(len(indices) - 1):
            dist = indices[k+1] - indices[k]
            if dist > max_gap:
                max_gap = dist
                
        return max_gap
