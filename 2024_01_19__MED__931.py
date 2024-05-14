"""
Title: 
931. Minimum Falling Path Sum

Description: 
    Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.
    A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

Example:
    Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
    Output: 13
    Explanation: There are two falling paths with a minimum sum as shown.
    
    Input: matrix = [[-19,57],[-40,-5]]
    Output: -59
    Explanation: The falling path with a minimum sum is shown.
    
Constraints:
    n == matrix.length == matrix[i].length
    1 <= n <= 100
    -100 <= matrix[i][j] <= 100

"""


class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        
        # Dynamic Programming - bottom up

        num_of_rows = len(matrix)
        num_of_columns = len(matrix[0])

        # loop over rows in the matrix
        for row_index in range(1, num_of_rows):

            # loop over each column in a row
            for column_index in range(num_of_columns):
                
                # Always consider the middle path above for a potential minimum path
                temp_min = matrix[row_index - 1][column_index] + \
                           matrix[row_index][column_index]

                # if there is a left diagonal we can access, calcuate a  cost
                if column_index - 1 >= 0:
                    temp_min = min(
                        temp_min, 
                        matrix[row_index - 1][column_index - 1] + 
                        matrix[row_index][column_index]
                    )
                
                # if there is a right diagonal we can access, calcuate a  cost
                if column_index + 1 <= num_of_columns - 1:
                    temp_min = min(
                        temp_min,
                        matrix[row_index - 1][column_index + 1] + 
                        matrix[row_index][column_index]
                    )
                
                # set the new cheapest path cost
                matrix[row_index][column_index] = temp_min
        
        return min(matrix[-1])



if __name__ == "__main__":
    sol = Solution()
    
    matrix = [[2,1,3],[6,5,4],[7,8,9]]      # -> 13
    # matrix = [[-19,57],[-40,-5]]            # -> -59


    print(sol.minFallingPathSum(matrix=matrix))
