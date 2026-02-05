def dijkstry():
    graph = dict()
    graph["ty"] = ["alicja", "bartek", "cecylia"]
    graph["start"] = dict()
    graph["start"]["a"] = 6
    graph["start"]["b"] = 2
    graph["a"] = dict()
    graph["a"]["meta"] = 1
    graph["b"] = dict()
    graph["b"]["a"] = 3
    graph["b"]["meta"] = 5
    graph["meta"] = dict()
    infinity = float("inf")
    costs = dict()
    costs["a"] = 6
    costs["b"] = 2
    costs["fin"] = infinity
    parents = dict()
    parents["a"] = "start"
    parents["b"] = "start"
    parents["meta"] = None
    processed = []

    def find_lowest_cost_node(costs):
        lowest_cost = float("inf")
        lowest_cost_node = None
        for node in costs:
            cost = costs[node]
            if cost < lowest_cost and node not in processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

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


"""
Określ wagę najkrótszej drogi od linii startu do mety na każdym z poniższych grafów.
"""

# 'A' Odpowiedź: Start -> Góra -> Dół -> Meta = 5 + 2 + 1 = 8

# 'B' Odpowiedź: Start -> Góra -> Góra -> Góra = 10 + 20 + 30 = 60

# 'C' Odpowiedź: Nie da się obliczyć drogi z powodu ujemnej wagi

# Jeśli graf zawiera wagi ujemne, należy posłużyć się algorytmem Bellmana-Forda.
