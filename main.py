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

    currentColor = "black"
    currentTool = "line"

    startPoint = None

    while True:

        try:
            clickPoint = win.getMouse()
        except:
            print("Window is closed now, can't really fetch mouse clicks anymore...")
            exit()

        if lineBtn.getP1().getX() <= clickPoint.getX() <= lineBtn.getP2().getX() and \
                lineBtn.getP1().getY() <= clickPoint.getY() <= lineBtn.getP2().getY():
            currentTool = "line"
            rectText.setText("Rectangle")
            circleText.setText("Circle")
            triangleText.setText("Triangle")
            eraseText.setText("Erase")
            lineText.setText("Line (S)")
            continue

        if rectBtn.getP1().getX() <= clickPoint.getX() <= rectBtn.getP2().getX() and \
                rectBtn.getP1().getY() <= clickPoint.getY() <= rectBtn.getP2().getY():
            current_tool = "rectangle"
            rectText.setText("Rect (S)")
            circleText.setText("Circle")
            triangleText.setText("Triangle")
            eraseText.setText("Erase")
            lineText.setText("Line")
            continue

        if circleBtn.getP1().getX() <= clickPoint.getX() <= circleBtn.getP2().getX() and \
                circleBtn.getP1().getY() <= clickPoint.getY() <= circleBtn.getP2().getY():
            current_tool = "circle"
            rectText.setText("Rectangle")
            circleText.setText("Circle (S)")
            triangleText.setText("Triangle")
            eraseText.setText("Erase")
            lineText.setText("Line")
            continue

        if triangleBtn.getP1().getX() <= clickPoint.getX() <= triangleBtn.getP2().getX() and \
                triangleBtn.getP1().getY() <= clickPoint.getY() <= triangleBtn.getP2().getY():
            current_tool = "triangle"
            rectText.setText("Rectangle")
            circleText.setText("Circle")
            triangleText.setText("Triangle (S)")
            eraseText.setText("Erase")
            lineText.setText("Line")
            continue

        if eraseBtn.getP1().getX() <= clickPoint.getX() <= eraseBtn.getP2().getX() and \
                eraseBtn.getP1().getY() <= clickPoint.getY() <= eraseBtn.getP2().getY():
            current_tool = "erase"
            rectText.setText("Rectangle")
            circleText.setText("Circle")
            triangleText.setText("Triangle")
            lineText.setText("Line")
            eraseText.setText("Erase (S)")
            continue


main()
