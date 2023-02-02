import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets as qtw


class BFS:
    array_gui = []
    def solve(start, goal):
        BFS.array_gui.clear()
        begin = time.time()
        depth = start.depth
        frontier_s = set()
        frontier_q = []
        explored = set()
        parent_map = {}
        # use a set for frontier for O(1) lookup and a queue for FIFO
        frontier_s.add(start)
        frontier_q.append(start)
        while frontier_s:
            # remove the first state in the queue
            s = frontier_q.pop(0)
            frontier_s.remove(s)
            v = s.value
            # add the state to explored
            explored.add(s)
            # compare the depth of the state with the current max depth
            depth = max(depth, s.depth) 
            # check if the state is the goal           
            if s == goal:
                print("Goal achieved")
                print(v)
                break
            # get the children of the state
            array = s.children()            
            for child in array:
                if child not in explored and child not in frontier_s:
                    # add the child to the frontier and the parent map
                    frontier_s.add(child)
                    frontier_q.append(child)
                    parent_map[child] = s
                    parent_map[child] = s
        end = time.time()
        print("Depth ", depth)
        print("Expanded ", len(explored))
        print(f"Total runtime of the BFS is {end - begin}")
        if s != goal:
            print("Goal not found")
            return
        BFS.path(parent_map, start, s)

    def path(parent_map, start, goal):
        # get the path from the parent map 
        path_a = []
        parent = goal
        cost = 0
        # while loop terminates when the parent is the start state
        while parent != start:
            BFS.array_gui.append(parent.value)
            path_a.append(parent.value)
            parent = parent_map.get(parent)
        print("Cost", goal.cost)
        print("Cost:", len(path_a))
        # reverse the path to get the correct order
        path_a.reverse()
        # BFS array is used to display the path in the GUI
        BFS.array_gui.reverse()
        print(path_a)





