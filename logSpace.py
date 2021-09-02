from tkinter import Tk, mainloop, Canvas
from tkinter import ttk
import numpy as np
import random


root = Tk()
geo_x = root.winfo_screenwidth()
geo_y = root.winfo_screenheight()
root.geometry('%dx%d+%d+%d' % (1000, 1000, geo_x//2 - 400, geo_y//2 - 400))

mid = geo_x / 2
ca = 15  # center adjust

X1a = np.round(ca + mid - 10 * np.logspace(0.3, 2.4, 51), 0)
X1b = np.round(-ca + mid + 10 * np.logspace(0.3, 2.4, 50), 0)
X1 = np.concatenate((X1a, X1b))

p = np.ones(100)
Y1, Y2, Y3, Y4, Y5, Y6 = [100, 240], [250, 390], [400, 540], [550, 690], [700, 840], [850, 990]
Y7, Y8, Y9 = [1000, 1140], [1150, 1290], [1300, 1350]

spaces = [[X1, Y1], [X1, Y2], [X1, Y3], [X1, Y4], [X1, Y5], [X1, Y6], [X1, Y7], [X1, Y8], [X1, Y9]]

greys = ['#9b8e8e', '#545b62', '#ebecf0', '#b9b4b1', '#c8c7c5', '#a1988b', '#748b97']

class Logspace:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.y1, self.y2 = p * Y[0], p * Y[1]
        self.lgsp = self.logset()

    def logset(self):
        '''  X is a logspace. Y is a list of 2 y's; a logset looks like ||| .
        logset() returns: [((x0, y0), (x1, y1)), ((x2, y2), (x3, y3))...]
        '''
        l_a = list(zip(self.X, self.y1))
        l_b = list(zip(self.X, self.y2))
        self.lgsp = [(i[0], i[1]) for i in zip(l_a, l_b)]
        return self.lgsp

    def subset(self):
        y_a = np.random.randint(self.Y[0], self.Y[1], 100)
        y_b = np.random.randint(self.Y[0], self.Y[1], 100)
        l_a = list(zip(self.X, y_a))
        l_b = list(zip(self.X, y_b))
        self.sbsp = [(i[0], i[1]) for i in zip(l_a, l_b)]
        return self.sbsp

class TheCanvas(Canvas):
    def __init__(self, master):

        super().__init__(root, width=geo_x, height=geo_y, bg="black",
         bd=0, highlightthickness=0, relief="ridge")
        self.pack(fill='both', expand=True)

        self.lgsp = []      # l of lgsp objects
        self.lgs = []       # l of lgsp object representations
        self.sbs = []
        for space in spaces:
            l = Logspace(space[0], space[1])  # s[0],s[1] = X,Y
            l.lgsp = l.logset()
            self.lgsp.append(l.lgsp)
            l.sbsp = l.subset()
            self.sbs.append(l.sbsp)
            for line in l.lgsp:
                color = random.choice(greys)
                self.lgs.append(self.create_line(line, fill= color, width=2))
            for line in l.sbsp:
                self.sbs.append(self.create_line(line, fill='deepskyblue', width=3))


if __name__ == '__main__':
    c = TheCanvas(root)
    root.mainloop()
