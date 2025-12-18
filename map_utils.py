import webbrowser

def generate_google_maps_route(path, api_key, filename="google_route.html"):
    origin = path[0]
    destination = path[-1]
    waypoints = path[1:-1]

    waypoints_str = "|".join(waypoints)

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Google Maps Route</title>
        <script src="https://maps.googleapis.com/maps/api/js?key={api_key}"></script>
        <script>
            function initMap() {{
                const map = new google.maps.Map(document.getElementById("map"), {{
                    zoom: 7,
                    center: {{ lat: 12.9716, lng: 77.5946 }}
                }});

                const directionsService = new google.maps.DirectionsService();
                const directionsRenderer = new google.maps.DirectionsRenderer();
                directionsRenderer.setMap(map);

                directionsService.route({{
                    origin: "{origin}",
                    destination: "{destination}",
                    waypoints: [{",".join([f'{{location: "{w}"}}' for w in waypoints])}],
                    travelMode: google.maps.TravelMode.DRIVING
                }}, function(response, status) {{
                    if (status === "OK") {{
                        directionsRenderer.setDirections(response);
                    }} else {{
                        alert("Directions request failed: " + status);
                    }}
                }});
            }}
        </script>
    </head>
    <body onload="initMap()">
        <h2>Shortest Delivery Route (Road-Based)</h2>
        <div id="map" style="width:100%; height:600px;"></div>
    </body>
    </html>
    """

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)

    webbrowser.open(filename)
