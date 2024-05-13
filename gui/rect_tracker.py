import tkinter as tk

class RectTracker:
    
    def __init__(self):
        self.canvas = None
        self.rect_coordinates = None
        self.coor = None

    def draw(self, start, end, **opts):
        """Draw the rectangle"""
        return self.canvas.create_rectangle(*(list(start) + list(end)), **opts)

    def autodraw(self, canvas, **opts):
        """Setup automatic drawing"""
        self.canvas = canvas
        self.start = None
        self.rectopts = opts
        self.rect_coordinates = None

        self.canvas.bind("<Button-1>", self.__start_rect)
        self.canvas.bind("<B1-Motion>", self.__draw_rect)
        self.canvas.bind("<ButtonRelease-1>", self.__stop_rect)

    def __start_rect(self, event):
        if self.rect_coordinates:
            self.canvas.delete(self.rect_coordinates)  # Delete previously drawn rectangle
        self.start = (event.x, event.y)

    def __draw_rect(self, event):
        if self.start:
            if self.rect_coordinates:
                self.canvas.delete(self.rect_coordinates)  # Delete previously drawn rectangle
            self.rect_coordinates = self.draw(self.start, (event.x, event.y),tag = "box", **self.rectopts)

    def __stop_rect(self, event):
        self.coor = (self.start, (event.x, event.y))
        # print(self.coor)
        self.start = None