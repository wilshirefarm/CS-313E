#  File: Queens.py
#  Description: Solves the queens problem for board size n
#  Student's Name: Wilshire Liu
#  Student's UT EID: WL7583
#  Course Name: CS 313E 
#  Unique Number: 51325
#
#  Date Created: 11/8/16
#  Date Last Modified: 11/10/16

class QueensProblem:

    def __init__(self, numQueens):          #initiates a queens problem with size n
        self.size = numQueens
        self.row = numQueens
        self.col = numQueens
        self.count = 0                      #count is 0 at first
        self.board = []
        for r in range(self.row):           #makes initial board:
            self.board.append([])           #each row gets a empty list
            for c in range(self.col):
                self.board[r].append("*")   #each column in each row gets a *

    def __str__(self):
        string = ""
        for r in range(self.row):
            for c in range(self.col):                       #print out each * in each row
                string = string + self.board[r][c] + " "
            string = string + "\n"                          #after all the * are printed out in each row, print a new line
        return string

    def isValidPlace(self, row, col):
        for c in range(self.col):                               #loop through columns but does not look at the square the Q is initially placed in
            if ((c != col) and (self.board[row][c] == "Q")):    #if a queen is found in row the Q is placed in, return false
                return False
        for r in range(self.row):                               #loop through rows but does not look at the square the Q is initially place in
            if ((r != row) and (self.board[r][col] == "Q")):    #if a queen is found in the column the Q is place in, return false
                return False
        added = row + col                                       #diagonal rows have the same sum and difference of r and c
        subbed = row - col
        for r in range(self.row):                               #loop through each individual square
            for c in range(self.col):
                if (((r + c) == added or (r - c) == subbed) and not ((r == row) and (c == col))):       #does not look at the square the Q was intially place in    
                    if (self.board[r][c] == "Q"):               #if the square is in a diagonal and a Q is there, return false
                        return False
        return True                                             #valid placement, so return True

    def solve(self, n):
        r = self.size - n                               #loop variable to count through the rows
        if (n == 0):                                    #base case
            self.count += 1                             #found a solution so increment the solution counter
            print("Solution: #", self.count)            #print the solution
            print(self)
            return False                                #returns false so it keeps trying to find more solutions
        for c in range(self.col):                       #loops through each column in a row
            self.board[r][c] = "Q"                      #places a Q in the a square
            if (self.isValidPlace(r, c) and self.solve(n - 1)):     #first check if where the Q place is valid
                return True                                         #and then see if calling the method again with the row one under returns true, then return true
            self.board[r][c] = "*"                                  #if Q cannot be placed there, remove the Q from that square and try the next square
        return False                                #reached the end of the loop, which means no Q can be placed in that row, so return false
                                                    #and backtrack to the previous row            
def main():

    size = int(input("Enter the size of the square board: "))       #prompt the user for the size of the board
    if (size < 4):
        print("Invalid input.")                         #if the size is less than 4, no solutions possible
    else:
        problem = QueensProblem(size)                   #creates a board with the size inputed
        problem.solve(size)                             #calls the recursive method to find the solutions

main()
