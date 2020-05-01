from graph import *


def main():
    windowSize(600, 500)
    paint_house(100, 100, 50, 50)
    run()


def paint_walls(x, y, width, param):
    pass


def paint_roof(x, y, width, param):
    pass


def paint_window(param, param1, w_width, w_height):
    pass


def paint_house(x, y, width, heigth):
    """Рисует домик
    (x, y) - левая точка крыши
    """
    paint_walls(x, y, width, heigth // 2)
    paint_roof(x, y, width, heigth // 2)

    w_height = heigth // 6
    w_width = width // 3
    paint_window(x + w_width, y + w_height, w_width, w_height)


main()
