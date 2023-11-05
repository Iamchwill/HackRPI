import osmnx


def fastest_route(location, toilet):
    G = osmnx.graph_from_point(location, network_type="walk")
    G = osmnx.add_edge_speeds(G)
    G = osmnx.add_edge_travel_times(G)
    return find_shortest(G, location, toilet)

def find_shortest(G, pt1, pt2):
    orig = osmnx.nearest_nodes(G, pt1[0], pt1[1])
    dest = osmnx.nearest_nodes(G, pt2[0], pt2[1])
    print(orig)
    print(dest)
    route = osmnx.shortest_path(G, orig, dest, weight="travel_time")
    print(route)
    edge_lengths = osmnx.utils_graph.route_to_gdf(G, route, 'length')
    s = sum(edge_lengths)
    return route, s