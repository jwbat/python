'''
Use the spacebar to generate new patterns
'''

from tkinter import Tk, mainloop, Canvas
from collections import deque
import random

root = Tk()
geo_x = root.winfo_screenwidth()
geo_y = root.winfo_screenheight()
mid_x, mid_y = geo_x / 2, geo_y /2
root.geometry('%dx%d+%d+%d' % (300, 300, geo_x//2, geo_y//2))

c = Canvas(root, width=geo_x, height=geo_y, bg="black",
 bd=0, highlightthickness=0, relief="ridge")
c.pack(fill='both', expand=True)


def make_line():
    x, y = mid_x, mid_y
    line = [x, y]
    for _ in range(5000):
        p = random.choice([-50, 50])
        q = random.choice((-50, 50))
        x += p
        y += q
        line.append(x)
        line.append(y)

    return tuple(line)

def new(event):
    '''
    This fcn does this.
    '''
    line =  make_line()
    c.coords(i, line[:2000])
    c.coords(j, line[2000:3000])
    c.coords(k, line[3000:])

line = make_line()

i = c.create_line(line[:2000], fill="orangered", width=8)
j = c.create_line(line[2000:3000], fill="lightblue", width=8)
k = c.create_line(line[3000:], fill="yellow", width=8)


root.bind('<space>', new)
root.mainloop()
