# python program to draw a five click house
# import graphics library
from graphics import*
# include the math and time library
import math as m
from time import sleep
# main function
def main():
    # initiate the graphics window
    win=GraphWin("Five Clicks House", 500, 500)
    win.setCoords(-10, -10, 10, 10)
    # draw a rectangle representing the frame
    message=Text(Point(0,8)), "Click two opposite sides on the screen for drawing rectangular frame"
    message.draw(win)

    # capture the points of mouse click
    point1=win.getMouse()
    point2=win.getMouse()

    # determine the coordinates
    x1=point1.getX()
    y1=point1.getY()
    x2=point2.getX()
    y2=point2.getY()
    r = Rectangle(point1, point2)
    r.draw(win)
    message.undraw()

    # third click for center of the door
    message=Text(Point(0, y1-1), "Third click for the door")
    message.draw(win)
    point3=win.getMouse()
    x3=point3.getX()
    y3=point3.getY()

    # door for one-fifth width
    r_width=x2-x1
    door=Rectangle(Point(x3-(1/10*r_width),y2),Point(x3+(1/10*r_width)y3))
    door.draw(win)
    message.setText("Fourth click for the window")

    # fourth click for square window
    point4=win.getMouse()
    x4=point4.getX()
    y4=point4.getY()
    w=1/20*r_width
    # to set the window width
    window=Rectangle(Point((x4-w), (y4-w)),Point((x4+w), (y4+w)))
    window.draw(win)
    message.setText("Fifth click for roof of the house")

    # fifth click of roof of house
    point5=win.getMouse()

    # indicate the roof by drawing lines connecting peak point to the corners of top edge of house
    line1=Line(point1,point5)
    line1.draw(win)
    line2=Line(point5, Point(x2,y1))
    line2.draw(win)
    message.setText("Five-click house created")
    win.getMouse()
    win.close()
    sleep(20)

main()
