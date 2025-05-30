from tkinter import Tk, BOTH, Canvas

from graphics import Point, Line


class Window:

    def __init__(self, width, height, title="main"):
        self.__root = Tk()
        self.__root.title(title)
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running == True:
            self.redraw()
        print("window closed")

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self._Window__canvas, fill_color)
