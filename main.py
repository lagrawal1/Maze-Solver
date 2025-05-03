from tkinter import Tk, BOTH, Canvas
from window import Window
from graphics import Line, Point, Cell


def main():
    win = Window(800, 600)
    point_1 = Point(10, 20)
    point_2 = Point(100, 200)
    point_3 = Point(300, 54)

    cell_p1 = Point(10, 10)
    cell_p2 = Point(100, 100)

    cell_p3 = Point(300, 300)
    cell_p4 = Point(500, 500)

    line = Line(point_1, point_2)
    line_2 = Line(point_2, point_3)
    line_3 = Line(point_3, point_1)

    cell1 = Cell(win)
    cell2 = Cell(win)

    cell1.draw(cell_p1, cell_p2)
    cell2.draw(cell_p3, cell_p4)

    cell1.draw_move(cell2, True)

    win.draw_line(line, "red")
    win.draw_line(line_2, "blue")
    win.draw_line(line_3, "black")

    win.wait_for_close()


if __name__ == "__main__":
    main()
