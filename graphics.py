from tkinter import Tk, BOTH, Canvas


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point_1, point_2):
        self.__point_1 = point_1
        self.__point_2 = point_2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.__point_1.x,
            self.__point_1.y,
            self.__point_2.x,
            self.__point_2.y,
            fill=fill_color,
            width=2,
        )


class Cell:
    def __init__(self, window):
        self.left_wall, self.right_wall, self.bottom_wall, self.top_wall = (
            True,
            True,
            True,
            True,
        )

        self.__top_left = None
        self.__bottom_right = None
        self._win = window

    def draw(self, top_left, bottom_right):
        self.__top_left = top_left
        self.__bottom_right = bottom_right

        def Draw_Wall(wall, x1, y1, x2, y2):
            if wall:
                line = Line(Point(x1, y1), Point(x2, y2))
                self._win.draw_line(line)
            return

        Draw_Wall(
            self.left_wall,
            self.__top_left.x,
            self.__top_left.y,
            self.__top_left.x,
            self.__bottom_right.y,
        )
        Draw_Wall(
            self.right_wall,
            self.__bottom_right.x,
            self.__bottom_right.y,
            self.__bottom_right.x,
            self.__top_left.y,
        )
        Draw_Wall(
            self.bottom_wall,
            self.__top_left.x,
            self.__bottom_right.y,
            self.__bottom_right.x,
            self.__bottom_right.y,
        )
        Draw_Wall(
            self.top_wall,
            self.__top_left.x,
            self.__top_left.y,
            self.__bottom_right.x,
            self.__top_left.y,
        )

    def draw_move(self, to_cell, undo=False):
        initial = Point(
            (self.__top_left.x + self.__bottom_right.x) / 2,
            (self.__top_left.y + self.__bottom_right.y) / 2,
        )

        final = Point(
            (to_cell.__top_left.x + to_cell.__bottom_right.x) / 2,
            (to_cell.__top_left.y + to_cell.__bottom_right.y) / 2,
        )
        line = Line(initial, final)

        self._win.draw_line(line, "red" if not undo else "gray")
