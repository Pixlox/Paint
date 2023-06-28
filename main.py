from graphics import *

def drawLine(win, start, end, colour):
    line = Line(start, end)
    line.setFill(colour)
    line.setWidth(7)
    line.draw(win)

def drawRectangle(win, start, end, colour):
    rectangle = Rectangle(start, end)
    rectangle.setFill(colour)
    rectangle.draw(win)

def drawCircle(win, center, radius, colour):
    circle = Circle(center, radius)
    circle.setFill(colour)
    circle.draw(win)

def drawTriangle(win, p1, p2, p3, colour):
    triangle = Polygon(p1, p2, p3)
    triangle.setFill(colour)
    triangle.draw(win)

def circleOverlapMenu(circle, menuBarRectangle):
    center = circle.getCenter()
    radius = circle.getRadius()

    x1 = center.getX() - radius
    y1 = center.getY() - radius
    x2 = center.getX() + radius
    y2 = center.getY() + radius

    # Check if any part of the circle is inside the menu bar
    if x1 <= menuBarRectangle.getP2().getX() and \
            x2 >= menuBarRectangle.getP1().getX() and \
            y1 <= menuBarRectangle.getP2().getY() and \
            y2 >= menuBarRectangle.getP1().getY():
        return True
    else:
        return False



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

    currentColour = "black"
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
            currentTool = "rectangle"
            rectText.setText("Rect (S)")
            circleText.setText("Circle")
            triangleText.setText("Triangle")
            eraseText.setText("Erase")
            lineText.setText("Line")
            continue

        if circleBtn.getP1().getX() <= clickPoint.getX() <= circleBtn.getP2().getX() and \
                circleBtn.getP1().getY() <= clickPoint.getY() <= circleBtn.getP2().getY():
            currentTool = "circle"
            rectText.setText("Rectangle")
            circleText.setText("Circle (S)")
            triangleText.setText("Triangle")
            eraseText.setText("Erase")
            lineText.setText("Line")
            continue

        if triangleBtn.getP1().getX() <= clickPoint.getX() <= triangleBtn.getP2().getX() and \
                triangleBtn.getP1().getY() <= clickPoint.getY() <= triangleBtn.getP2().getY():
            currentTool = "triangle"
            rectText.setText("Rectangle")
            circleText.setText("Circle")
            triangleText.setText("Triangle (S)")
            eraseText.setText("Erase")
            lineText.setText("Line")
            continue

        if eraseBtn.getP1().getX() <= clickPoint.getX() <= eraseBtn.getP2().getX() and \
                eraseBtn.getP1().getY() <= clickPoint.getY() <= eraseBtn.getP2().getY():
            currentTool = "erase"
            rectText.setText("Rectangle")
            circleText.setText("Circle")
            triangleText.setText("Triangle")
            lineText.setText("Line")
            eraseText.setText("Erase (S)")
            continue

        if redBtn.getP1().getX() <= clickPoint.getX() <= redBtn.getP2().getX() and \
                redBtn.getP1().getY() <= clickPoint.getY() <= redBtn.getP2().getY():
            currentColour = "red"
            greenBtnText.setText("Green")
            blueBtnText.setText("Blue")
            yellowBtnText.setText("Yellow")
            orangeBtnText.setText("Orange")
            blackBtnText.setText("Black")
            redBtnText.setText("Red (S)")
            continue

        if greenBtn.getP1().getX() <= clickPoint.getX() <= greenBtn.getP2().getX() and \
                greenBtn.getP1().getY() <= clickPoint.getY() <= greenBtn.getP2().getY():
            currentColour = "green"
            greenBtnText.setText("Green (S)")
            blueBtnText.setText("Blue")
            yellowBtnText.setText("Yellow")
            orangeBtnText.setText("Orange")
            blackBtnText.setText("Black")
            redBtnText.setText("Red")
            continue

        if blueBtn.getP1().getX() <= clickPoint.getX() <= blueBtn.getP2().getX() and \
                blueBtn.getP1().getY() <= clickPoint.getY() <= blueBtn.getP2().getY():
            currentColour = "blue"
            greenBtnText.setText("Green")
            yellowBtnText.setText("Yellow")
            orangeBtnText.setText("Orange")
            blueBtnText.setText("Blue (S)")
            blackBtnText.setText("Black")
            redBtnText.setText("Red")
            continue

        if yellowBtn.getP1().getX() <= clickPoint.getX() <= yellowBtn.getP2().getX() and \
                yellowBtn.getP1().getY() <= clickPoint.getY() <= yellowBtn.getP2().getY():
            currentColour = "yellow"
            greenBtnText.setText("Green")
            blueBtnText.setText("Blue")
            orangeBtnText.setText("Orange")
            yellowBtnText.setText("Yellow (S)")
            blackBtnText.setText("Black")
            redBtnText.setText("Red")
            continue

        if orangeBtn.getP1().getX() <= clickPoint.getX() <= orangeBtn.getP2().getX() and \
                orangeBtn.getP1().getY() <= clickPoint.getY() <= orangeBtn.getP2().getY():
            currentColour = "orange"
            greenBtnText.setText("Green")
            blueBtnText.setText("Blue")
            yellowBtnText.setText("Yellow")
            orangeBtnText.setText("Orange (S)")
            blackBtnText.setText("Black")
            redBtnText.setText("Red")
            continue

        if blackBtn.getP1().getX() <= clickPoint.getX() <= blackBtn.getP2().getX() and \
                blackBtn.getP1().getY() <= clickPoint.getY() <= blackBtn.getP2().getY():
            currentColour = "black"
            greenBtnText.setText("Green")
            greenBtnText.setText("Blue")
            yellowBtnText.setText("Yellow")
            orangeBtnText.setText("Orange")
            blackBtnText.setText("Black (S)")
            redBtnText.setText("Red")
            continue

        if currentTool is None:
            continue

        if currentTool == "line":
            if 0 <= clickPoint.getX() <= 78 and 0 <= clickPoint.getY() <= winHeight:
                continue
            if startPoint is None:
                startPoint = clickPoint
            else:
                drawLine(win, startPoint, clickPoint, currentColour)
                startPoint = None

        elif currentTool == "rectangle":
            if 0 <= clickPoint.getX() <= 78 and 0 <= clickPoint.getY() <= winHeight:
                continue
            if startPoint is None:
                startPoint = clickPoint
            else:
                drawRectangle(win, startPoint, clickPoint, currentColour)
                startPoint = None

        elif currentTool == "circle":
            if 0 <= clickPoint.getX() <= 78 and 0 <= clickPoint.getY() <= winHeight:
                continue
            if startPoint is None:
                startPoint = clickPoint
            else:
                radius = abs(startPoint.getX() - clickPoint.getX())
                circle = Circle(startPoint, radius)
                if circleOverlapMenu(circle, menuBarRectangle):
                    circleText_big = Text(Point(400, 50), "Circle too big!")
                    circleText_big.draw(win)
                    circleText_big.setSize(20)
                    circleText_big.setStyle("bold")
                    time.sleep(0.25)  # Make the thread sleep for 0.25s. This has some drawbacks, but will do for now.
                    circleText_big.setFill("red") # Wake back up to swap colour, in case covered.
                    time.sleep(0.25) # Let thread sleep again, then
                    circleText_big.undraw() # Undraw the text.
                    print("circle too big")
                else:
                    drawCircle(win, startPoint, radius, currentColour)

                startPoint = None

        elif currentTool == "triangle":
            if 0 <= clickPoint.getX() <= 78 and 0 <= clickPoint.getY() <= winHeight:
                continue
            if startPoint is None:
                startPoint = clickPoint
            elif startPoint is not None:
                secondPoint = clickPoint
                drawTriangle(win, startPoint, Point(startPoint.getX(), secondPoint.getY()), secondPoint, currentColour)
                startPoint = None

        elif currentTool == "erase":
            if 0 <= clickPoint.getX() <= 78 and 0 <= clickPoint.getY() <= winHeight:
                continue

            items = win.find_overlapping(clickPoint.getX(), clickPoint.getY(), clickPoint.getX(), clickPoint.getY())

            for item in items:
                win.delete(item)


# Calls main function
main()

