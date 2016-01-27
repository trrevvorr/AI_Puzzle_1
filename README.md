# AI_Homework_2
Exercise 2 for CS 5400 - Artificial Intelligence (Missionaries and Cannibals problem)

##HOW TO USE PROGRAM
*Build with Python 2.7*
To find the solution to the puzzle discribed below, simply build and run the program. The program will print out all the actions caried out. If you wish to see a visual representation of the states, uncomment lines 188 and 189. 

##Puzzle Statement (from the book)
The missionaries and cannibals problem is usually stated as follows. Three mission-aries and three cannibals are on one side of a river, along with a boat that can hold one or two people. Find a way to get everyone to the other side without ever leaving a group of mis-sionaries in one place outnumbered by the cannibals in that place. This problem is famous in Al because it was the subject of the first paper that approached problem formulation from an analytical viewpoint (Amarel, 1968).
a. Formulate the problem precisely, making only those distinctions necessary to ensure a
valid solution. Draw a diagram of the complete state space.
b. Implement and solve the problem optimally using an appropriate search algorithm. Is it
a good idea to check for repeated states?
c. Why do you think people have a hard time solving this puzzle, given that the state space is so simple?

##Extra Info (from Dr. T)
Note that the only valid actions consist of moving the boat from one side to the other side of the river, with either one or two people aboard to pilot it (so there are no intermediate states where the boat is on the river). Your task is to:
1. Precisely formulate the problem by:
a. Defining a state by giving the minimal set of information needed to uniquely identify it.
b. Specifying the initial state.
c. Defining a function ACTIONS(s) for an arbitrary state s which returns the set of actions that can be executed in state s.
d. Definining a transition model by specifying a function RESULT(s,a) which returns the state that results from executing action a in state s.
e. Defining a test to determine whether a given state is a goal state.
f. Defining the step cost (which also gives us the path cost as that's merely the sum of all the step costs associated with a path).
2. Professionally render a diagram of the complete state space employing appropriate software such as Microsoft Visio or the free open-source software Dia.
3. Find and report a path in the state space from the initial state to a goal state (i.e., a solution).
See pages 70-73 in the textbook under "Toy problems" for examples of formulating a problem.
