#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  File: Chess.py

#  Description: Prints out the number of solutions to the N-Queens problem where N denotes the number
#  of queens and the size of the board

#  Student Name: Gaytri Vasal

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 3/20/22

#  Date Last Modified: 3/21/22

import sys

class Queens (object):
  def __init__ (self, n = 8):
    self.board = []
    self.solutions = []
    self.n = n
    for i in range (self.n):
      row = []
      for j in range (self.n):
        row.append ('*')
      self.board.append (row)

  # print the board
  def print_board (self):
    for i in range (self.n):
      for j in range (self.n):
        print (self.board[i][j], end = ' ')
      print ()
    print ()

  # check if a position on the board is valid
  def is_valid (self, row, col):
    for i in range (self.n):
      if (self.board[row][i] == 'Q') or (self.board[i][col] == 'Q'):
        return False
    for i in range (self.n):
      for j in range (self.n):
        row_diff = abs (row - i)
        col_diff = abs (col - j)
        if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
          return False
    return True
    
  # do the recursive backtracking
  def recursive_solve (self, col):
    if (col == self.n):
        # appends to a list of solutions
       self.solutions.append(self.board)
    else:
      for i in range (self.n):
        if (self.is_valid (i, col)):
          self.board[i][col] = 'Q'
          # backtracks
          self.recursive_solve(col + 1)
          self.board[i][col] = '*'
      
  

  # if the problem has a solution print the board
  def solve (self):
    for i in range (self.n):
      if (self.recursive_solve(i)):
        self.print_board()
        

def main():
  # read the size of the board
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)

  # create a chess board
  game = Queens (n)
  

  # place the queens on the board and count the solutions
  # starts on col 0
  game.recursive_solve(0)


  # print the number of solutions
  print(len(game.solutions))

  
 
if __name__ == "__main__":
  main()
