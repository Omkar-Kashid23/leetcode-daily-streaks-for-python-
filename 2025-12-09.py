class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        dic={}
        dic2={}
        res=0
        for num in nums:
            if num%2==0 and num//2 in dic2:
                res+=dic2[num//2]
                res%=10**9+7
            if num*2 in dic:
                if num in dic2:
                    dic2[num]+=dic[num*2]
                else:
                    dic2[num]=dic[num*2]
            if num in dic:
                dic[num]+=1
            else:
                dic[num]=1
        return res