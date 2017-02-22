from search import printSolution

if __name__ == "__main__":
    height = int(input()) #maximum height of stack
    start = raw_input() #initial location of the containers
    goal = raw_input() #goal state

    printSolution('bfs', height, start, goal)