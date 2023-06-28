from graphics import *

# Custom function to draw a line
def drawLine(win, start, end, colour):
    line = Line(start, end)
    line.setFill(colour)
    line.setWidth(7)
    line.draw(win)

# Custom function to draw a rectangle
def drawRectangle(win, start, end, colour):
    rectangle = Rectangle(start, end)
    rectangle.setFill(colour)
    rectangle.draw(win)

# Custom function to draw a circle
def drawCircle(win, center, radius, colour):
    circle = Circle(center, radius)
    circle.setFill(colour)
    circle.draw(win)

# Custom function to draw a triangle
def drawTriangle(win, p1, p2, p3, colour):
    triangle = Polygon(p1, p2, p3)
    triangle.setFill(colour)
    triangle.draw(win)

# Function to check circle and menu bar overlap
def circleOverlapMenu(circle, menuBarRectangle):
    center = circle.getCenter()
    radius = circle.getRadius()

    x1 = center.getX() - radius
    y1 = center.getY() - radius
    x2 = center.getX() + radius
    y2 = center.getY() + radius

    # Check if any part of the circle is inside the menu bar
    if x1 <= menuBarRectangle.getP2().getX() and x2 >= menuBarRectangle.getP1().getX() and y1 <= menuBarRectangle.getP2().getY() and y2 >= menuBarRectangle.getP1().getY():
        return True
    else:
        return False



