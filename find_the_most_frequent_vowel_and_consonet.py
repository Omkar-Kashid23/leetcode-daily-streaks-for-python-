class Solution:
    def maxFreqSum(self, s: str) -> int:
        
        from collections import defaultdict
        freq_map = defaultdict(int)
        for char in s:
            freq_map[char] += 1
        
        vowel_max = 0
        consonant_max = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        for key, value in freq_map.items():
            if key in vowels:
                if value > vowel_max:
                    vowel_max = value
            else:
                if value > consonant_max:
                    consonant_max = value
        
        return vowel_max + consonant_max
            
        
