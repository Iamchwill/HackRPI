import osmnx

def fastest_route(location, toilet):
    G = osmnx.graph_from_place(location, network_type="walk")
    G = osmnx.add_edge_speeds(G)
    G = osmnx.add_edge_travel_times(G)
    find_shortest(G, location, toilet)

def find_shortest(G, pt1, pt2):
    orig = osmnx.nearest_nodes(G, pt1[0], pt1[1])
    dest = osmnx.nearest_nodes(G, pt2[0], pt2[1])
    route = osmnx.shortest_path(G, orig, dest, weight="travel_time")
    return route

def route_length(r):
    edge_lengths = osmnx.utils_graph.get_route_edge_attributes(G, r, 'length')
    return sum(edge_lengths)