def main():
    winWidth = 800
    winHeight = 600

    # Create the window with the size of 800x600
    win = GraphWin("PxPaint", winWidth, winHeight)

    # Create the menu bar, below the button 'layer'
    menuBarRectangle = Rectangle(Point(0, 0), Point(78, winHeight))
    menuBarRectangle.setFill("lightgrey")
    menuBarRectangle.draw(win)

    # Set the background to white (canvas)
    win.setBackground("white")

    # TOOLS
    # Create the line button with an (S) marker for default tool
    lineBtn = Rectangle(Point(10, 10), Point(70, 40))
    lineBtn.setFill("lightgrey")  # Set the colour to light grey to contrast
    lineBtn.draw(win)
    lineText = Text(lineBtn.getCenter(), "Line (S)")
    lineText.draw(win)

    # Create selectable rectangle button
    rectBtn = Rectangle(Point(10, 60), Point(70, 90))
    rectBtn.setFill("lightgrey")
    rectBtn.draw(win)
    rectText = Text(rectBtn.getCenter(), "Rectangle")
    rectText.draw(win)

    # Create selectable circle button
    circleBtn = Rectangle(Point(10, 110), Point(70, 140))
    circleBtn.setFill("lightgrey")
    circleBtn.draw(win)
    circleText = Text(circleBtn.getCenter(), "Circle")
    circleText.draw(win)

    # Create selectable triangle button
    triangleBtn = Rectangle(Point(10, 160), Point(70, 190))
    triangleBtn.setFill("lightgrey")
    triangleBtn.draw(win)
    triangleText = Text(triangleBtn.getCenter(), "Triangle")
    triangleText.draw(win)

    # Create the selectable erase button
    eraseBtn = Rectangle(Point(10, 210), Point(70, 240))
    eraseBtn.setFill("lightgrey")
    eraseBtn.draw(win)
    eraseText = Text(eraseBtn.getCenter(), "Erase")
    eraseText.draw(win)


    # COLOURS
    # Selectable red colour button
    redBtn = Rectangle(Point(10, 270), Point(70, 320))
    redBtn.setFill("red")  # Button colour corresponds with the selected colour
    redBtn.draw(win)
    redBtnText = Text(redBtn.getCenter(), "Red")
    redBtnText.draw(win)

    # Selectable green colour button
    greenBtn = Rectangle(Point(10, 320), Point(70, 370))
    greenBtn.setFill("green")
    greenBtn.draw(win)
    greenBtnText = Text(greenBtn.getCenter(), "Green")
    greenBtnText.draw(win)

    # Selectable blue colour button
    blueBtn = Rectangle(Point(10, 370), Point(70, 420))
    blueBtn.setFill("blue")
    blueBtn.draw(win)
    blueBtnText = Text(blueBtn.getCenter(), "Blue")
    blueBtnText.draw(win)

    # Selectable yellow colour button
    yellowBtn = Rectangle(Point(10, 420), Point(70, 470))
    yellowBtn.setFill("yellow")
    yellowBtn.draw(win)
    yellowBtnText = Text(yellowBtn.getCenter(), "Yellow")
    yellowBtnText.draw(win)

    # Selectable orange colour button
    orangeBtn = Rectangle(Point(10, 470), Point(70, 520))
    orangeBtn.setFill("orange")
    orangeBtn.draw(win)
    orangeBtnText = Text(orangeBtn.getCenter(), "Orange")
    orangeBtnText.draw(win)

    # Selectable black colour button
    blackBtn = Rectangle(Point(10, 520), Point(70, 570))
    blackBtn.setFill("black")
    blackBtn.draw(win)
    blackBtnText = Text(blackBtn.getCenter(), "Black (S)")
    blackBtnText.setTextColor("white")
    blackBtnText.draw(win)

    # Set the default startup tools (black / line)
    currentColour = "black"
    currentTool = "line"

    startPoint = None

    while True:

        try:
            clickPoint = win.getMouse()
        except:
            # When the user closes the window, graphics.py likes to throw an error. This sends a msg to console
            # explaining and closes the program.
            print("Window is closed now, can't really fetch mouse clicks anymore...")
            exit()

        # Check if the user clicked on the button by checking if the click point is within the buttons coords
        if lineBtn.getP1().getX() <= clickPoint.getX() <= lineBtn.getP2().getX() and \
                lineBtn.getP1().getY() <= clickPoint.getY() <= lineBtn.getP2().getY():
            # Current tool is now line
            currentTool = "line"
            # Change every tool text to default, except for line tool, which get a (S) marker
            rectText.setText("Rectangle")
            circleText.setText("Circle")
            triangleText.setText("Triangle")
            eraseText.setText("Erase")
            lineText.setText("Line (S)")
            continue

        # Check if the user clicked on the button by checking if the click point is within the buttons coords
        if rectBtn.getP1().getX() <= clickPoint.getX() <= rectBtn.getP2().getX() and \
                rectBtn.getP1().getY() <= clickPoint.getY() <= rectBtn.getP2().getY():
            # Current tool is now rectangle
            currentTool = "rectangle"
            # Change every tool text to default, except for rectangle tool, which get a (S) marker
            rectText.setText("Rect (S)")
            circleText.setText("Circle")
            triangleText.setText("Triangle")
            eraseText.setText("Erase")
            lineText.setText("Line")
            continue

        # Check if the user clicked on the button by checking if the click point is within the buttons coords
        if circleBtn.getP1().getX() <= clickPoint.getX() <= circleBtn.getP2().getX() and \
                circleBtn.getP1().getY() <= clickPoint.getY() <= circleBtn.getP2().getY():
            # Current tool is now circle
            currentTool = "circle"
            # Change every tool text to default, except for circle tool, which get a (S) marker
            rectText.setText("Rectangle")
            circleText.setText("Circle (S)")
            triangleText.setText("Triangle")
            eraseText.setText("Erase")
            lineText.setText("Line")
            continue

        # Check if the user clicked on the button by checking if the click point is within the buttons coords
        if triangleBtn.getP1().getX() <= clickPoint.getX() <= triangleBtn.getP2().getX() and \
                triangleBtn.getP1().getY() <= clickPoint.getY() <= triangleBtn.getP2().getY():
            # Current tool is now triangle
            currentTool = "triangle"
            # Change every tool text to default, except for triangle tool, which get a (S) marker
            rectText.setText("Rectangle")
            circleText.setText("Circle")
            triangleText.setText("Triangle (S)")
            eraseText.setText("Erase")
            lineText.setText("Line")
            continue

        # Check if the user clicked on the button by checking if the click point is within the buttons coords
        if eraseBtn.getP1().getX() <= clickPoint.getX() <= eraseBtn.getP2().getX() and \
                eraseBtn.getP1().getY() <= clickPoint.getY() <= eraseBtn.getP2().getY():
            # Current tool is now erase
            currentTool = "erase"
            # Change every tool text to default, except for erase tool, which get a (S) marker
            rectText.setText("Rectangle")
            circleText.setText("Circle")
            triangleText.setText("Triangle")
            lineText.setText("Line")
            eraseText.setText("Erase (S)")
            continue

        # Check if the user clicked on the button by checking if the click point is within the buttons coords
        if redBtn.getP1().getX() <= clickPoint.getX() <= redBtn.getP2().getX() and \
                redBtn.getP1().getY() <= clickPoint.getY() <= redBtn.getP2().getY():
            # Current colour is now red
            currentColour = "red"
            # Change every colour text to default, except for red colour, which get a (S) marker
            greenBtnText.setText("Green")
            blueBtnText.setText("Blue")
            yellowBtnText.setText("Yellow")
            orangeBtnText.setText("Orange")
            blackBtnText.setText("Black")
            redBtnText.setText("Red (S)")
            continue

        # Check if the user clicked on the button by checking if the click point is within the buttons coords
        if greenBtn.getP1().getX() <= clickPoint.getX() <= greenBtn.getP2().getX() and \
                greenBtn.getP1().getY() <= clickPoint.getY() <= greenBtn.getP2().getY():
            # Current colour is now green
            currentColour = "green"
            # Change every colour text to default, except for green colour, which get a (S) marker
            greenBtnText.setText("Green (S)")
            blueBtnText.setText("Blue")
            yellowBtnText.setText("Yellow")
            orangeBtnText.setText("Orange")
            blackBtnText.setText("Black")
            redBtnText.setText("Red")
            continue

        # Check if the user clicked on the button by checking if the click point is within the buttons coords
        if blueBtn.getP1().getX() <= clickPoint.getX() <= blueBtn.getP2().getX() and \
                blueBtn.getP1().getY() <= clickPoint.getY() <= blueBtn.getP2().getY():
            # Current colour is now blue
            currentColour = "blue"
            # Change every colour text to default, except for blue colour, which get a (S) marker
            greenBtnText.setText("Green")
            yellowBtnText.setText("Yellow")
            orangeBtnText.setText("Orange")
            blueBtnText.setText("Blue (S)")
            blackBtnText.setText("Black")
            redBtnText.setText("Red")
            continue

        # Check if the user clicked on the button by checking if the click point is within the buttons coords
        if yellowBtn.getP1().getX() <= clickPoint.getX() <= yellowBtn.getP2().getX() and yellowBtn.getP1().getY() <= clickPoint.getY() <= yellowBtn.getP2().getY():
            # Current colour is now yellow
            currentColour = "yellow"
            # Change every colour text to default, except for yellow colour, which get a (S) marker
            greenBtnText.setText("Green")
            blueBtnText.setText("Blue")
            orangeBtnText.setText("Orange")
            yellowBtnText.setText("Yellow (S)")
            blackBtnText.setText("Black")
            redBtnText.setText("Red")
            continue

        # Check if the user clicked on the button by checking if the click point is within the buttons coords
        if orangeBtn.getP1().getX() <= clickPoint.getX() <= orangeBtn.getP2().getX() and orangeBtn.getP1().getY() <= clickPoint.getY() <= orangeBtn.getP2().getY():
            # Current colour is now orange
            currentColour = "orange"
            # Change every colour text to default, except for orange colour, which get a (S) marker
            greenBtnText.setText("Green")
            blueBtnText.setText("Blue")
            yellowBtnText.setText("Yellow")
            orangeBtnText.setText("Orange (S)")
            blackBtnText.setText("Black")
            redBtnText.setText("Red")
            continue

        # Check if the user clicked on the button by checking if the click point is within the buttons coords
        if blackBtn.getP1().getX() <= clickPoint.getX() <= blackBtn.getP2().getX() and blackBtn.getP1().getY() <= clickPoint.getY() <= blackBtn.getP2().getY():
            # Current colour is now black
            currentColour = "black"
            # Change every colour text to default, except for black colour, which get a (S) marker
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
            # Checks if the X coordinate of a mouse click is between 0 and 78
            # and if the Y coordinate is between 0 and the window height, to determine if the click occurred
            # within the menu bar area. if it is there, the click is ignored.
            if 0 <= clickPoint.getX() <= 78 and 0 <= clickPoint.getY() <= winHeight:
                continue
            if startPoint is None:
                # Set the start point for drawing the line
                startPoint = clickPoint
            else:
                # Call draw line function, with startPoint and the 'second' start point (clickPoint)
                drawLine(win, startPoint, clickPoint, currentColour)
                startPoint = None

        elif currentTool == "rectangle":
            # Call menubar click check function
            if 0 <= clickPoint.getX() <= 78 and 0 <= clickPoint.getY() <= winHeight:
                continue
            if startPoint is None:
                # Set the start point for drawing the line
                startPoint = clickPoint
            else:
                # Call draw line function, with startPoint and the 'second' start point (clickPoint)
                drawRectangle(win, startPoint, clickPoint, currentColour)
                startPoint = None

        elif currentTool == "circle":
            # Call menubar click check function
            if 0 <= clickPoint.getX() <= 78 and 0 <= clickPoint.getY() <= winHeight:
                continue
            if startPoint is None:
                # Set the start point for drawing the line
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
            # Call menubar click check function
            if 0 <= clickPoint.getX() <= 78 and 0 <= clickPoint.getY() <= winHeight:
                continue
            if startPoint is None:
                # Set the start point for drawing the line
                startPoint = clickPoint
            elif startPoint is not None:
                # Get the SECOND point for drawing it
                secondPoint = clickPoint
                # Draw using the start point, a vertical aligned point, and the second point
                drawTriangle(win, startPoint, Point(startPoint.getX(), secondPoint.getY()), secondPoint, currentColour)
                startPoint = None

        elif currentTool == "erase":
            # Call menubar click check function
            if 0 <= clickPoint.getX() <= 78 and 0 <= clickPoint.getY() <= winHeight:
                continue

            # Find all items that overlap the click point
            items = win.find_overlapping(clickPoint.getX(), clickPoint.getY(), clickPoint.getX(), clickPoint.getY())

            # for each of those items, delete them.
            for item in items:
                win.delete(item)


# Calls main function
main()

