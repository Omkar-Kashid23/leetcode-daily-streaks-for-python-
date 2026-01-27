class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        rev_adj = defaultdict(list)
        
        for u, v, w in edges:
            adj[u].append((v, w))
            rev_adj[v].append((u, w))
            
        # 2. Dijkstra's Setup
        # min_costs[i] stores the cheapest cost to reach node i
        min_costs = [float('inf')] * n
        min_costs[0] = 0
        
        # Priority Queue stores (current_total_cost, current_node)
        # heapq is a min-heap, so it always pops the lowest cost first
        pq = [(0, 0)]
        
        while pq:
            curr_dist, u = heapq.heappop(pq)
            
            # If we already found a cheaper way to u, skip this
            if curr_dist > min_costs[u]:
                continue
            
            # If we reached the target, we can return immediately 
            # (Dijkstra guarantees the first time we pop a node, it's the min cost)
            if u == n - 1:
                return curr_dist
            
            # 3. Explore Normal Edges (Cost: w)
            for v, w in adj[u]:
                if curr_dist + w < min_costs[v]:
                    min_costs[v] = curr_dist + w
                    heapq.heappush(pq, (min_costs[v], v))
            
            # 4. Explore Reversed Edges (Cost: 2 * w)
            # These are edges that originally pointed INTO u
            for v, w in rev_adj[u]:
                if curr_dist + 2 * w < min_costs[v]:
                    min_costs[v] = curr_dist + 2 * w
                    heapq.heappush(pq, (min_costs[v], v))
        
        # If we exit the loop without reaching n-1
        return min_costs[n-1] if min_costs[n-1] != float('inf') else -1
