from graph import *

x = 40
y = 40
for i in range(5):
    for i in range(4):
        circle(x, y, 20)
        y += 20
    x += 60
run()
