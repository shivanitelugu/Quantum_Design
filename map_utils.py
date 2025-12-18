import folium

def plot_route(coords, path, filename="shortest_route_map.html"):
    # Center map at first location
    start_coord = coords[path[0]]
    m = folium.Map(location=start_coord, zoom_start=7)

    # Add markers
    for place, (lat, lon) in coords.items():
        folium.Marker(
            location=[lat, lon],
            popup=place,
            icon=folium.Icon(color="blue")
        ).add_to(m)

    # Draw route
    route_coords = [coords[loc] for loc in path]
    folium.PolyLine(
        locations=route_coords,
        color="red",
        weight=5,
        tooltip="Shortest Route"
    ).add_to(m)

    # Save map
    m.save(filename)
    print(f"\nMap saved as {filename}")
