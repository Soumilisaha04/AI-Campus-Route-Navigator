import csv
import time

def run_experiment(pathfinder, orbit, campus, problems):
    rows=[]
    for number,start,destination in problems:
        for agent in [pathfinder,orbit]:
            begin=time.perf_counter()
            path,cost,nodes=agent.find_route(campus,start,destination)
            elapsed=time.perf_counter()-begin
            rows.append({
                "problem":number,
                "agent":agent.name,
                "source":start,
                "destination":destination,
                "path":" -> ".join(path) if path else "No route",
                "cost":cost if cost is not None else "",
                "nodes_explored":nodes,
                "time_seconds":round(elapsed,6)
            })
    return rows

def save_results(rows,filename="results.csv"):
    fields=["problem","agent","source","destination","path","cost","nodes_explored","time_seconds"]
    with open(filename,"w",newline="") as file:
        writer=csv.DictWriter(file,fieldnames=fields)
        writer.writeheader(); writer.writerows(rows)
