from api_utils import create_graph_from_locations
from classical import dfs_paths, shortest_path_from_dfs
from map_utils import generate_google_maps_route

API_KEY = "enter_api_here"

def main():
    user_input = input(
        "Enter delivery locations separated by comma:\n"
    )
    locations = [l.strip() for l in user_input.split(",")]

    if len(locations) < 2:
        print("Need at least two locations")
        return

    print("\nFetching coordinates and building graph...")
    G, coords = create_graph_from_locations(locations)

    start = locations[0]
    end = locations[-1]

    print("\nRunning DFS...")
    paths = dfs_paths(G, start, end)

    best_path, best_dist = shortest_path_from_dfs(G, paths)

    print("\n✅ SHORTEST DELIVERY PATH (ROAD-BASED):")
    print(" → ".join(best_path))
    print(f"Distance: {best_dist:.2f} km")

    print("\nOpening Google Maps with road route...")
    generate_google_maps_route(best_path, API_KEY)

if __name__ == "__main__":
    main()
