class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        lst = []
        res = []
        arr.sort()
        for i in range(0,len(arr)-1):
            k = arr[i+1] - arr[i]
            lst += [k]
        min_value = min(lst)
        for i in range(0,len(arr)-1):
            ans = arr[i+1] - arr[i]
            if ans == min_value:
                kes = [arr[i],arr[i+1]]
                res.extend([kes])
        return res