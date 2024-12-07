class Board:
    def __init__(self):
        self.grid = [[" " for _ in range(3)] for _ in range(3)]

    def draw_board(self):
        """
        Draw the board of Tic-Tac-Toe game
        """
        size = len(self.grid)
        for row in range(size):
            print(" ---" * size)
            row_content = "|"
            for col in range(size):
                row_content += f" {self.grid[row][col]} |"
            print(row_content)
        print(" ---" * size)


    def update_board(self, row: int, col: int, symbol: str) -> bool:
        """
        Update the game board based on location selected by player

        Args:
            row (int): row index of board
            col (int): column index of board
            symbol (str): symbol used by player
        """
        if self.grid[row][col] == " ":
            self.grid[row][col] = symbol
            return True
        return False

    def check_winner(self) -> str:
        """
        Check the winner of the current board

        Returns:
            str: The winning symbol ('X' or 'O') if there is a winner, else an empty string
        """
        for row in self.grid:
            if row[0] == row[1] == row[2] and row[0] != ' ':
                return row[0]

        for col in range(3):
            if self.grid[0][col] == self.grid[1][col] == self.grid[2][col] and self.grid[0][col] != ' ':
                return self.grid[0][col]

        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] and self.grid[0][0] != ' ':
            return self.grid[0][0]
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] and self.grid[0][2] != ' ':
            return self.grid[0][2]

        return ""
    
    def is_full(self) -> bool:
        """
        Check if the current board is full or not

        Returns:
            bool: Boolean outcome indicating whether the board is full
        """
        return all(cell != " " for row in self.grid for cell in row)
