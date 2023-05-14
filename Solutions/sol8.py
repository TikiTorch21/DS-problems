board = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]


def valid_solution(board):
    """
    Function to check for a valid
    sudoku solution

    Parameters
    ----------
    board : list
            Sudoku board.

    Returns
    -------
    bool
            True if all the nested functions
            are True
    """

    def verify_nums(board):
        for seq in board:
            for index, num in enumerate(seq):
                if num in seq[index + 1 :]:
                    return False
        return True

    def board_T(board):
        return list(map(list, zip(*board)))

    def square_cr(board):
        # Set up coordinates

        indices = [(x % 3, x // 3) for x in range(9)]

        boxes = [
            [board[out_x * 3 + ins_x][out_y * 3 + ins_y] for ins_x, ins_y in indices]
            for out_x, out_y in indices
        ]
        return boxes

    return (
        verify_nums(board)
        and verify_nums(board_T(board))
        and verify_nums(square_cr(board))
    )


print(f"Using approach 1:\n\t{valid_solution(board)}")

######################################################

"""
Solutions
---------
Using approach 1:
	True
"""
