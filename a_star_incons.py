#!/usr/bin/python
# -*- coding: utf-8 -*-

#heuristic: manhattan distance

from search import printSolution

def bad_heuristic(node, goal):
    distances = {}
    for i in range(0, len(goal.problem)):
        boxes = goal.problem[i].split(',')
        for j in range(0, len(boxes)):
            if boxes[j] != '' and boxes[j] != 'X':
                distances[boxes[j]] = (i, j)

    for i in range(0, len(node.problem)):
        boxes = node.problem[i].split(',')
        for j in range(0, len(boxes)):
            if boxes[j] != '':
                try:
                    distances[boxes[j]] = abs(i - distances[boxes[j]][0]) + abs(i - distances[boxes[j]][1]) #calculate h
                except:
                    distances[boxes[j]] = 0
    
    return sum(distances.values())


if __name__ == "__main__":
    height = int(input()) #maximum height of stack
    start = raw_input() #initial location of the containers
    goal = raw_input() #goal state

    printSolution('a*', height, start, goal, bad_heuristic)