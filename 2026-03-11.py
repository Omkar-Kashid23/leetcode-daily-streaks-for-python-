class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # Edge case: The constraints say n can be 0. 
        # 0 in binary is '0', so its complement must be '1'.
        if n == 0:
            return 1
            
        # Create a mask of all 1s that is the same length as n
        mask = (1 << n.bit_length()) - 1
        
        # XOR n with the mask to flip all the bits
        return n ^ mask
