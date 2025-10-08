"""Programms run life games."""
import numpy as np
from matplotlib import pyplot
from scipy.signal import convolve2d

glider = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]])

blinker = np.array([
    [0, 0, 0],
    [1, 1, 1],
    [0, 0, 0]]
        )

glider_gun = np.array([
    [0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0]
])


class Game:
    """It is the life games."""

    def __init__(self, size):
        self.board = np.zeros((size, size))

    def play(self):
        """Start the games."""
        print("Playing life. Press ctrl + c to stop.")
        pyplot.ion()
        while True:
            self.move()
            self.show()
            pyplot.pause(0.0000005)

    def move(self):
        """Conduct the games."""
        stencil = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        neighbourcount = convolve2d(self.board, stencil, mode='same')

        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                self.board[i, j] = 1 if (
                    neighbourcount[i, j] == 3 or (neighbourcount[i, j] == 2
                                                  and self.board[i, j])) else 0

    def __setitem__(self, key, value):
        """Assign the values."""
        self.board[key] = value

    def show(self):
        """Show the result."""
        pyplot.clf()
        pyplot.matshow(self.board, fignum=0, cmap='binary')
        pyplot.show()

    def insert(self, pattern, coord):
        """Insert the pattern with center coordinates."""
        x_length, y_length = pattern.grid.shape[0], pattern.grid.shape[1]
        self.board[coord[0]-(x_length - 1)//2:coord[0]+(x_length + 1)//2,
                   coord[1]-(y_length - 1)//2:coord[1]+(y_length + 1)//2
                   ] = pattern.grid


class Pattern:
    """Show different pattern of glider."""

    def __init__(self, grid):
        self.grid = grid

    def flip_vertical(self):
        """Flip pattern upside down."""
        return Pattern(self.grid[::-1])

    def flip_horizontal(self):
        """Flip pattern left to right."""
        return Pattern(self.grid[:, ::-1])

    def flip_diag(self):
        """Transpose pattern."""
        result = Pattern(self.grid.copy())
        return Pattern(np.transpose(result.grid))

    def rotate(self, n):
        """Rotate pattern n times."""
        result = Pattern(self.grid.copy())
        for i in range(n):
            result = result.flip_diag().flip_vertical()
        return result
