'''def find_uniq(arr):
    seen = {}
    common = None
    for string in arr:
        key = frozenset(set(string.lower()).difference(' '))
        if key in seen:
            common = key
        if common is not None:
            if key != common:
                return string
            if len(seen) > 1:
                del seen[common]
                return next(iter(seen.values()))
        seen[key] = string

print(find_uniq([ 'Aa', 'aaa', 'aaaaa', 'aaaAAa',  'Aaaa', 'AaAaAa', 'sd', 'a']))'''

graph = {}
graph['start'] = {}
graph['start']['a'] = 5
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['c'] = 4
graph['a']['d'] = 2
graph['b'] = {}
graph['b']['a'] = 8
graph['b']['d'] = 7
graph['c'] = {}
graph['c']['d'] = 6
graph['c']['fin'] = 3
graph['d'] = {}
graph['d']['fin'] = 1
graph['fin'] = {}
infinity = float('inf')
costs = {}
costs['a'] = 5
costs['b'] = 2
costs['c'] = infinity
costs['d'] = infinity
costs['fin'] = infinity

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['c'] = None
parents['d'] = None
parents['fin'] = None

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
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

print('Кратчайший путь от начала до конца -', costs['fin'])

def get_print():
    for i in costs.keys():
        if costs.get(i) != None and i != 'fin':
            y = costs.get(i)
            print('От начала до', i, y)
get_print()
