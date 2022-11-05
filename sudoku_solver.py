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
                    square.extend(self.matrix[(3*j)+k][3*i:(3*i)+3])
                #extract only the valid values
                square_list = [item for sublist in square for item in sublist]
                numbers = [s for s in square_list if s != 0]
                
                #check for duplicates (len list != len set)
                if len(numbers) != len(set(numbers)):
                    valid = False
                    break
        return valid

    def check_valid(self):
        #combines all the checks in one function
        if (self.check_columns() and self.check_rows() and self.check_squares() == True):
            return True

        else:
            return False



    def Complete(self, row, column):
        #recursive function to try a number
        
        if (row == 8 and column == 9):
            return True

        if column == 9:
            row += 1
            column = 0

        if self.matrix[row][column] != 0:
            return self.Complete(row, column + 1)

        for num in range (1, 10, 1):
            
            self.matrix[row][column] = num
            if self.check_valid():
                if self.Complete(row, column + 1):
                    return True
            self.matrix[row][column] = 0

        return False

        



    def Solve(self):
        #function to solve the sudoku
        
        self.Complete(0,0)
            
        print("the sudoku is solved!")
        self.print_sudoku()
        
        
    def print_sudoku(self):
        for row in self.matrix:
            print(row)
         




if __name__ == "__main__":

    sudoku3 = Sudoku(
        [
            [2, 5, 1, 4, 3, 6, 9, 7, 8],
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

    sudoku3.print_sudoku()
    sudoku3.Solve()

    

    

    