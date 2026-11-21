class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == ".":
                    continue

                r_tag = (r, value)
                c_tag = (value, c)
                grid = (r // 3, c // 3, value)
                if (r_tag in seen) or (c_tag in seen) or (grid in seen):
                    return False
                seen.add(r_tag)
                seen.add(c_tag)
                seen.add(grid)

        return True
