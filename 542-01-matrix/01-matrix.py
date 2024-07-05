class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        output = [[float('inf')]*cols for _ in range(rows)]
        fifo = deque()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    output[r][c] = 0
                    fifo.append((r,c))

        
        neighbors = [(1,0), (-1, 0), (0, 1), (0, -1)]

        while fifo:
            curr_r, curr_c = fifo.popleft()

            for neigh_r, neigh_c in neighbors:
                
                neigh_r, neigh_c = neigh_r + curr_r, neigh_c + curr_c
                distance = 1 + output[curr_r][curr_c]

                if 0 <= neigh_r < rows and 0 <= neigh_c < cols and (distance < output[neigh_r][neigh_c]):
                    output[neigh_r][neigh_c] = distance
                    fifo.append((neigh_r, neigh_c))

        return output
