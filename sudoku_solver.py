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
        for i in range(len(self.matrix)):
            column = [row[i] for row in self.matrix]
            #extract only the valid values
            numbers = [s for s in column if s != 0]
            #check for duplicates (len list != len set)
            if len(numbers) != len(set(numbers)):
                return False
                break
        else:
            return True



    