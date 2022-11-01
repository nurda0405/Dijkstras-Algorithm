#graph
graph = {}
graph["start"] = {}
graph["start"]["plastinka"] = 5
graph["start"]["poster"] = 0

graph["poster"] = {}
graph["poster"]["gitara"] = 30
graph["poster"]["baraban"] = 35

graph["plastinka"] = {}
graph["plastinka"]["gitara"] = 15
graph["plastinka"]["baraban"] = 20

graph["gitara"] = {}
graph["gitara"]["piano"] = 20

graph["baraban"] = {}
graph["baraban"]["piano"] = 10

graph["piano"] = {}

#costs
costs = {}
costs["plastinka"] = 5
costs["poster"] = 0
costs["gitara"] = float("inf")
costs["baraban"] = float("inf")
costs["piano"] = float("inf")

#parents
parents = {}
parents["plastinka"] = "start"
parents["poster"] = "start"
parents["gitara"] = None
parents["baraban"] = None
parents["piano"] = None

processed = []

#function
def find_lowest_cost_node(costs):
  lowest_cost = float("inf")
  lowest_cost_node = None
  for node in costs:
    cost=costs[node]
    if cost< lowest_cost and node not in processed:
      lowest_cost = cost
      lowest_cost_node = node
  return lowest_cost_node 
  
#algorithm
node = find_lowest_cost_node(costs)
while node is not None:
  cost = costs[node]
  neighbors = graph[node]
  for n in neighbors.keys():
    new_cost = cost + neighbors[n]
    if costs[n] > new_cost:
      costs[n] = new_cost
      parents[n] = node
  processed.append(node)
  node = find_lowest_cost_node(costs)

print(costs)



  