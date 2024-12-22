from database import create_app
from routes.countries import register_countries_routes
from routes.cities import register_cities_routes
from routes.temperatures import register_temperatures_routes

app = create_app()

register_countries_routes(app)
register_cities_routes(app)
register_temperatures_routes(app)

if __name__ == "__main__":
    print("Registered routes:")
    for rule in app.url_map.iter_rules():
        print(rule)
    app.run(debug=True, host="0.0.0.0", port=5001)
