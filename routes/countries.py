from flask import request, jsonify
from models import db, Tara

def register_countries_routes(app):
    @app.route('/api/countries', methods=['POST'])
    def add_country():
        data = request.get_json()
        if not data or 'nume' not in data or 'lat' not in data or 'lon' not in data:
            return jsonify({'error': 'Bad Request'}), 400

        existing_country = Tara.query.filter_by(nume_tara=data['nume']).first()
        if existing_country:
            return jsonify({'error': 'Conflict: Country already exists'}), 409

        try:
            new_country = Tara(
                nume_tara=data['nume'],
                latitudine=data['lat'],
                longitudine=data['lon']
            )
            db.session.add(new_country)
            db.session.commit()
            return jsonify({'id': new_country.id}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 400

    @app.route('/api/countries', methods=['GET'])
    def get_countries():
        countries = Tara.query.all()
        return jsonify([{
            'id': country.id,
            'nume': country.nume_tara,
            'lat': country.latitudine,
            'lon': country.longitudine
        } for country in countries]), 200

    @app.route('/api/countries/<int:id>', methods=['PUT'])
    def update_country(id):
        data = request.get_json()
        if not data or 'nume' not in data or 'lat' not in data or 'lon' not in data:
            return jsonify({'error': 'Bad Request'}), 400

        country = Tara.query.get(id)
        if not country:
            return jsonify({'error': 'Not Found'}), 404

        try:
            country.nume_tara = data['nume']
            country.latitudine = data['lat']
            country.longitudine = data['lon']
            db.session.commit()
            return jsonify({'message': 'Country updated successfully'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 400

    @app.route('/api/countries/<int:id>', methods=['DELETE'])
    def delete_country(id):
        country = Tara.query.get(id)
        if not country:
            return jsonify({'error': 'Not Found'}), 404

        try:
            db.session.delete(country)
            db.session.commit()
            return jsonify({'message': 'Country deleted successfully'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    
