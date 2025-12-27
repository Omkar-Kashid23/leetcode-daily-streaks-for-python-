from heapq import heapify, heappop, heappush
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # Sort by start time
        meetings.sort(key=lambda x: x[0])
        
        used = [0] * n
        
        # available rooms by smallest index
        avail = list(range(n))
        heapify(avail)
        
        busy = []
        
        for start, end in meetings:
            # Free up rooms that have finished by the current meeting's start time
            while busy and busy[0][0] <= start:
                _, room = heappop(busy)
                heappush(avail, room)
                
            if avail:
                # Case 1: Room available
                room = heappop(avail)
                heappush(busy, (end, room))
                used[room] += 1
            else:
                # Case 2: No room available (Delay)
                dur = end - start
                endTime, room = heappop(busy)
                heappush(busy, (endTime + dur, room))
                used[room] += 1
        
        # Single-pass to find max room (faster than .index(max(...)))
        maxRoom = 0
        maxCount = 0
        for i in range(n):
            if used[i] > maxCount:
                maxCount = used[i]
                maxRoom = i
                
        return maxRoom