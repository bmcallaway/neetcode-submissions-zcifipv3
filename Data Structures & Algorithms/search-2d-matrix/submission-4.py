class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        array = [
            [1, 2, 3],
            [4, 5, 6]
        ]

        l = 0
        r = len(matrix) - 1
        m = (r-l) % 2
        print("m1:",m)
        print("test:",matrix[m][0])
        while l < r:
            print("m1:",m)
            if matrix[m][0] > target:
                r = m - 1
            elif matrix[m][0] < target:
                l = m
                if matrix[m][len(matrix[m]) - 1] > target:
                    r = m
                elif matrix[m][len(matrix[m]) - 1] < target:
                    l = m + 1
                elif matrix[m][len(matrix[m]) - 1] == target:
                    return True
            elif matrix[m][0] == target:
                return True
            m = l + ((r-l) % 2)
        row = m
        if row >= len(matrix):
            return False
        print("row:",row)
        l = 0
        r = len(matrix[0]) - 1
        m = (r-l) % 2
        while l <= r:
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] < target:
                l = m + 1
            elif matrix[row][m] > target:
                r = m - 1
            m = l + ((r-l) % 2)
        print("m:",m)
        return False