class Solution:
    def processStr(self, s: str, k: int) -> str:
        lengths = []
        curr_len = 0
        
        # ---------------------------------------------------------
        # STEP 1: THE FORWARD PASS (Building the "Logbook")
        # We don't build the string, we just record how big it gets.
        # ---------------------------------------------------------
        for char in s:
            if char.isalpha():
                curr_len += 1
            elif char == '*':
                curr_len = max(0, curr_len - 1) # Prevent going below 0
            elif char == '#':
                curr_len *= 2
            elif char == '%':
                pass # Reversing doesn't change the size
            
            lengths.append(curr_len)
            
        # ---------------------------------------------------------
        # STEP 2: BOUNDS CHECK
        # ---------------------------------------------------------
        # If k is greater than or equal to the final length, it's invalid.
        if k >= lengths[-1]:
            return "."
            
        # ---------------------------------------------------------
        # STEP 3: THE BACKWARD PASS (Tracing 'k' to its origin)
        # ---------------------------------------------------------
        for i in range(len(s) - 1, -1, -1):
            # What was the size of the string BEFORE this operation?
            prev_len = lengths[i - 1] if i > 0 else 0
            char = s[i]
            
            if char.isalpha():
                # A letter is always added exactly at index `prev_len`
                if k == prev_len:
                    return char
                
            elif char == '#':
                # If k is in the fake/cloned second half, trace it back to the original
                if k >= prev_len:
                    k -= prev_len
                    
            elif char == '%':
                # The string was flipped, so we mirror k's position
                k = (prev_len - 1) - k
                
            elif char == '*':
                # A star deleted the character at the very end. 
                # Since k must be a valid index *before* the deletion to survive this far, 
                # the deletion at the end doesn't affect k's position at all.
                pass 
                
        return "."