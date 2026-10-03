import heapq
import math

CSE = {"CSE Laboratory", "CSE_AKC Seminar Hall", "CSE_Reflxon Room"}
TOWER = {"Tower 2 Front Entry", "Tower 2 Rear Entry"}

def heuristic(campus, current, goal):
    x1, y1 = campus.get_coordinates(current)
    x2, y2 = campus.get_coordinates(goal)
    return math.sqrt((x1-x2)**2 + (y1-y2)**2) * 50

def valid_state(current, neighbor, mode):
    # normal -> cse is allowed only through Lift Area
    if mode == "normal":
        if neighbor in CSE:
            return "cse" if current == "Lift Area" else None
        return "normal"
    # inside CSE: only CSE places or Lift Area can be visited
    if mode == "cse":
        if neighbor in CSE:
            return "cse"
        if neighbor == "Lift Area":
            return "exit"
        return None
    # after returning to Lift from CSE, must use a Tower 2 entry to leave
    if mode == "exit":
        if neighbor in TOWER:
            return "normal"
        return None
    return None

def path_cost(campus, path):
    return sum(campus.get_cost(path[i], path[i+1]) for i in range(len(path)-1))

def make_path(parent, state):
    path=[]
    while state is not None:
        path.append(state[0])
        state=parent[state]
    return path[::-1]

def greedy_best_first(campus, start, goal):
    start_state=(start,"cse" if start in CSE else "normal")
    q=[]; count=0
    heapq.heappush(q,(heuristic(campus,start,goal),count,start_state))
    parent={start_state:None}; visited=set(); explored=0
    while q:
        _,_,state=heapq.heappop(q)
        if state in visited: continue
        visited.add(state); explored+=1
        current,mode=state
        if current==goal:
            path=make_path(parent,state)
            return path,path_cost(campus,path),explored
        for neighbor,_ in campus.get_neighbors(current):
            new_mode=valid_state(current,neighbor,mode)
            ns=(neighbor,new_mode) if new_mode else None
            if ns and ns not in visited and ns not in parent:
                parent[ns]=state; count+=1
                heapq.heappush(q,(heuristic(campus,neighbor,goal),count,ns))
    return [],None,explored

def a_star(campus,start,goal):
    start_state=(start,"cse" if start in CSE else "normal")
    q=[]; count=0
    heapq.heappush(q,(heuristic(campus,start,goal),count,start_state))
    parent={start_state:None}; cost={start_state:0}; visited=set(); explored=0
    while q:
        _,_,state=heapq.heappop(q)
        if state in visited: continue
        visited.add(state); explored+=1
        current,mode=state
        if current==goal:
            path=make_path(parent,state)
            return path,path_cost(campus,path),explored
        for neighbor,edge in campus.get_neighbors(current):
            new_mode=valid_state(current,neighbor,mode)
            if new_mode is None: continue
            ns=(neighbor,new_mode)
            new_cost=cost[state]+edge
            if ns not in cost or new_cost<cost[ns]:
                cost[ns]=new_cost; parent[ns]=state; count+=1
                f=new_cost+heuristic(campus,neighbor,goal)
                heapq.heappush(q,(f,count,ns))
    return [],None,explored
