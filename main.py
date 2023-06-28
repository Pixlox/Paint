from graphics import *

def draw_line(win, start, end, colour):
    line = Line(start, end)
    line.setFill(colour)
    line.setWidth(7)
    line.draw(win)

def draw_rectangle(win, start, end, colour):
    rectangle = Rectangle(start, end)
    rectangle.setFill(colour)
    rectangle.draw(win)

def draw_circle(win, center, radius, colour):
    circle = Circle(center, radius)
    circle.setFill(colour)
    circle.draw(win)

def draw_triangle(win, p1, p2, p3, colour):
    triangle = Polygon(p1, p2, p3)
    triangle.setFill(colour)
    triangle.draw(win)


def main():
    winWidth = 800
    winHeight = 600

    win = GraphWin("PxPaint", winWidth, winHeight)


    menuBarRectangle = Rectangle(Point(0, 0), Point(78, winHeight))
    menuBarRectangle.setFill("lightgrey")
    menuBarRectangle.draw(win)

    win.setBackground("white")

    win.getMouse()
    win.close()

main()
