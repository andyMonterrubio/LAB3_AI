#!/usr/bin/python
# -*- coding: utf-8 -*-

from search import printSolution

if __name__ == "__main__":
    height = int(input()) #maximum height of stack
    start = raw_input() #initial location of the containers
    goal = raw_input() #goal state

    printSolution('dfs', height, start, goal)
