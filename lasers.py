from tkinter import *
from tkinter import ttk
import numpy as np
import random

N = 8       # no. of shortlines
n = 0       # indexes colors
colors = ['orangered', 'chartreuse', 'deepskyblue', '#e7accf', '#cbc9c0', '#525746', '#008381', '#67592a', '#0f4645', '#ac9884','#d4dcd6', '#619ad6', '#84623e', '#e0dee3']
size = 50

root = Tk()
geo_x = root.winfo_screenwidth()
geo_y = root.winfo_screenheight()
root.geometry('%dx%d+%d+%d' % (1000, 1000, geo_x//2 - 400, geo_y//2 - 400))

mid_x, mid_y = geo_x / 2, geo_y /2

ca = 50
xa = np.round(ca + mid_x - np.geomspace(50, mid_x, size//2), 0)
xb = np.round(-ca + mid_x + np.geomspace(50, mid_x, size//2), 0)
x = np.concatenate((xa, xb))
x = np.sort(x)

ya = np.round(ca + mid_y - np.geomspace(50, mid_y, size//2), 0)
yb = np.round(-ca + mid_y + np.geomspace(50, mid_y, size//2), 0)
y = np.concatenate((ya, yb))
y = np.sort(y)

# logspace grid
x_min, x_max = min(x), max(x)
y_min, y_max = min(y), max(y)
lines = []
for p in x:
    line = (p, y_min, p, y_max)
    lines.append(line)
for q in y:
    line = (x_min, q, x_max, q)
    lines.append(line)

class Short:
    def __init__(self):
        self.i, self.j = np.random.choice(x.size), np.random.choice(y.size)
        self.color = colors[n]

    def select_next(self):
        x1, y1 = x[self.i], y[self.j]
        delta, epsilon = np.random.choice([-1, 1]), np.random.choice([-1, 1])
        self.i, self.j = self.i + delta, self.j + epsilon
        self.i, self.j = self.i % size, self.j % size
        x2, y2 = x[self.i], y[self.j]
        self.pts = (x1, y1, x2, y2)
        return self.pts

class TheCanvas(Canvas):
    def __init__(self, master):

        super().__init__(root, width=geo_x, height=geo_y, bg="black",
         bd=0, highlightthickness=0, relief="ridge")
        self.pack(fill='both', expand=True)

        self.lns = []
        for line in lines:
            self.lns.append(self.create_line(line, fill= 'grey', width=1))

        self.shorts = []
        self.sh = []
        for _ in range(N):
            global n
            short = Short()
            self.shorts.append(short)
            self.pts = short.select_next()
            self.sh.append(self.create_line(self.pts, fill=short.color, width=3))
            n += 1
        self.after(2000, self.run)

    def run(self):
        for s, short in zip(self.sh, self.shorts):
            self.pts = short.select_next()
            self.coords(s, self.pts)
        self.after(100, self.run)


if __name__ == '__main__':
    c = TheCanvas(root)
    root.mainloop()
