class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if nr >= 0 and nc >= 0 and nr < ROWS and nc < COLS and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))