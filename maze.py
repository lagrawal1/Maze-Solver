from tkinter import Tk, BOTH, Canvas
from window import Window
from graphics import Line, Point, Cell
import time


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win

        self._create_cells()

    def _create_cells(self):
        self._cells = [
            [[] for i in range(self.__num_rows)] for i in range(self.__num_cols)
        ]

        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self._cells[i][j] = Cell(self.__win)

        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self._draw_cell(i, j)
        self._break_entrance_and_exit()

    def _draw_cell(self, i, j):
        cell = self._cells[i][j]
        if self.__win == None:
            return
        cell.draw(
            Point(
                self.__x1 + (j) * self.__cell_size_x,
                self.__y1 + (i) * self.__cell_size_y,
            ),
            Point(
                self.__x1 + (j + 1) * self.__cell_size_x,
                self.__y1 + (i + 1) * self.__cell_size_y,
            ),
        )
        self._animate()

    def _animate(self):
        if self.__win == None:
            return
        self.__win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].top_wall = False
        self._draw_cell(0, 0)
        print(self._cells[0][0].top_wall)
        self._cells[self.__num_cols - 1][self.__num_rows - 1].bottom_wall = False
        self._draw_cell(self.__num_cols - 1, self.__num_rows - 1)
