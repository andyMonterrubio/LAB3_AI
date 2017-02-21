#!/usr/bin/python
# -*- coding: utf-8 -*-

from search import printSolution

def bad_heuristic(node, goal):
    for currentContainer in node.problem:
        boxes = currentContainer.split(',')

if __name__ == "__main__":
    height = int(input()) #maximum height of stack
    start = raw_input() #initial location of the containers
    goal = raw_input() #goal state

    printSolution('a*', height, start, goal, bad_heuristic)
