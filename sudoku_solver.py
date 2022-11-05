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
        #iterate on the row
        for i in range(3):
            square = []
            #iterate on the column
            for j in range(3):
                square.extend([self.matrix[j][3*i:(3*i)+3]])
                #extract only the valid values
                numbers = list([s for s in square if s != 0])
                #check for duplicates (len list != len set)
                print(numbers)
                if len(numbers) != len(set(numbers)):
                    return False
                    break
            else:
                continue
        else:
            return True




    