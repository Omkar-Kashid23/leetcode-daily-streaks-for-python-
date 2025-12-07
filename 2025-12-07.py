class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # lst = (x for x in range(low,high+1) if x%2!=0)
        # return len(lst)
        is_odd = low % 2 != 0
        total_num = high - low + 1
        if is_odd:
            return (total_num + 1) // 2
        else:return total_num // 2