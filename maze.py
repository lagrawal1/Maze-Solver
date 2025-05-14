from tkinter import Tk, BOTH, Canvas
from window import Window
from graphics import Line, Point, Cell
import time
import random


class Maze:
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        if seed != None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

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

    def _draw_cell(self, i, j):
        cell = self._cells[i][j]
        if self.__win == None:
            return
        cell.draw(
            Point(
                self.__x1 + (i) * self.__cell_size_x,
                self.__y1 + (j) * self.__cell_size_y,
            ),
            Point(
                self.__x1 + (i + 1) * self.__cell_size_x,
                self.__y1 + (j + 1) * self.__cell_size_y,
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
        self._cells[self.__num_cols - 1][self.__num_rows - 1].bottom_wall = False
        self._draw_cell(self.__num_cols - 1, self.__num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []

            def possible_dir(col, row):
                try:
                    if (
                        self._cells[col][row].visited == False
                        and 0 <= col < self.__num_cols
                        and 0 <= row < self.__num_rows
                    ):
                        to_visit.append((col, row))
                except IndexError:
                    return

            possible_dir(i + 1, j)
            possible_dir(i - 1, j)
            possible_dir(i, j + 1)
            possible_dir(i, j - 1)

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return

            else:

                index = random.randrange(0, len(to_visit))
                coord = to_visit[index]

                if coord[0] == i + 1:
                    self._cells[coord[0]][coord[1]].left_wall = False
                    self._cells[i][j].right_wall = False
                    print(f"i+1")

                if coord[0] == i - 1:
                    self._cells[coord[0]][coord[1]].right_wall = False
                    self._cells[i][j].left_wall = False
                    print(f"i-1")

                if coord[1] == j + 1:
                    self._cells[coord[0]][coord[1]].top_wall = False
                    self._cells[i][j].bottom_wall = False
                    print(f"j+1")

                if coord[1] == j - 1:
                    self._cells[coord[0]][coord[1]].bottom_wall = False
                    self._cells[i][j].top_wall = False
                    print(f"j-1")

                self._draw_cell(i, j)

                self._break_walls_r(coord[0], coord[1])

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False
        return

    def solve_DFS(self):
        return self._solve_DFS_r(0, 0)

    def _solve_DFS_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self.__num_cols - 1 and j == self.__num_rows - 1:
            return True

        possible_dir_list = []

        def possible_dir(col, row, wall):
            try:
                if (
                    self._cells[col][row].visited == False
                    and 0 <= col < self.__num_cols
                    and 0 <= row < self.__num_rows
                ):
                    possible_dir_list.append((col, row, wall))
            except IndexError:
                return

        possible_dir(i + 1, j, self._cells[i][j].right_wall)
        possible_dir(i - 1, j, self._cells[i][j].left_wall)
        possible_dir(i, j + 1, self._cells[i][j].bottom_wall)
        possible_dir(i, j - 1, self._cells[i][j].top_wall)

        for tuple in possible_dir_list:
            wall = tuple[2]
            next_i = tuple[0]
            next_j = tuple[1]
            if wall == False and next_i < self.__num_cols and next_j < self.__num_rows:
                if not self._cells[next_i][next_j].visited:
                    self._cells[next_i][next_j].draw_move(self._cells[i][j])

                    if self._solve_DFS_r(next_i, next_j):
                        return True
                    else:
                        self._cells[next_i][next_j].draw_move(
                            self._cells[i][j], undo=True
                        )
        return False
