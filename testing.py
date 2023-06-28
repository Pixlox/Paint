from graphics import *


# Custom function to draw a line
def draw_line(win, start, end, color):
    line = Line(start, end)
    line.setFill(color)
    line.setWidth(7)
    line.draw(win)


# Custom function to draw a rectangle
def draw_rectangle(win, start, end, color):
    rectangle = Rectangle(start, end)
    rectangle.setFill(color)
    rectangle.draw(win)


# Custom function to draw a circle
def draw_circle(win, center, radius, color):
    circle = Circle(center, radius)
    circle.setFill(color)
    circle.draw(win)


def circle_overlaps_menu(circle, menu_bar_rect):
    center = circle.getCenter()
    radius = circle.getRadius()

    x1 = center.getX() - radius
    y1 = center.getY() - radius
    x2 = center.getX() + radius
    y2 = center.getY() + radius

    # Check if any part of the circle is inside the menu bar
    if x1 <= menu_bar_rect.getP2().getX() and \
            x2 >= menu_bar_rect.getP1().getX() and \
            y1 <= menu_bar_rect.getP2().getY() and \
            y2 >= menu_bar_rect.getP1().getY():
        return True
    else:
        return False


# Custom function to draw a triangle
def draw_triangle(win, p1, p2, p3, color):
    # This is different compared to the others ( another parameter)
    triangle = Polygon(p1, p2, p3)
    triangle.setFill(color)
    triangle.draw(win)


