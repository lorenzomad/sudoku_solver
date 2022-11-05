import numpy as np

class Sudoku:
    # class to instatiate a sudoku object with the values given in 9*9 array matrix
    def __init__(self, matrix):
        self.matrix = matrix

    def check_rows(self):
        for row in self.matrix:
            #extract only the valid values
            numbers = [s for s in row if s != 0]
            #check for duplicates (len list != len set)
            if len(numbers) != len(set(numbers)):
                return False
                break
        else: 
            return True
    
    def check_columns(self):
        for i in range(9):
            column = [row[i] for row in self.matrix]
            #extract only the valid values
            numbers = [s for s in column if s != 0]
            #check for duplicates (len list != len set)
            if len(numbers) != len(set(numbers)):
                return False
                break
        else:
            return True

    def check_squares(self):
        valid = True
        #i iterates on the rows
        for i in range(3):
            #j iterates on the columns
            for j in range(3):
                square = []
                #k iterates on the single square lines
                for k in range(3):
                    square.extend([self.matrix[(3*j)+k][3*i:(3*i)+3]])
                #extract only the valid values
                square_list = [item for sublist in square for item in sublist]
                numbers = [s for s in square_list if s != 0]
                
                #check for duplicates (len list != len set)
                if len(numbers) != len(set(numbers)):
                    valid = False
                    break
        return valid



if __name__ == "__main__":

    sudoku3 = Sudoku(
        [
            [2, 5, 0, 0, 3, 0, 9, 0, 1],
            [0, 1, 0, 0, 0, 4, 0, 0, 0],
            [4, 0, 7, 0, 0, 0, 2, 0, 8],
            [0, 0, 5, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 9, 8, 1, 0, 0],
            [0, 4, 0, 0, 0, 3, 0, 0, 0],
            [0, 0, 0, 3, 6, 0, 0, 7, 2],
            [0, 7, 0, 0, 0, 0, 0, 0, 3],
            [9, 0, 3, 0, 0, 0, 6, 0, 4]
        ]
    )

    sudoku3.check_squares()

    