class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        def dfs(path=''):
            if len(res) == k: return
            if len(path) == n: return res.append(path)
            
            for x in 'abc':
                if not path or x != path[-1]:
                    dfs(path+x)
        
        res = []
        dfs()
        return res[-1] if len(res) == k else ''
