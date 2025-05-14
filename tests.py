import unittest

from tkinter import Tk, BOTH, Canvas

from maze import Maze
from graphics import Line, Point, Cell
from window import Window

"""
class Test_Cell_Walls(unittest.TestCase):
    def test_cell_create_wall_no_left(self):
        win = Window(800, 600, "no_left")

        top_left = Point(20, 20)
        bottom_right = Point(400, 400)

        cell_no_left = Cell(win)
        cell_no_left.left_wall = False
        cell_no_left.draw(top_left, bottom_right)

        win.wait_for_close()

    def test_cell_create_wall_no_right(self):
        win = Window(800, 600, "no_right")

        top_left = Point(20, 20)
        bottom_right = Point(400, 400)

        cell_no_right = Cell(win)
        cell_no_right.right_wall = False
        cell_no_right.draw(top_left, bottom_right)

        win.wait_for_close()

    def test_cell_create_wall_no_top(self):
        win = Window(800, 600, "no_top")

        top_left = Point(20, 20)
        bottom_right = Point(400, 400)

        cell_no_right = Cell(win)
        cell_no_right.top_wall = False
        cell_no_right.draw(top_left, bottom_right)

        win.wait_for_close()

    def test_cell_create_wall_no_bottom(self):
        win = Window(800, 600, "no_bottom")

        top_left = Point(20, 20)
        bottom_right = Point(400, 400)

        cell_no_right = Cell(win)
        cell_no_right.bottom_wall = False
        cell_no_right.draw(top_left, bottom_right)

        win.wait_for_close()
"""


class Test_Maze(unittest.TestCase):
    """

    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        win = Window(800, 600)
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_appearance(self):
        win = Window(800, 600)

        maze = Maze(3, 4, 10, 10, 100, 100, win)
        win.wait_for_close()

    def test_maze_visited_reset(self):
        win = Window(800, 600)

        maze = Maze(3, 4, 10, 10, 100, 100, win)

        cell_list = maze._cells
        for col in cell_list:
            for cell in col:
                if cell.visited:
                    self.assertFalse("Cell List contain visited Fals")
        self.assertTrue("yayaya")

        win.wait_for_close()
    """

    def test_solve_maze_DFS(self):
        win = Window(800, 600)

        maze = Maze(3, 4, 20, 20, 40, 40, win)
        print(maze.solve_DFS())
        win.wait_for_close()


if __name__ == "__main__":
    unittest.main()
