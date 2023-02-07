from typing import Dict, List

# Function to build the graph from the given information
def buildGraph(flowRates: Dict[str, int], tunnels: Dict[str, List[str]]) -> Dict[str, List[str]]:
    graph = {}
    for valve, flowRate in flowRates.items():
        graph[valve] = []
    for valve, neighbors in tunnels.items():
        for neighbor in neighbors:
            graph[valve].append(neighbor)
    return graph

# Function to find the maximum flow rate through the graph using dynamic programming
def maxFlowRate(graph: Dict[str, List[str]], flowRates: Dict[str, int], startNode: str, timeLimit: int) -> int:
    # Initialize a table to store the maximum flow rate for each time spent
    table = [[0 for _ in range(timeLimit + 1)] for _ in range(len(graph))]

    # For each node in the graph
    for node in range(len(graph)):
        # For each time spent
        for timeSpent in range(timeLimit + 1):
            # If we have spent more time than the time limit, break the inner loop
            if timeSpent > timeLimit:
                break
            # If we have spent one minute to reach this node, set the flow rate to the node's flow rate
            elif timeSpent == 1:
                table[node][timeSpent] = flowRates[startNode]
            # Otherwise, set the flow rate to the maximum flow rate of the neighbors
            else:
                maxFlow = 0
                for neighbor in graph[startNode]:
                    maxFlow = max(maxFlow, table[neighbor][timeSpent - 1])
                table[node][timeSpent] = maxFlow

    # Return the maximum flow rate in the table
    return max(table[node])

# Example usage
flowRates = {
    "AA": 0,
    "BB": 13,
    "CC": 2,
    "DD": 20,
    "EE": 3,
    "FF": 0,
    "GG": 0,
    "HH": 22,
    "II": 0,
    "JJ": 21
}
tunnels = {
    "AA": ["DD", "II", "BB"],
    "BB": ["CC", "AA"],
    "CC": ["DD", "BB"],
    "DD": ["CC", "AA", "EE"],
    "EE": ["FF", "DD"],
    "FF": ["EE", "GG"],
    "GG": ["FF", "HH"],
    "HH": ["GG"],
    "II": ["AA", "JJ"],
    "JJ": ["II"]
}
graph = buildGraph(flowRates, tunnels)
print(maxFlowRate(graph, flowRates, "AA", 30))  # Should print 54
