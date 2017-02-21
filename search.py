#!/usr/bin/python
# -*- coding: utf-8 -*-

class Node(object):
    def __init__(self):
        self.problem = None #current node (containers) list
        self.parent = None
        self.action = None
        self.cost = None
        self.heuristic = None

def childNode(problem, parent, action, cost, heuristic):
    node = Node()
    node.action = action
    node.parent = parent
    node.problem = problem
    node.cost = cost
    node.heuristic = heuristic
    return node
    
def checkGoal(node,goal):
    count = 0
    for pair in goal:
        if pair != 'X':
            if node.problem[count] != pair:
                return False
        count = count+1
    return True      
    

# create new state based on parent's state and proposed move
def createList(move, parentList):
    origin = move[0]
    end = move[1]
    newList = []
    for letter in parentList: #copy parent list into newList
        newList.append(letter)
        
    potentialMove = newList.pop(origin).split(',') #get stack where the box to move is
    boxToMove = potentialMove.pop() #get box
    if len(potentialMove) <= 1:
        newList.insert(origin,''.join(potentialMove)) #return what was not taken from the stack
    else:
        newList.insert(origin,','.join(potentialMove))
        
    endList = newList.pop(end).split(',')#get the stack where the box will be moved
    if '' in endList:
        endList.insert(0,boxToMove)
        endList.pop()#add the box to the stack
    else:
        endList.append(boxToMove)#add the box to the stack

    newList.insert(end,','.join(endList)) #return the stack to the list
    return newList
    
    
def lookforNode(n, visitedStack, hasHeuristic=False):
    for node in visitedStack:
        if node.problem == n.problem:
            # replace if there's a better heuristic for the same state
            if hasHeuristic and n.heuristic < node.heuristic:
                visitedStack.remove(node)
                return False
            return True
    return False

# generic search algorithm
# algorithmName supports bfs, dfs and a*
def search(algorithmName, start, goal, height, heuristic=(lambda node, goal : 0)):
    stateQueue = [] #nodes to be visited
    visitedStack = [] #nodes that were already visited

    root = childNode(start, None, None, 0, None)
    stateQueue.append(root)

    goalNode = childNode(goal, None, None, 0, 0)

    while stateQueue:
        lengthStack = []
        moveStack = [] #(start,finish)

        if algorithmName == 'dfs':
            currentNode = stateQueue.pop()
        else:
            currentNode = stateQueue.pop(0)

        #add to the visited states
        #print 'popped node:',currentNode.problem
        visitedStack.append(currentNode)

        #check if the current state is the goal
        if checkGoal(currentNode,goal):
            return currentNode
        else:
            #get the length for each container
            for pair in currentNode.problem:
                if len(pair) > 1:
                    lengthStack.append(len(pair.split(',')))
                else:
                    lengthStack.append(len(pair))
                    
            #print 'lengthStack:',lengthStack
            xCount = 0
            for length in lengthStack:
                if length > 0:
                    x = xCount
                    xCount = xCount+1
                    for res in range(0, len(lengthStack)):
                        if res != x:
                            if lengthStack[res] < height:
                                moveStack.append((x, res))
                else:
                    xCount = xCount+1
    
            #print 'moveStack:',moveStack                    
            #add nodes to the queue
            for move in moveStack:
                # print 'currentNode problem:', currentNode.problem
                nodeCost = currentNode.cost + abs(move[1]-move[0]) + 1
                newNode = childNode(createList(move, currentNode.problem), currentNode,
                          str(move[0])+','+str(move[1]), nodeCost,
                          heuristic(currentNode, goalNode) + nodeCost)
                #print 'new:',newNode.problem
                if not lookforNode(newNode, visitedStack, algorithmName == 'a*'):
                    stateQueue.append(newNode)
                    
            if algorithmName == 'a*':
                stateQueue.sort(key = lambda node : node.heuristic)

    return None

# read raw input, run search and print solution
def printSolution(algorithmName, height, start, goal, heuristic=None):
    start = start.replace(" ", "")
    start = start.replace("(", "")
    start = start.replace(")", "")
    startContainers = start.split(';')

    goal = goal.replace(" ", "")
    goal = goal.replace("(", "")
    goal = goal.replace(")", "")
    goalContainers = goal.split(';')
    
    if heuristic:
        solution = search(algorithmName, startContainers, goalContainers, height, heuristic)
    else:
        solution = search(algorithmName, startContainers, goalContainers, height)

    if solution:
        # get solution node and trace back the steps to get there
        solutionSteps = []
        node = solution
        while node.action:
            solutionSteps.append("(" + node.action + ")")
            node = node.parent
        solutionSteps.reverse()
        print solution.cost
        print "; ".join(solutionSteps)
    else:
        print 'No solution found'
