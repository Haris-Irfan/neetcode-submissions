class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check rows for duplicates
        for i in range(len(board)):
            print("Row: ", i)
            rowCheck = set()
            for j in range(len(board[i])):
                print("Column: ", j)
                num = board[i][j]
                if num == ".":
                    continue
                if num in rowCheck:
                    print("Row Check Failed")
                    return False
                rowCheck.add(num)
        
        # Check columns for duplicates
        for i in range(len(board[0])):
            colCheck = set()
            for j in range(len(board)):
                num = board[j][i]
                if num == ".":
                    continue
                if num in colCheck:
                    print("Column Check Failed!")
                    return False
                colCheck.add(num)

        # Check 3x3 square
        for rowStart in range(0, len(board[0]), 3):
            for colStart in range(0, len(board), 3):
                gridCheck = set()
                for rowIndex in range(3):
                    squareRow = rowStart + rowIndex
                    for colIndex in range(3):
                        squareCol = colStart + colIndex
                        num = board[squareRow][squareCol]
                        if num == ".":
                            continue
                        if num in gridCheck:
                            print("Grid Check Failed!")
                            return False
                        gridCheck.add(num)
        
        return True

                


