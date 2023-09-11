from typing import List, Optional, Tuple


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for r in range(len(board)):
            for c in range(len(board[0])):
                if self.helper(board, word, (r, c)):
                    return True
        return False

    def helper(
        self,
        board: List[List[Optional[str]]],
        word: str,
        curr: Tuple[int, int],
    ) -> bool:
        print(curr, word)
        if len(word) == 0:
            return True
        if len(word) == 1:
            return board[curr[0]][curr[1]] == word[0]
        if board[curr[0]][curr[1]] != word[0]:
            return False
        letter = board[curr[0]][curr[1]]
        board[curr[0]][curr[1]] = None
        next_word = word[1:]
        res = curr[1] > 0 and self.helper(
            board,
            next_word,
            (curr[0], curr[1] - 1),
        )
        if not res:
            res = curr[1] < len(board[0]) - 1 and self.helper(
                board, next_word, (curr[0], curr[1] + 1)
            )
        if not res:
            res = curr[0] > 0 and self.helper(
                board,
                next_word,
                (curr[0] - 1, curr[1]),
            )
        if not res:
            res = curr[0] < len(board) - 1 and self.helper(
                board, next_word, (curr[0] + 1, curr[1])
            )
        board[curr[0]][curr[1]] = letter
        return res


print(
    Solution().exist(
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        "ABCCED",
    )
)