def main():
    win_width = 800
    win_height = 600

    # Create the window with the size 800x600
    win = GraphWin("PxPaint", win_width, win_height)

    # Create the grey menu bar below the buttons
    menu_bar_rect = Rectangle(Point(0, 0), Point(78, win_height))  # 78 because of the 8px border
    menu_bar_rect.setFill("lightgrey")
    menu_bar_rect.draw(win)

    # Create the white canvas
    win.setBackground("white")

    # TOOLS
    # Create line button with (S) marker for default tool
    line_btn = Rectangle(Point(10, 10), Point(70, 40))
    line_btn.setFill("lightgray")
    line_btn.draw(win)
    line_text = Text(line_btn.getCenter(), "Line (S)")
    line_text.draw(win)

    # Create selectable rectangle button
    rect_btn = Rectangle(Point(10, 60), Point(70, 90))
    rect_btn.setFill("lightgray")
    rect_btn.draw(win)
    rect_text = Text(rect_btn.getCenter(), "Rectangle")
    rect_text.draw(win)

    # Create selectable circle button
    circle_btn = Rectangle(Point(10, 110), Point(70, 140))
    circle_btn.setFill("lightgray")
    circle_btn.draw(win)
    circle_text = Text(circle_btn.getCenter(), "Circle")
    circle_text.draw(win)

    # Create selectable triangle button
    triangle_btn = Rectangle(Point(10, 160), Point(70, 190))
    triangle_btn.setFill("lightgray")
    triangle_btn.draw(win)
    triangle_text = Text(triangle_btn.getCenter(), "Triangle")
    triangle_text.draw(win)

    # Create selectable erase button
    erase_btn = Rectangle(Point(10, 210), Point(70, 240))
    erase_btn.setFill("lightgray")
    erase_btn.draw(win)
    erase_text = Text(erase_btn.getCenter(), "Erase")
    erase_text.draw(win)

    # COLORS
    # Selectable red colour button
    red_btn = Rectangle(Point(10, 270), Point(70, 320))
    red_btn.setFill("red")
    red_btn.draw(win)
    red_text = Text(red_btn.getCenter(), "Red")
    red_text.draw(win)

    # Selectable green colour button
    green_btn = Rectangle(Point(10, 320), Point(70, 370))
    green_btn.setFill("green")
    green_btn.draw(win)
    green_text = Text(green_btn.getCenter(), "Green")
    green_text.draw(win)

    # Selectable blue colour button
    blue_btn = Rectangle(Point(10, 370), Point(70, 420))
    blue_btn.setFill("blue")
    blue_btn.draw(win)
    blue_text = Text(blue_btn.getCenter(), "Blue")
    blue_text.draw(win)

    # Selectable yellow colour button
    yellow_btn = Rectangle(Point(10, 420), Point(70, 470))
    yellow_btn.setFill("yellow")
    yellow_btn.draw(win)
    yellow_text = Text(yellow_btn.getCenter(), "Yellow")
    yellow_text.draw(win)

    # Selectable orange colour button
    orange_btn = Rectangle(Point(10, 470), Point(70, 520))
    orange_btn.setFill("orange")
    orange_btn.draw(win)
    orange_text = Text(orange_btn.getCenter(), "Orange")
    orange_text.draw(win)

    # Selectable black colour button
    black_btn = Rectangle(Point(10, 520), Point(70, 570))
    black_btn.setFill("black")
    black_btn.draw(win)
    black_text = Text(black_btn.getCenter(), "Black (S)")
    black_text.setTextColor("white")
    black_text.draw(win)

    # Set default tools
    current_color = "black"
    current_tool = "line"
    isOnCircleTool = bool(0)

    start_point = None

    while True:

        try:
            click_point = win.getMouse()
        except:
            # When the user closes the window, graphics.py likes to throw an error. This sends a message explaining,
            # and closes the program.
            print("Window is closed now, can't really fetch mouse clicks anymore...")
            exit()

        # Check if the user clicked on the button by checking if the click point is within the buttons coords
        if line_btn.getP1().getX() <= click_point.getX() <= line_btn.getP2().getX() and \
                line_btn.getP1().getY() <= click_point.getY() <= line_btn.getP2().getY():
            # Current tool is now line
            current_tool = "line"
            # Change every tool text to default, except for line tool, which get a (S) marker
            rect_text.setText("Rectangle")
            circle_text.setText("Circle")
            triangle_text.setText("Triangle")
            erase_text.setText("Erase")
            line_text.setText("Line (S)")
            continue

        # Check if the user clicked on the button by checking if the click point is within the buttons coords
        if rect_btn.getP1().getX() <= click_point.getX() <= rect_btn.getP2().getX() and \
                rect_btn.getP1().getY() <= click_point.getY() <= rect_btn.getP2().getY():
            # Current tool is now rectangle
            current_tool = "rectangle"
            # Change every tool text to default, except for rectangle tool, which get a (S) marker
            rect_text.setText("Rect (S)")
            circle_text.setText("Circle")
            triangle_text.setText("Triangle")
            erase_text.setText("Erase")
            line_text.setText("Line")
            continue

        # Check if the user clicked on the button by checking if the click point is within the buttons coords
        if circle_btn.getP1().getX() <= click_point.getX() <= circle_btn.getP2().getX() and \
                circle_btn.getP1().getY() <= click_point.getY() <= circle_btn.getP2().getY():
            # Current tool is now circle
            current_tool = "circle"
            # Change every tool text to default, except for circle tool, which get a (S) marker
            rect_text.setText("Rectangle")
            circle_text.setText("Circle (S)")
            triangle_text.setText("Triangle")
            erase_text.setText("Erase")
            line_text.setText("Line")
            continue

        # Check if the user clicked on the button by checking if the click point is within the buttons coords
        if triangle_btn.getP1().getX() <= click_point.getX() <= triangle_btn.getP2().getX() and \
                triangle_btn.getP1().getY() <= click_point.getY() <= triangle_btn.getP2().getY():
            # Current tool is now triangle
            current_tool = "triangle"
            # Change every tool text to default, except for triangle tool, which get a (S) marker
            rect_text.setText("Rectangle")
            circle_text.setText("Circle")
            triangle_text.setText("Triangle (S)")
            erase_text.setText("Erase")
            line_text.setText("Line")
            continue

        # Check if the user clicked on the button by checking if the click point is within the buttons coords
        if erase_btn.getP1().getX() <= click_point.getX() <= erase_btn.getP2().getX() and \
                erase_btn.getP1().getY() <= click_point.getY() <= erase_btn.getP2().getY():
            # Current tool is now erase
            current_tool = "erase"
            # Change every tool text to default, except for erase tool, which get a (S) marker
            rect_text.setText("Rectangle")
            circle_text.setText("Circle")
            triangle_text.setText("Triangle")
            line_text.setText("Line")
            erase_text.setText("Erase (S)")
            continue

        # Check if the user clicked on the button by checking if the click point is within the buttons coords
        if red_btn.getP1().getX() <= click_point.getX() <= red_btn.getP2().getX() and \
                red_btn.getP1().getY() <= click_point.getY() <= red_btn.getP2().getY():
            # Current colour is now red
            current_color = "red"
            # Change every colour text to default, except for red colour, which get a (S) marker
            green_text.setText("Green")
            blue_text.setText("Blue")
            yellow_text.setText("Yellow")
            orange_text.setText("Orange")
            black_text.setText("Black")
            red_text.setText("Red (S)")
            continue

        # Check if the user clicked on the button by checking if the click point is within the buttons coords
        if green_btn.getP1().getX() <= click_point.getX() <= green_btn.getP2().getX() and \
                green_btn.getP1().getY() <= click_point.getY() <= green_btn.getP2().getY():
            # Current colour is now green
            current_color = "green"
            # Change every colour text to default, except for green colour, which get a (S) marker
            green_text.setText("Green (S)")
            blue_text.setText("Blue")
            yellow_text.setText("Yellow")
            orange_text.setText("Orange")
            black_text.setText("Black")
            red_text.setText("Red")
            continue

        # Check if the user clicked on the button by checking if the click point is within the buttons coords
        if blue_btn.getP1().getX() <= click_point.getX() <= blue_btn.getP2().getX() and \
                blue_btn.getP1().getY() <= click_point.getY() <= blue_btn.getP2().getY():
            # Current colour is now blue
            current_color = "blue"
            # Change every colour text to default, except for blue colour, which get a (S) marker
            green_text.setText("Green")
            yellow_text.setText("Yellow")
            orange_text.setText("Orange")
            blue_text.setText("Blue (S)")
            black_text.setText("Black")
            red_text.setText("Red")
            continue

        # Check if the user clicked on the button by checking if the click point is within the buttons coords
        if yellow_btn.getP1().getX() <= click_point.getX() <= yellow_btn.getP2().getX() and \
                yellow_btn.getP1().getY() <= click_point.getY() <= yellow_btn.getP2().getY():
            # Current colour is now yellow
            current_color = "yellow"
            # Change every colour text to default, except for yellow colour, which get a (S) marker
            green_text.setText("Green")
            blue_text.setText("Blue")
            orange_text.setText("Orange")
            yellow_text.setText("Yellow (S)")
            black_text.setText("Black")
            red_text.setText("Red")
            continue

        # Check if the user clicked on the button by checking if the click point is within the buttons coords
        if orange_btn.getP1().getX() <= click_point.getX() <= orange_btn.getP2().getX() and \
                orange_btn.getP1().getY() <= click_point.getY() <= orange_btn.getP2().getY():
            # Current colour is now orange
            current_color = "orange"
            # Change every colour text to default, except for orange colour, which get a (S) marker
            green_text.setText("Green")
            blue_text.setText("Blue")
            yellow_text.setText("Yellow")
            orange_text.setText("Orange (S)")
            black_text.setText("Black")
            red_text.setText("Red")
            continue

        # Check if the user clicked on the button by checking if the click point is within the buttons coords
        if black_btn.getP1().getX() <= click_point.getX() <= black_btn.getP2().getX() and \
                black_btn.getP1().getY() <= click_point.getY() <= black_btn.getP2().getY():
            # Current colour is now black
            current_color = "black"
            # Change every colour text to default, except for black colour, which get a (S) marker
            green_text.setText("Green")
            blue_text.setText("Blue")
            yellow_text.setText("Yellow")
            orange_text.setText("Orange")
            black_text.setText("Black (S)")
            red_text.setText("Red")
            continue

        if current_tool is None:
            continue

        if current_tool == "line":
            # Checks if the X coordinate of a mouse click is between 0 and 78
            # and if the Y coordinate is between 0 and the window height, to determine if the click occurred
            # within the menu bar area. if it is there, the click is ignored.
            if 0 <= click_point.getX() <= 78 and 0 <= click_point.getY() <= win_height:
                continue
            if start_point is None:
                # Set the start point for drawing the line
                start_point = click_point
            else:
                # Call draw line function
                draw_line(win, start_point, click_point, current_color)
                start_point = None

        elif current_tool == "rectangle":
            # Call menubar click check function
            if 0 <= click_point.getX() <= 78 and 0 <= click_point.getY() <= win_height:
                continue
            if start_point is None:
                # Set the start point for drawing the line
                start_point = click_point
            else:
                # Call draw line function
                draw_rectangle(win, start_point, click_point, current_color)
                start_point = None

        elif current_tool == "circle":
            # Call menubar click check function
            if 0 <= click_point.getX() <= 78 and 0 <= click_point.getY() <= win_height:
                continue
            if start_point is None:
                # Set the start point for drawing the line
                start_point = click_point
            else:
                radius = abs(start_point.getX() - click_point.getX())
                circle = Circle(start_point, radius)
                if circle_overlaps_menu(circle, menu_bar_rect):
                    circle_text_big = Text(Point(400, 50), "Circle too big!")
                    circle_text_big.draw(win)
                    circle_text_big.setSize(20)
                    circle_text_big.setStyle("bold")
                    time.sleep(0.5)  # Make the thread sleep for 0.5s. This has some drawbacks, but will do for now.
                    circle_text_big.undraw()
                    print("circle too big")
                else:
                    draw_circle(win, start_point, radius, current_color)

                start_point = None

        elif current_tool == "triangle":
            # Call menubar click check function
            if 0 <= click_point.getX() <= 78 and 0 <= click_point.getY() <= win_height:
                continue
            if start_point is None:
                # Set the start point for drawing the line
                start_point = click_point
            elif start_point is not None:
                # Get the SECOND point for drawing it
                second_point = click_point
                # Draw using the start point, a vertical aligned point, and the second point
                draw_triangle(win, start_point, Point(start_point.getX(), second_point.getY()), second_point,
                              current_color)
                start_point = None

        elif current_tool == "erase":
            # Call menubar click check function
            if 0 <= click_point.getX() <= 78 and 0 <= click_point.getY() <= win_height:
                continue

            # Find all items that overlap the click point
            items = win.find_overlapping(click_point.getX(), click_point.getY(), click_point.getX(), click_point.getY())

            # for each of those items, delete them.
            for item in items:
                win.delete(item)


# Calls main function
main()
