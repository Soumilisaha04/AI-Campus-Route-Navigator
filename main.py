from campus_map import CampusMap
from agents import Pathfinder, Orbit
from experiment import run_experiment, save_results
import time

def main():
    campus=CampusMap()
    pathfinder=Pathfinder()
    orbit=Orbit()

    print("AI CAMPUS ROUTE NAVIGATOR")
    print("-------------------------")
    print("1. Run experiments")
    print("2. Enter your own route")
    choice=input("Enter choice (1/2): ").strip()

    if choice=="2":
        print("\nAvailable locations:")
        for location in campus.nodes:
            print("-",location)
        start=input("\nEnter starting location exactly as shown: ").strip()
        destination=input("Enter destination exactly as shown: ").strip()
        if start not in campus.nodes or destination not in campus.nodes:
            print("Location not found. Check spelling.")
            return
        for agent in [pathfinder,orbit]:
            begin=time.perf_counter()
            path,cost,nodes=agent.find_route(campus,start,destination)
            print("\n"+agent.name)
            print("Route:"," -> ".join(path) if path else "No route")
            print("Cost:",cost,"m" if cost is not None else "")
            print("Nodes explored:",nodes)
            print("Time:",round(time.perf_counter()-begin,6),"s")
    else:
        problems=[
            (1,"Reception of Calcutta University","Library"),
            (2,"Canteen of Technology Campus","New Building 2 (Workshop Building)"),
            (3,"Entry Gate 1 (G1)","CSE Laboratory"),
            (4,"Auditorium Hall","CSE_AKC Seminar Hall"),
            (5,"Library","Canteen of Technology Campus"),
            (6,"Power Area","New Building 1 (Science Building)")
        ]
        rows=run_experiment(pathfinder,orbit,campus,problems)
        print("\nEXPERIMENT RESULTS")
        for r in rows:
            print(r["problem"],r["agent"],"| Cost:",r["cost"],"| Nodes:",r["nodes_explored"],"| Time:",r["time_seconds"])
        save_results(rows,"results.csv")
        print("\nResults saved in results.csv")

if __name__=="__main__":
    main()
