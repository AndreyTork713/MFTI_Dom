from graph import *


def row(y):
    x = 40
    for i in range(5):
        circle(x, y, 40)
        x += 60


y = 40
for k in range(5):
    y += 40
    row(y)

run()
