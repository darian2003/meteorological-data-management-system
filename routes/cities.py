from flask import request, jsonify
from models import db, Oras, Tara

def register_cities_routes(app):
    @app.route('/api/cities', methods=['POST'])
    def add_city():
        data = request.get_json()
        if not data or 'idTara' not in data or 'nume' not in data or 'lat' not in data or 'lon' not in data:
            return jsonify({'error': 'Bad Request'}), 400

        # Check if the country exists
        tara = Tara.query.get(data['idTara'])
        if not tara:
            return jsonify({'error': 'Country Not Found'}), 404

        # Check for duplicate city
        existing_city = Oras.query.filter_by(nume_oras=data['nume'], id_tara=data['idTara']).first()
        if existing_city:
            return jsonify({'error': 'Conflict: City already exists'}), 409

        try:
            new_city = Oras(
                id_tara=data['idTara'],
                nume_oras=data['nume'],
                latitudine=data['lat'],
                longitudine=data['lon']
            )
            db.session.add(new_city)
            db.session.commit()
            return jsonify({'id': new_city.id}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 400

    # GET /api/cities - Get all cities
    @app.route('/api/cities', methods=['GET'])
    def get_cities():
        cities = Oras.query.all()
        return jsonify([{
            'id': city.id,
            'idTara': city.id_tara,
            'nume': city.nume_oras,
            'lat': city.latitudine,
            'lon': city.longitudine
        } for city in cities]), 200

    # GET /api/cities/country/:id_Tara - Get cities by country ID
    @app.route('/api/cities/country/<int:id_tara>', methods=['GET'])
    def get_cities_by_country(id_tara):
        cities = Oras.query.filter_by(id_tara=id_tara).all()
        return jsonify([{
            'id': city.id,
            'idTara': city.id_tara,
            'nume': city.nume_oras,
            'lat': city.latitudine,
            'lon': city.longitudine
        } for city in cities]), 200

    # PUT /api/cities/:id - Update a city
    @app.route('/api/cities/<int:id>', methods=['PUT'])
    def update_city(id):
        data = request.get_json()
        if not data or 'idTara' not in data or 'nume' not in data or 'lat' not in data or 'lon' not in data:
            return jsonify({'error': 'Bad Request'}), 400

        city = Oras.query.get(id)
        if not city:
            return jsonify({'error': 'Not Found'}), 404

        try:
            city.id_tara = data['idTara']
            city.nume_oras = data['nume']
            city.latitudine = data['lat']
            city.longitudine = data['lon']
            db.session.commit()
            return jsonify({'message': 'City updated successfully'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 400

    # DELETE /api/cities/:id - Delete a city
    @app.route('/api/cities/<int:id>', methods=['DELETE'])
    def delete_city(id):
        city = Oras.query.get(id)
        if not city:
            return jsonify({'error': 'Not Found'}), 404

        try:
            db.session.delete(city)
            db.session.commit()
            return jsonify({'message': 'City deleted successfully'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 400
