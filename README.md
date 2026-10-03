# AI Campus Route Navigator :-

This is my AI/ML Laboratory Assignment. The task is to make a small campus navigation system using the CU Technology Campus map given in the assignment. I converted the locations from the map into a weighted graph and used two search methods:
- PATHFINDER - Greedy Best-First Search
- ORBIT - A* Search

## Files :-

- `campus.json` - campus locations, connections and approximate distances
- `campus_map.py` - loads the graph from JSON
- `search.py` - Greedy Best-First Search and A*
- `agents.py` - PATHFINDER and ORBIT
- `experiment.py` - runs experiments and saves results
- `main.py` - runs the program
- `results.csv` - experimental results
- `BRIEF_REPORT.md` - short report

## Heuristic :-

I used approximate map positions stored in `campus.json`. The heuristic calculates an estimated distance between two locations.
Greedy Best-First uses:
`f(n) = h(n)`

A* uses:
`f(n) = g(n) + h(n)`

## CSE Rule :-
The CSE locations are CSE Laboratory, CSE_AKC Seminar Hall and CSE_Reflxon Room.
To enter CSE, the route must go through Tower 2 Front/Rear Entry and Lift Area. While inside CSE, only CSE locations can be visited until returning to Lift Area. To exit, the route goes from Lift Area to a Tower 2 entry and then to other campus locations.

## Hoe to Run :-
Open this folder in VS Code and run:
```bash
python main.py
```
Choose 1 for the given experiments or 2 to enter your own source and destination.

## Conclusion :-
Greedy Best-First mainly looks at the estimated distance to the destination. A* also considers the distance already travelled, so the two agents can choose different routes.
