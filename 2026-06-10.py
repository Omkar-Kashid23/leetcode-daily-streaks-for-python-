from collections import deque

class Solution:
    def maxTotalValue(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # Helper function to count subarrays with (max - min) >= V
        def count_ge(V):
            if V <= 0:
                return n * (n + 1) // 2
            max_q = deque()
            min_q = deque()
            r = 0
            ans = 0
            for l in range(n):
                while r < n:
                    if max_q and min_q and nums[max_q[0]] - nums[min_q[0]] >= V:
                        break
                    while max_q and nums[max_q[-1]] <= nums[r]:
                        max_q.pop()
                    max_q.append(r)
                    while min_q and nums[min_q[-1]] >= nums[r]:
                        min_q.pop()
                    min_q.append(r)
                    r += 1
                    
                if max_q and min_q and nums[max_q[0]] - nums[min_q[0]] >= V:
                    ans += (n - r + 1)
                    
                if max_q and max_q[0] == l:
                    max_q.popleft()
                if min_q and min_q[0] == l:
                    min_q.popleft()
            return ans

        # 1. Binary Search for the threshold value V
        low = 0
        high = max(nums) - min(nums)
        ans_V = 0
        
        while low <= high:
            mid = (low + high) // 2
            if count_ge(mid) >= k:
                ans_V = mid
                low = mid + 1
            else:
                high = mid - 1
                
        # 2. Build a Sparse Table for O(1) range max/min queries
        K = n.bit_length()
        st_max = [[0] * n for _ in range(K)]
        st_min = [[0] * n for _ in range(K)]
        for j in range(n):
            st_max[0][j] = nums[j]
            st_min[0][j] = nums[j]
        for i in range(1, K):
            length = 1 << (i - 1)
            for j in range(n - (1 << i) + 1):
                st_max[i][j] = max(st_max[i-1][j], st_max[i-1][j + length])
                st_min[i][j] = min(st_min[i-1][j], st_min[i-1][j + length])
                
        def query_val(L, R):
            length = R - L + 1
            i = length.bit_length() - 1
            mx = max(st_max[i][L], st_max[i][R - (1 << i) + 1])
            mn = min(st_min[i][L], st_min[i][R - (1 << i) + 1])
            return mx - mn

        # 3. Collect and sum subarrays with value >= ans_V + 1
        target_V = ans_V + 1
        total_sum = 0
        collected_count = 0
        
        max_q = deque()
        min_q = deque()
        r = 0
        for l in range(n):
            while r < n:
                if max_q and min_q and nums[max_q[0]] - nums[min_q[0]] >= target_V:
                    break
                while max_q and nums[max_q[-1]] <= nums[r]:
                    max_q.pop()
                max_q.append(r)
                while min_q and nums[min_q[-1]] >= nums[r]:
                    min_q.pop()
                min_q.append(r)
                r += 1
                
            if max_q and min_q and nums[max_q[0]] - nums[min_q[0]] >= target_V:
                # All right endpoints from r - 1 to n - 1 are valid
                for R in range(r - 1, n):
                    total_sum += query_val(l, R)
                    collected_count += 1
                    
            if max_q and max_q[0] == l:
                max_q.popleft()
            if min_q and min_q[0] == l:
                min_q.popleft()
                
        # 4. Fill the remaining spots with subarrays having exactly the threshold value
        remaining = k - collected_count
        total_sum += remaining * ans_V
        
        return total_sum
