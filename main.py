from tkinter import Tk, BOTH, Canvas
from window import Window
from graphics import Line, Point, Cell
from maze import Maze


def main():
    win = Window(800, 600)

    maze = Maze(3, 4, 5, 5, 100, 100, win)
    win.wait_for_close()


if __name__ == "__main__":
    main()
