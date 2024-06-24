class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for i in range(numRows):  # Outer loop runs numRows times
            row = [1] * (i + 1)
            
            for j in range(1, i):  # Inner loop runs i - 1 times
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            
            triangle.append(row)
        
        return triangle