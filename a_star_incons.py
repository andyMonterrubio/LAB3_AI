#!/usr/bin/python
# -*- coding: utf-8 -*-

from search import printSolution


def bad_heuristic(node, goal):
    a = {}
    for i in range(0, len(goal.problem)):
        boxes = node.problem[i].split(',')
        for box in boxes:
            if box != '' and box != 'X':
                a[box] = i
    
    for i in range(0, len(node.problem)):
            boxes = node.problem[i].split(',')
            for box in boxes:
                if box != '':
                    a[box] = abs(i - a[box]) #calculate h
    
    return sum(a.values())


if __name__ == "__main__":
    height = int(input()) #maximum height of stack
    start = raw_input() #initial location of the containers
    goal = raw_input() #goal state

    printSolution('a*', height, start, goal, bad_heuristic)
