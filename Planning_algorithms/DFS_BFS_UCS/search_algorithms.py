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

    fringe=Queue()  # fifo queue
    closed_set=set()

    fringe.put(start)
    closed_set.add(start)

    parent_dict={start:None}



    while not fringe.empty():# no more nodes to expand
        pop_node=fringe.get()
        
      
        if pop_node==goal:
            print("path found")
            while pop_node is not None:
                path.append(pop_node)
                pop_node=parent_dict[pop_node]

            return path[::-1]
        
        
        
       

        neighbors=get_neighbors(maze,pop_node)
        

        for n in neighbors :
            if n not in closed_set :
                fringe.put(n)
                closed_set.add(n)
                parent_dict[n]=pop_node
                




        

        


    
    
    
    
    
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
    i=0

    fringe=PriorityQueue()
    closed_set=set()

    fringe.put((i,start))
    closed_set.add(start)

    parent_dict={start:None}



    while not fringe.empty():

        pop_node=fringe.get()
       

        if pop_node[1]==goal:
            print("path found")
            current_node=pop_node[1]

            while current_node is not None:
                path.append(current_node)
                current_node=parent_dict[current_node]
            return path[::-1]
    
        


        neighbors=get_neighbors(maze,pop_node[1])
            

        for n in neighbors :
                if n not in closed_set :
                    i-=1
                    fringe.put((i,n))
                    closed_set.add(n)
                    parent_dict[n]=pop_node[1]
    

        


        


    
    
    
    
    
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

    fringe=PriorityQueue()
 


    fringe.put((0,start))

    cost_dict={start:0}

    parent_dict={start:None}

    while not fringe.empty():
        current_cost,pop_node=fringe.get()

        if pop_node==goal:
            current_node=pop_node
            while current_node is not None:
                path.append(current_node)
                current_node=parent_dict[current_node]
            return path[::-1]
        

        # Optimization: If we found a cheaper way to this node previously, skip this stale entry
        if current_cost > cost_dict[pop_node]:
            continue
        

 
        neighbor=get_neighbors(maze,pop_node)

        for n in neighbor:

            cost_edge=get_edge_cost(costs=costs,node=n,neighbor=pop_node)
            cost_n=current_cost + cost_edge
           
            if n not in cost_dict or cost_n<cost_dict[n] :
                
                cost_dict[n]=cost_n
                fringe.put((cost_n,n))
                parent_dict[n]=pop_node





    
    
    
    
    
    return path
################################################################################################################################# 
#Any oher functions you may want to define