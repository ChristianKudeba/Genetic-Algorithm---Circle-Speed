from graphics import *
import copy
import random

def main():
    win = GraphWin("Genetic Algorithm: Speed", 500, 500) # set up window

    def circle_setup(circle, colour): # For drawing a circle
        circle.setFill(colour)
        circle.draw(win)

    def quick_setup(circleStatus):   # For drawing all the circles
        circle_setup(circleStatus[0], 'blue')
        circle_setup(circleStatus[1], 'purple')
        circle_setup(circleStatus[2], 'red')
        circle_setup(circleStatus[3], 'pink')
        circle_setup(circleStatus[4], 'orange')
        circle_setup(circleStatus[5], 'yellow')
        circle_setup(circleStatus[6], 'green')
        circle_setup(circleStatus[7], 'teal')

    def check_Speed(speedlist): # checks if target speed has been reached
        for i in speedlist:
            if i >= 4:
                return True

    # Circle speeds
    speed = [1 + random.random(),1 + random.random(),1 + random.random(),1 + random.random(),1 + random.random(),1 + random.random(),1 + random.random(),1 + random.random()]

    # Initial circle coordinates
    pt = [Point(50, 75),Point(50, 125),Point(50, 175),Point(50, 225),Point(50, 275),Point(50, 325),Point(50, 375),Point(50, 425)]

    # list of circles
    circlesStart = [Circle(pt[0], 10),Circle(pt[1], 10),Circle(pt[2], 10),Circle(pt[3], 10),Circle(pt[4], 10),Circle(pt[5], 10),Circle(pt[6], 10),Circle(pt[7], 10)]

    # generations of evolution
    generations = 0

    # Just some nice start up text
    start_string = Text(Point(250, 250), "Target speed: 4\n\n"
                                         "Initial speeds:\n"
                                         "Blue: " + str(speed[0]) + "\n"
                                         "Purple:" + str(speed[1]) + "\n"
                                         "Red:" + str(speed[2]) + "\n"
                                         "Pink:" + str(speed[3]) + "\n"
                                         "Orange:" + str(speed[4]) + "\n"
                                         "Yellow:" + str(speed[5]) + "\n"
                                         "Green:" + str(speed[6]) + "\n"
                                         "Teal:" + str(speed[7]) + "\n\n"
                                         "CLICK TO START")
    start_string.draw(win)

    win.getMouse()  # start race animation on mouse click

    start_string.undraw()

    while not(check_Speed(speed)):

        racingCircles = copy.deepcopy(circlesStart) # creates copy of initial positions - changes to copy don't change origianl
        quick_setup(racingCircles) # Draws the circles

        for i in range(100): # race animation - make circles move to the right
            for j in range(len(racingCircles)):
                racingCircles[j].move(speed[j], 0)

        for k in range(len(racingCircles)): # reset race animation
            racingCircles[k].undraw()

        # replace the 2 slowest circles speeds with genetics of the faster ones
        speedorder = copy.deepcopy(speed)
        speedorder.sort(reverse=True)
        for m in range(len(speed)):
            if speed[m] == speedorder[-1]:
                speed[m] = ((speedorder[0] + speedorder[1])/2) + 0.1*random.uniform(-1, 1)
            elif speed[m] == speedorder[-2]:
                speed[m] = ((speedorder[2] + speedorder[3])/2) + 0.1*random.uniform(-1, 1)

        generations += 1



    #Convoluted way of finding out the winner
    speedorder = copy.deepcopy(speed)
    speedorder.sort(reverse=True)

    winner = ""
    winnerindex = 0
    for m in range(len(speed)):
        if speed[m] == speedorder[0]:
            winnerindex = m

    if winnerindex == 0:
        winner = "Blue"
    elif winnerindex == 1:
        winner = "Purple"
    elif winnerindex == 2:
        winner = "Red"
    elif winnerindex == 3:
        winner = "Pink"
    elif winnerindex == 4:
        winner = "Orange"
    elif winnerindex == 5:
        winner = "Yellow"
    elif winnerindex == 6:
        winner = "Green"
    elif winnerindex == 7:
        winner = "Teal"
    # End of convoluted way of finding out the winner


    # Just some nice ending text
    end_string = Text(Point(250,250), "Winner: " + winner + "\n\n"
                                      "Generations to reach target: " + str(generations) + "\n\n"
                                      "Final speeds:\n"
                                      "Blue: " + str(speed[0]) + "\n"
                                      "Purple:" + str(speed[1]) + "\n"
                                      "Red:" + str(speed[2]) + "\n"
                                      "Pink:" + str(speed[3]) + "\n"
                                      "Orange:" + str(speed[4]) + "\n"
                                      "Yellow:" + str(speed[5]) + "\n"
                                      "Green:" + str(speed[6]) + "\n"
                                      "Teal:" + str(speed[7]) + "\n\n"
                                      "CLICK TO EXIT")
    end_string.draw(win)

    # Mouse click to leave
    win.getMouse()
    win.close()

main()