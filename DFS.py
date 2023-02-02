import time

from PyQt5 import QtCore, QtGui, QtWidgets
from main import State

class DFS:
    frontier_s = set()
    frontier_q = []
    array_gui = []

    def solve(start, goal):
        DFS.array_gui.clear()
        begin = time.time()
        frontier_s = set()
        frontier_q = []
        depth = start.depth
        explored = set()
        parent_map = {}
        # use a set for frontier for O(1) lookup and a queue for FIFO
        frontier_s.add(start)
        frontier_q.append(start)
        while frontier_s:
            # remove x from frontier
            s = frontier_q.pop()
            frontier_s.remove(s)
            # add x to explored
            explored.add(s)
            # compare the depth of the state with the current max depth
            depth = max(depth, s.depth)
            if s == goal:
                print("Goal achieved")
                break
            # get the children of the state
            array = s.children()
            array.reverse()
            for child in array:
                if child not in explored and child not in frontier_s:
                    # add the child to the frontier and the parent map
                    frontier_s.add(child)
                    frontier_q.append(child)
                    parent_map[child]=s
        end = time.time()
        print("Depth ", depth)
        print("Expanded ", len(explored))
        print(f"Total runtime of the DFS is {end - begin}")
        if s != goal:
            print("Goal not found")
            return
        DFS.path(parent_map, start, s)

    def path(parent_map, start, goal):
        # get the path from the parent map
        path_a = []
        parent = goal
        cost = 0
        # while loop terminates when the parent is the start state
        while parent != start:
            path_a.append(parent.action)
            DFS.array_gui.append(parent.value)
            parent = parent_map.get(parent)
        print("Cost", goal.cost)
        # reverse the path to get the correct order
        path_a.reverse()
        DFS.array_gui.reverse()
        print(path_a)