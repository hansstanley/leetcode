from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        memo = set(range(len(rooms)))
        stack = [0]
        while len(stack) > 0:
            room = stack.pop()
            if room not in memo: continue
            memo.discard(room)
            stack.extend(rooms[room])
        return len(memo) == 0