from geopy.geocoders import Nominatim
import networkx as nx
import math
import time

geolocator = Nominatim(user_agent="route_project")

def get_coordinates(place):
    time.sleep(1)  # avoid API blocking
    location = geolocator.geocode(place)
    if location is None:
        raise ValueError(f"Could not find location: {place}")
    return (location.latitude, location.longitude)

def haversine(c1, c2):
    lat1, lon1 = c1
    lat2, lon2 = c2
    R = 6371  # km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat/2)**2 +
         math.cos(math.radians(lat1)) *
         math.cos(math.radians(lat2)) *
         math.sin(dlon/2)**2)
    return 2 * R * math.asin(math.sqrt(a))

def create_graph_from_locations(locations):
    G = nx.Graph()
    coords = {}

    for loc in locations:
        coords[loc] = get_coordinates(loc)
        G.add_node(loc)

    for i in range(len(locations)):
        for j in range(i + 1, len(locations)):
            d = haversine(coords[locations[i]], coords[locations[j]])
            G.add_edge(locations[i], locations[j], weight=d)

    return G, coords
