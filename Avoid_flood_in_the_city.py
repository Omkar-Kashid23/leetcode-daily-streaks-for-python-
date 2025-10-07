class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        f, stk, res = {}, [], [1] * len(rains)
        for i, v in enumerate(rains):
            if v == 0:
                stk.append(i)
                continue
            res[i] = -1
            if v in f: 
                if (p := bisect.bisect(stk, f[v])) == len(stk):
                    return []
                res[stk.pop(p)] = v
            f[v] = i
        return res 
