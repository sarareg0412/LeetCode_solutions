class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])

        output = [[float('inf')] *cols for _ in range(rows)]

        neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        fifo = deque()

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    fifo.append((i, j))
                    output[i][j] = 0

        while fifo:
            r, c = fifo.popleft()

            for nx, ny in neighbours:
                r_n, c_n = r + nx, c + ny

                if 0 <= r_n < rows and 0 <= c_n < cols:
                    new_dist = 1 + output[r][c]

                    if new_dist < output[r_n][c_n]:
                        output[r_n][c_n] = new_dist
                        fifo.append((r_n, c_n))

        return output