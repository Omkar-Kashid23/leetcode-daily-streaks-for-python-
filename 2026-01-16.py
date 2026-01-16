class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences = [1] + hFences + [m]
        vFences = [1] + vFences + [n]
        sorted_h = sorted([abs(x-y) for x, y in combinations(hFences, 2)], reverse = True)
        vFences_set = set(abs(x-y) for x, y in combinations(vFences, 2))
        
        for v in sorted_h:
            if v in vFences_set:
                return (v**2) % (10**9 + 7)
        return -1
                
