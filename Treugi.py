from graph import *

def treug(x, y, c):
    brushColor(c)
    polygon([(x, y), (x, y-60), (x+100, y), (x, y)])


penColor("black")
treug(100, 100, "blue")
treug(200, 100, "green")
treug(200, 160, "red")


run()
