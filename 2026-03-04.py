class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        cnt = 0
        transpose_mat = [list(row) for row in zip(*mat)]
        for i in range(len(mat)):
            count_one = mat[i].count(1)
            if count_one == 1:
                j = mat[i].index(1)
                column_count = transpose_mat[j].count(1)
                if column_count == 1:
                    cnt += 1
        return cnt
