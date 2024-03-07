from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, i, j, visited):
            m, n = len(grid), len(grid[0])
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0' or visited[i][j]:
                return
            visited[i][j] = True
            dfs(grid, i + 1, j, visited)
            dfs(grid, i - 1, j, visited)
            dfs(grid, i, j + 1, visited)
            dfs(grid, i, j - 1, visited)

            return

        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    count += 1
                    dfs(grid, i, j, visited)
        return count


if __name__ == '__main__':
    s = Solution()
    grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    print(s.numIslands(grid))