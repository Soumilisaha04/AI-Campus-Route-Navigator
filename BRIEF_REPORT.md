# Brief Report - "AI Campus Route Navigator"

## 1. Objective :-

The objective was to convert the given Calcutta University Technology Campus map into a weighted graph and compare Greedy Best-First Search with A* Search.

## 2. Campus Graph :-

I used only the locations shown in the assignment map. Approximate walking costs are stored in `campus.json`.The graph is kept separate from the
search algorithm .

## 3. Heuristic :-

I used simple map-based coordinates stored in `campus.json`. The heuristic estimates the remaining distance using the coordinates.
Greedy Best-First uses `f(n) = h(n)`. A* uses `f(n) = g(n) + h(n)`.

## 4. CSE Routing Rule :-

The special CSE rule was implemented. The CSE locations are CSE Laboratory, CSE_AKC Seminar Hall and CSE_Reflxon Room. Entry is through Tower 2 Front/Rear Entry -> Lift Area -> CSE. Inside the CSE zone only CSE locations can be visited until returning to Lift Area. Exit is through Lift Area -> Tower 2 Front/Rear Entry -> other locations.

## 5. Experimental Results :-

| Problem | Agent | Source | Destination | Route | Cost | Nodes | Time |
|---:|---|---|---|---|---:|---:|---:|
| 1 | PATHFINDER | Reception of Calcutta University | Library | Reception of Calcutta University → Power Area → Canteen of Technology Campus → Parking Area → Tower 2 Front Entry → Lift Area → Library | 685 | 9 | 4.5e-05 |
| 1 | ORBIT | Reception of Calcutta University | Library | Reception of Calcutta University → Power Area → Canteen of Technology Campus → Parking Area → Tower 2 Front Entry → Lift Area → Library | 685 | 10 | 3.3e-05 |
| 2 | PATHFINDER | Canteen of Technology Campus | New Building 2 (Workshop Building) | Canteen of Technology Campus → Garden of Technology Campus → New Building 2 (Workshop Building) | 300 | 3 | 1.1e-05 |
| 2 | ORBIT | Canteen of Technology Campus | New Building 2 (Workshop Building) | Canteen of Technology Campus → Garden of Technology Campus → New Building 2 (Workshop Building) | 300 | 3 | 9e-06 |
| 3 | PATHFINDER | Entry Gate 1 (G1) | CSE Laboratory | Entry Gate 1 (G1) → Reception of Calcutta University → Power Area → Canteen of Technology Campus → Parking Area → Tower 2 Front Entry → Lift Area → CSE Laboratory | 850 | 9 | 1.9e-05 |
| 3 | ORBIT | Entry Gate 1 (G1) | CSE Laboratory | Entry Gate 1 (G1) → Reception of Calcutta University → Power Area → Canteen of Technology Campus → Parking Area → Tower 2 Front Entry → Lift Area → CSE Laboratory | 850 | 11 | 2.2e-05 |
| 4 | PATHFINDER | Auditorium Hall | CSE_AKC Seminar Hall | Auditorium Hall → Garden of Technology Campus → Canteen of Technology Campus → Parking Area → Tower 2 Front Entry → Lift Area → CSE_AKC Seminar Hall | 645 | 7 | 1.5e-05 |
| 4 | ORBIT | Auditorium Hall | CSE_AKC Seminar Hall | Auditorium Hall → Garden of Technology Campus → Canteen of Technology Campus → Parking Area → Tower 2 Front Entry → Lift Area → CSE_AKC Seminar Hall | 645 | 11 | 2.3e-05 |
| 5 | PATHFINDER | Library | Canteen of Technology Campus | Library → Lift Area → Tower 2 Front Entry → Parking Area → Canteen of Technology Campus | 375 | 7 | 1.5e-05 |
| 5 | ORBIT | Library | Canteen of Technology Campus | Library → Lift Area → Tower 2 Front Entry → Parking Area → Canteen of Technology Campus | 375 | 10 | 1.8e-05 |
| 6 | PATHFINDER | Power Area | New Building 1 (Science Building) | Power Area → CNM Centre (Nano Technology) → Auditorium Hall → New Building 2 (Workshop Building) → New Building 1 (Science Building) | 610 | 5 | 1e-05 |
| 6 | ORBIT | Power Area | New Building 1 (Science Building) | Power Area → Canteen of Technology Campus → Garden of Technology Campus → New Building 1 (Science Building) | 500 | 6 | 1.3e-05 |

## 6. Observations :-

1. Greedy Best-First mainly uses the estimated remaining distance, so it can select a location that looks close to the destination without considering all the distance already travelled.
2. A* uses both the travelled cost and estimated remaining cost.
3. In the tested problems, most routes were the same, but the Power Area to New Building 1 problem produced different costs.
4. The same heuristic is used for both agents so the comparison is fair.
5. The CSE restriction removes some otherwise possible moves, so the search checks the routing rule while expanding neighbours.

## 7. Conclusion :-

This assignment helped me understand how a real campus map can be
represented as a graph and how different search strategies behave on the same graph. Greedy Best-First is mainly guided by the destination estimate, while A* also considers the cost already travelled.
