class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        beams,prev =0,0
        for row in bank:
            de = row.count("1")
            if de:
                beams += prev * de
                prev = de
        return beams
