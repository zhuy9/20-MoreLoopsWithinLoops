"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Yuchen Zhu DARREN
"""  # D: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    run_test_draw_upside_down_wall()


def run_test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Upside-down wall, Tests 1 and 2')

    rectangle = rg.Rectangle(rg.Point(125, 230), rg.Point(155, 250))
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(375, 175), rg.Point(425, 225))
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()


def draw_upside_down_wall(rectangle, n, window):
    """
    See   MoreWalls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" on the given window, where:
      -- The BOTTOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is nonnegative.
    """
    # ------------------------------------------------------------------
    # D: 2. Implement and test this function.
    #     Some tests are already written for you (above).
    # ------------------------------------------------------------------
    # move the rectangle to upper-left
    length = abs(rectangle.corner_2.x - rectangle.corner_1.x)
    width = abs(rectangle.corner_1.y - rectangle.corner_2.y)
    rectangle.corner_1.x -= ((n-1) / 2 * length)
    rectangle.corner_2.x -= ((n-1) / 2 * length)
    rectangle.corner_2.y -= ((n-1) * width)
    rectangle.corner_1.y -= ((n-1) * width)
    # loops within loops
    for i in range(n):
        for j in range(n-i):
            new_rect = rg.Rectangle(rectangle.corner_1, rectangle.corner_2)
            new_rect.attach_to(window)
            window.render()
            rectangle.corner_1.x += length
            rectangle.corner_2.x += length
        rectangle.corner_2.y += width
        rectangle.corner_1.y += width
        rectangle.corner_2.x -= ( (n-i-1) * length + 0.5 * length )
        rectangle.corner_1.x -= ( (n-i-1) * length + 0.5 * length )


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
