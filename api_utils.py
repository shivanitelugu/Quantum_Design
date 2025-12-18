import googlemaps
import networkx as nx
import time

# 🔑 PUT YOUR API KEY HERE
gmaps = googlemaps.Client(key="ENTER-THE_API_KEY")

def get_coordinates(place):
    time.sleep(0.2)
    result = gmaps.geocode(place)
    if not result:
        raise ValueError(f"Could not geocode {place}")
    loc = result[0]["geometry"]["location"]
    return (loc["lat"], loc["lng"])

def get_road_distance(origin, destination):
    directions = gmaps.directions(
        origin,
        destination,
        mode="driving"
    )
    if not directions:
        raise ValueError("No route found")

    return directions[0]["legs"][0]["distance"]["value"] / 1000  # km

def create_graph_from_locations(locations):
    G = nx.Graph()
    coords = {}

    for loc in locations:
        coords[loc] = get_coordinates(loc)
        G.add_node(loc)

    for i in range(len(locations)):
        for j in range(i + 1, len(locations)):
            dist = get_road_distance(locations[i], locations[j])
            G.add_edge(locations[i], locations[j], weight=dist)

    return G, coords

