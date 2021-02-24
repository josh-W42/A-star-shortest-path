import heapq
import math

def shortest_path(M, start, goal):
    print("shortest path called")
    
#   Dictionary to keep track of the node before a current one along the shortest path
    node_before =  dict()

    start_point = M.intersections[start]
    goal_point = M.intersections[goal]
    
#   We need to keep track of all the nodes that are the frontier
    explored = {start}
    
#   We need a dictionary of costs from the starting point to the end.
    g_cost = dict()
    g_cost[start] = 0
    
#   A dictionary for all values of the function f = g + h that pair with a point
    f_total = dict()
    f_total[distance(start_point, goal_point)] = start
    
#   This priority queue will always choose the minimum f_value
#   so we dont need to check in the while loop

    frontier_heap = list(f_total.keys())
    heapq.heapify(frontier_heap)
    
    
    while(len(frontier_heap) > 0):
        
        current_node = f_total[heapq.heappop(frontier_heap)]
        
        if current_node == goal:
            return construct_path(node_before, current_node)
        else:
#           Search for all the neighboors of the current node
            for point in M.roads[current_node]:
                
                # The g value of a node is the sum of the shortest path up to the current
                # point and edge distance between itself and the current Node.
                neighboor_g_value = g_cost[current_node] + distance(M.intersections[current_node], M.intersections[point])
                
                # If not in our costs dictionary, we say that we're not connected to it.
                if g_cost.get(point) is None:
                    g_cost[point] = math.inf
                
#               if the neighboor g_cost is lower then we found point with the minimized cost.
                if neighboor_g_value < g_cost[point]:
                    
#                   Then we store the point's information into respective dictionaries.
                    node_before[point] = current_node
                    g_cost[point] = neighboor_g_value
                    f_value = g_cost[point] + distance(M.intersections[point], goal_point)
                    f_total[f_value] = point
                   
                    heapq.heappush(frontier_heap, f_value)
      

    # Here is an idea, don't add everything to the output make a make shift path then connect the dots.
    return -1 

def distance(p1, p2):
    '''
    Helper function that will finds the distance between two sets of x, y cordinates.
    Can be used to find the heuristic, h.
    
    Args:
        p1(list), p2(list): two points [x,y] in a list.
    Returns:
        The distance between them.
    '''
    return math.sqrt((p2[1] - p1[1])**2 + (p2[0] - p1[0])**2)
    
    
def construct_path(dictionary, last_node):
    '''
    Helper function that creates a list with shortest path starting from the goal.
    Must be reversed at the end.
    '''
    path = [last_node]
    
    while last_node in dictionary.keys():
        last_node = dictionary[last_node]
        path = [last_node] + path
    return path
    
