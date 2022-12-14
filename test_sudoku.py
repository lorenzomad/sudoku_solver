import pytest
from sudoku_solver import Sudoku


def test_check_lines():

    sudoku1 = Sudoku(
        [
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9]
        ]
    )

    assert sudoku1.check_rows() == True
    assert sudoku1.check_columns() == False
    assert sudoku1.check_squares() == False

    sudoku2 = Sudoku(
        [
            [1,0,3,0,5,0,7,0,9],
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9]
        ]
    )
    assert sudoku2.check_rows() == True
    assert sudoku2.Solve() == False

    sudoku3 = Sudoku(
        [
            [2, 5, 0, 0, 3, 0, 9, 0, 1],
            [0, 1, 0, 0, 0, 4, 0, 0, 0],
            [4, 6, 7, 0, 0, 0, 2, 0, 8],
            [0, 0, 5, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 9, 8, 1, 0, 0],
            [0, 4, 0, 0, 0, 3, 0, 0, 0],
            [0, 0, 0, 3, 6, 0, 0, 7, 2],
            [0, 7, 0, 0, 0, 0, 0, 0, 3],
            [9, 0, 3, 0, 0, 0, 6, 0, 4]
        ]
    )

    assert sudoku3.check_columns() == True
    assert sudoku3.check_rows() == True
    assert sudoku3.check_squares() == True
    assert sudoku3.Solve() == False

    sudoku4 = Sudoku(
        [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    )


    assert sudoku4.check_valid() == True

    sudoku4.Solve()

    assert sudoku4.check_valid() == True

    sudoku5 = Sudoku(
        [[9, 0, 4, 5, 3, 0, 6, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 7, 0, 0, 4],
        [5, 6, 0, 0, 7, 0, 9, 0, 0],
        [0, 0, 9, 1, 0, 0, 7, 0, 6],
        [3, 7, 0, 9, 0, 0, 0, 0, 1],
        [0, 3, 2, 0, 0, 0, 1, 0, 0],
        [0, 0, 5, 0, 0, 8, 0, 0, 9],
        [0, 0, 0, 0, 5, 0, 0, 4, 0]]
    )

    assert sudoku5.Solve() == True

