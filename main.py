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

    lineBtn = Rectangle(Point(10, 10), Point(70, 40))
    lineBtn.setFill("lightgrey")
    lineBtn.draw(win)
    lineText = Text(lineBtn.getCenter(), "Line (S)")
    lineText.draw(win)

    rectBtn = Rectangle(Point(10, 60), Point(70, 90))
    rectBtn.setFill("lightgrey")
    rectBtn.draw(win)
    rectText = Text(rectBtn.getCenter(), "Rectangle")
    rectText.draw(win)

    circleBtn = Rectangle(Point(10, 110), Point(70, 140))
    circleBtn.setFill("lightgrey")
    circleBtn.draw(win)
    circleText = Text(circleBtn.getCenter(), "Circle")
    circleText.draw(win)

    triangleBtn = Rectangle(Point(10, 160), Point(70, 190))
    triangleBtn.setFill("lightgrey")
    triangleBtn.draw(win)
    triangleText = Text(triangleBtn.getCenter(), "Triangle")
    triangleText.draw(win)

    eraseBtn = Rectangle(Point(10, 210), Point(70, 240))
    eraseBtn.setFill("lightgrey")
    eraseBtn.draw(win)
    eraseText = Text(eraseBtn.getCenter(), "Erase")
    eraseText.draw(win)

    redBtn = Rectangle(Point(10, 270), Point(70, 320))
    redBtn.setFill("red")
    redBtn.draw(win)
    redBtnText = Text(redBtn.getCenter(), "Red")
    redBtnText.draw(win)

    greenBtn = Rectangle(Point(10, 320), Point(70, 370))
    greenBtn.setFill("green")
    greenBtn.draw(win)
    greenBtnText = Text(greenBtn.getCenter(), "Green")
    greenBtnText.draw(win)

    blueBtn = Rectangle(Point(10, 370), Point(70, 420))
    blueBtn.setFill("blue")
    blueBtn.draw(win)
    blueBtnText = Text(blueBtn.getCenter(), "Blue")
    blueBtnText.draw(win)

    yellowBtn = Rectangle(Point(10, 420), Point(70, 470))
    yellowBtn.setFill("yellow")
    yellowBtn.draw(win)
    yellowBtnText = Text(yellowBtn.getCenter(), "Yellow")
    yellowBtnText.draw(win)

    orangeBtn = Rectangle(Point(10, 470), Point(70, 520))
    orangeBtn.setFill("orange")
    orangeBtn.draw(win)
    orangeBtnText = Text(orangeBtn.getCenter(), "Orange")
    orangeBtnText.draw(win)

    blackBtn = Rectangle(Point(10, 520), Point(70, 570))
    blackBtn.setFill("black")
    blackBtn.draw(win)
    blackBtnText = Text(blackBtn.getCenter(), "Black (S)")
    blackBtnText.setTextColor("white")
    blackBtnText.draw(win)

    win.getMouse()
    win.close()

main()
