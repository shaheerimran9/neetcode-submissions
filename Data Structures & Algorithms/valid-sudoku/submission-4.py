class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Input -> 9x9 board
        # Output -> Return true if board is valid || False if not valid
        
        # Rules:
            # Each ROW must not contain any duplicates
            # Each COL must not contain any duplicates
            # Each BOX must not contain any duplicates

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                cell = board[r][c]
                if cell == '.':
                    continue

                if (cell in rows[r] or 
                    cell in cols[c] or 
                    cell in boxes[(r//3, c//3)]): 
                    return False
                else:
                    rows[r].add(cell)
                    cols[c].add(cell)
                    boxes[(r//3, c//3)].add(cell)
        return True
                    

                    