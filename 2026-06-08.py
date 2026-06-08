class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lst1 = []
        lst2 = []
        lst3 = []
        for i in nums:
            if i < pivot:lst1.append(i)
            elif i == pivot:lst3.append(i)
            else:lst2.append(i)
        return lst1 + lst3 + lst2
