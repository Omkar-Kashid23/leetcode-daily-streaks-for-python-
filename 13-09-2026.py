class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        a_point, b_point, d = [], [], collections.defaultdict(int)
        
        for i in range(len(img1)):
            for j in range(len(img1[0])):
                if img1[i][j]: a_point.append((i, j))
                if img2[i][j]: b_point.append((i, j))
                
        for i_1, j_1 in a_point:
            for i_2, j_2 in b_point:
                # Corrected: j_2 - j_1
                d[(i_2 - i_1, j_2 - j_1)] += 1 
                
        return max(d.values() or [0])
