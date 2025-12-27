class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)
        capacity.sort(reverse=True)
        for i,c in enumerate(capacity):
            total -= c
            if (total <= 0 ):return i+1
<<<<<<< HEAD
        
=======
>>>>>>> 1d45c9dd0d618a022dedd19453125103c4456745
