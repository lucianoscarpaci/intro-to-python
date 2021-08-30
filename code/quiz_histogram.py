# program to draw a histogram of quiz scores
# import the graphics library
from graphics import *
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

def main():
    File_in = open('testfile.txt', 'r')

    #determine number of scores in the file
    string_number = File_in.readlines()
    count_list = [0] * 11

    #iterate over the number in the file and find frequency of the scores
    for num in string_number:
        count_list[int(num)] = count_list[int(num)] + 1
    
    #create a window and set the coordinates
    window = Graphics('Quiz score histogram', 400, 200)
    window.setCoord(-10, -10, 100, 120)
    window.setBackground('White')
    
    # draw the histogram
    for i in range(11):
        text = Text(Point(-5 + i * 10, 5), str(i))
        text.setSize(10)
        text.draw(window)
        height = count_list[i] * 100 / max(count_list)
        if count_list[i] != 0:
            bar = rectangle(Point(-7.5 + i * 10, 0), Point(-2.5 + i * 10, height))
            bar.draw(window)
    # close the file and the window
    window.getMouse()
    window.close()
    File_in.close()
main()