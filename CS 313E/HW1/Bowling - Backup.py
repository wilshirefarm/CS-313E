#  File: Bowling.py
#  Description: Reads in bowling scores and outputs the frames
#  Student's Name: Wilshire Liu
#  Student's UT EID: WL7583
#  Course Name: CS 313E 
#  Unique Number: 51325
#
#  Date Created: 9/5/2016
#  Date Last Modified: 9/9/2016

def main():

    #inputs the "scores.txt" file and counts how many lines are in it
    scores = open("scores.txt", "r")
    num_players = 0
    for p in scores:
        num_players += 1
    #resets the reading of "scores.txt" to the beginning
    scores.seek(0)

    #reads each line of "scores.txt" individually and changes the each line into a list of scores
    for s in range(num_players):
        player = scores.readline()
        player = player.split()

        #hard codes the frame format   
        print("  1   2   3   4   5   6   7   8   9    10")
        print("+---+---+---+---+---+---+---+---+---+-----+")

        #uses a while loop to output the row with the individual scores (the output of frames 1-9 are different from the output of frame 10)
        score_row = "|"
        i = 0
        frame = 1
        while (i < len(player) - 1):
            if (frame < 10):
                if (player[i] == "X"):
                    score_row = score_row + "X  |"
                elif (player[i] == "/"):
                    score_row = score_row + "/|"
                else:
                    score_row = score_row + player[i] + " " + player[i+1] + "|"
                    i += 1
                frame += 1
            elif (frame == 10):
                if (player[i] == "X"):
                    score_row = score_row + player[i] + " " + player[i+1] + " " + player[i+2] + "|"
                elif (player[i+1] == "/"):
                    score_row = score_row + player[i] + " " + player[i+1] + " " + player[i+2] + "|"
                else:
                    score_row = score_row + player[i] + " " + player[i+1] + "  |"
                frame += 1
            i += 1
        print(score_row)

        #changes "-" to 0's    
        for z in range(len(player)):
            if (player[z] == "-"):
                player[z] = "0"

        #calculates points by going through each scenario that can happen (this method only reads in the first score of a frame, so a spare is not possible)
        def calculatePoints(total_points, player, i):
            #if player hits a strike
            if (player[i] == "X"):
                if (player[i+1] == "X"):
                    if (player[i+2] == "X"):
                        total_points = total_points + 30
                    else:
                        total_points = total_points + 20 + int(player[i+2])
                else:
                    if (player[i+2] == "/"):
                        total_points = total_points + 20
                    else:
                        total_points = total_points + 10 + int(player[i+1]) + int(player[i+2])
            #if player does not hit a strike
            else:
                if (player[i+1] == "/"):
                    if (player[i+2] != "X"):
                        total_points = total_points + 10 + int(player[i+2])
                    elif (player[i+2] == "X"):
                        total_points = total_points + 20
                else:
                    total_points = total_points + int(player[i]) + int(player[i+1])
            return total_points

        #formats the points row for frames 1-9    
        def formatPoints(points_row, total_points):
            if (total_points < 10):
                points_row = points_row + "  " + str(total_points) + "|"
            elif (total_points >= 10 and total_points < 100):
                points_row = points_row + " " + str(total_points) + "|"
            elif (total_points >= 100 and total_points < 301):
                points_row = points_row + str(total_points) + "|"
            return points_row

        #formats the points row for frame 10
        def formatPointsForFrameTen(points_row, total_points):
            if (total_points < 10):
                points_row = points_row + "    " + str(total_points) + "|"
            elif (total_points >= 10 and total_points < 100):
                points_row = points_row + "   " + str(total_points) + "|"
            elif (total_points >= 100 and total_points < 301):
                points_row = points_row + "  " + str(total_points) + "|"
            return points_row

        #uses a while loop to output the row with the points (the output of frames 1-9 are different from the output of frame 10)
        points_row = "|"
        total_points = 0
        i = 0
        frame = 1
        while (i < len(player) - 1):
            if (frame < 10):
                total_points = calculatePoints(total_points, player, i)
                points_row = formatPoints(points_row, total_points)
                if (player[i] != "/" and player[i] != "X"):
                    if (int(player[i]) >= 0 and int(player[i]) <= 9):
                        i += 1
                frame += 1
            elif (frame == 10):
                total_points = calculatePoints(total_points, player, i)
                points_row = formatPointsForFrameTen(points_row, total_points)
                frame += 1
            i += 1
        print(points_row)

        #hard codes the frame format
        print("+---+---+---+---+---+---+---+---+---+-----+")
        print("\n")

main()
