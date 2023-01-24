
PROJECT DESCRIPTION AND GUIDELINES PROVIDED ON ASSIGNMENT INSTRUCTIONS

The Eight Queens Problem is a fairly old problem that has been well discussed and researched. The first published reference to this problem was in a German Chess magazine in 1848 by Max Bezzel. In 1850, Franz Nauck published all 92 solutions to the problem for an 8x8 board. S. Gunther in 1874 suggested a method for finding solutions by using determinants and J.W.L. Glaisher extended this method. E. Dijkstra published a detailed description of the solution to the problem as a depth-first backtracking algorithm.

The original statement of the problem ran as follows - how can we place eight queens on a regular chess board such that no queen can capture another. It turns out there is no unique solution but 92 possible solutions of which only 12 are distinct. The 12 distinct solutions can generate all other solutions through reflections and/or rotations. Here is a table that gives the size of the board, all possible solutions, and all distinct solutions.

Size	All Solutions	Distinct Solutions
1	1	1
2	0	0
3	0	0
4	2	1
5	10	2
6	4	1
7	40	6
8	92	12
9	352	46
10	724	92
11	2680	341
12	14200	1787

This is a classic back-tracking problem.

Read the size of the board from a file called chess.in. The number n will between 1 and 12 inclusive. Generate all possible solutions for a board of that size. Keep a count of the number of solutions and print the total number of solutions. For a board of size 8, your output should be 92.

To run this code on the command line on Mac, you will do:

python3 Chess.py < chess.in

To run the code on the command line on a Windows machine, you will do:

python Chess.py < chess.in
