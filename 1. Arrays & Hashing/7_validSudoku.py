class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # counting y down
        col_dict = {k:set() for k in range(9)}
        grid_dict = {}
        for i in range(9):
            # counting x to the right
            row_set = set()
            for j in range(9):
                curr = board[i][j]
                if curr != ".":
                    if curr in row_set:
                        return False
                    row_set.add(curr)
                    if curr in col_dict[j]:
                        return False
                    col_dict[j].add(curr)
                    a = i//3
                    b = j//3
                    tup = (a, b)
                    if tup in grid_dict:
                        if curr in grid_dict[tup]:
                            return False
                        grid_dict[tup].add(curr)
                    else:
                        grid_dict[tup] = set(curr)
        print(grid_dict)
        return True