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


    def Complete(self):
        #recursive function to try a number
        
        solved = False    
        
        while solved == False: 
            #decide which value ot try as input 
            for row in self.matrix:
                if 0 in row:
                    row_value= self.matrix.index(row)
                    column_value = row.index(0)

                    square_row = row_value // 3
                    square_column = column_value // 3
                    
                    #this set will remember the numbers which are in the 
                    #same row column or square
                    numbers = set()

                    #add the elements for the corresponding row
                    for element in row:
                        numbers.add(element)
                    column = [row[column_value] for row in self.matrix]
                    
                    #add the elements for the corresponding column
                    for element in column:
                        numbers.add(element)

                    # add the elements for the corresponding square
                    for k in range(3):
                        line = self.matrix[(3*(square_row))+k][3*square_column:(3*square_column)+3]
                        numbers.update(line)

                    all_numbers = {1,2,3,4,5,6,7,8,9}

                    possible = list(all_numbers.difference(numbers))

                    

                else:
                    solved = True


    def Solve(self):
        #function to solve the sudoku
        
        self.Complete()
            
        print("the sudoku is solved!")
        self.print_sudoku()
        
        
    def print_sudoku(self):
        pass
        #need to write it 




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

    sudoku3.Solve()

    

    

    