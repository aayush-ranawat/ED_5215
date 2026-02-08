#DO NOT MODIFY FOR HERE
import random
from queue import PriorityQueue, Queue
import numpy as np
import matplotlib.pyplot as plt

###############################        NOTES           ############################################################
#1. Do not import an additional packages, read about the imported packages and learn to use them to solve to problem: Queue
#2. Stack is readily available data type in python use that for DFS, read about it
#3. Only when you run the code you will see GUI output, however when evaluating it will not show GUI, it will show path calcualted by your algorithm and corrct path if your path is not correct.
#4. You can add any number of additional functions that you can call from already defined functions below
#5. DO NOT MODIFY name, arguments or the return type othrwise your code will not get auto evaluated

#################################################################################################################################

#This fuction is to be used only with UCS, it returns edge cost given the node and an action. Don't worry about how the costs are generated just use it as suggested
#Arguments:
# 1. costs: contains cost between a given node and its neighbor
# 2. node: this is the coordInate of the current node givn as [x,y]
# 3. neighbor: this is the coordinate of the neighbor node givn as [x,y]

# Returns: cost to go from the node to the neighbour

def get_edge_cost(costs, node, neighbor):
    nx, ny = node
    return costs[nx, ny]

#################################################################################################################################

#This function returns all valid neighbours given the maze and the node

#Arguments:
# 1. maze: this is the search space of size X (rows) x Y (columns), its a numpy array of size X rows and Y columns
# 2. node: this is the coordinate of the current node givn as [x,y]

# Returns: all the neighbors to be added to the Stack (DFS) or Queue (BFS) or Prioity queue (UCS)

#Note: Put the neighbours in the Stack/Queue in same order as they are returned from this function
def get_neighbors(maze, node):
    x, y = node
    neighbors = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < maze.shape[0] and 0 <= ny < maze.shape[1] and maze[nx, ny] == 0:
            neighbors.append((nx, ny))
    return neighbors

################################################################################################################################# TO HERE



#MODIFY CONTENT FROM THIS LINE ONWARDS HOWEVER DO NOT MODIFY FUNCTION NAMES ARGUMENTS OR RETURN TYPE


#This function should implement BFS algorithm

#Arguments:
# 1. maze: this is the search space of size X (rows) x Y (columns), its a numpy array of size X rows and Y columns
# 2. start: coordinate of the start node givn as [x,y]
# 3. goal: coordinate of the goal node givn as [x,y]

# Return values
# 1. a list of nodes containng path from START to GOAL, rememebr the first node in this list should be START and the last one should be GOAL

def bfs(maze, start, goal):
    path = [] #this should contai list of nodes [start, (20,30), (21,30), ...., goal] as a path from start to goal
    
    
    
    
    
    return path

################################################################################################################################# 
#This function should implement DFS algorithm

#Arguments:
# 1. maze: this is the search space of size X (rows) x Y (columns), its a numpy array of size X rows and Y columns
# 2. start: coordinate of the start node givn as [x,y]
# 3. goal: coordinate of the goal node givn as [x,y]

# Return values
# 1. a list of nodes containng path from START to GOAL, rememebr the first node in this list should be START and the last one should be GOAL
def dfs(maze, start, goal):
    path = []
    
    
    
    
    
    return path

################################################################################################################################# 
#This function should implement UCS algorithm

#Arguments:
# 1. maze: this is the search space of size X (rows) x Y (columns), its a numpy array of size X rows and Y columns
# 2. start: coordinate of the start node givn as [x,y]
# 3. goal: coordinate of the goal node givn as [x,y]

# Return values
# 1. a list of nodes containng path from START to GOAL, rememebr the first node in this list should be START and the last one should be GOAL
def ucs(maze, costs, start, goal):
    path = []
    
    
    
    
    
    return path
################################################################################################################################# 
#Any oher functions you may want to define