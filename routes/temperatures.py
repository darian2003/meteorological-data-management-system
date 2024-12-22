from flask import request, jsonify
from models import db, Tara, Oras, Temperatura

def register_temperatures_routes(app):

    # POST /api/temperatures - Add a temperature
    @app.route('/api/temperatures', methods=['POST'])
    def add_temperature():
        data = request.get_json()
        if not data or 'idOras' not in data or 'valoare' not in data:
            return jsonify({'error': 'Bad Request'}), 400

        # Check if the city exists
        oras = Oras.query.get(data['idOras'])
        if not oras:
            return jsonify({'error': 'City Not Found'}), 404

        try:
            new_temperature = Temperatura(
                id_oras=data['idOras'],
                valoare=data['valoare']
            )
            db.session.add(new_temperature)
            db.session.commit()
            return jsonify({'id': new_temperature.id}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 400

    # GET /api/temperatures - Get temperatures by filters
    @app.route('/api/temperatures', methods=['GET'])
    def get_temperatures():
        lat = request.args.get('lat', type=float)
        lon = request.args.get('lon', type=float)
        from_date = request.args.get('from', type=str)
        until_date = request.args.get('until', type=str)

        query = Temperatura.query.join(Oras).join(Tara)

        if lat:
            query = query.filter(Oras.latitudine == lat)
        if lon:
            query = query.filter(Oras.longitudine == lon)
        if from_date:
            query = query.filter(Temperatura.timestamp >= from_date)
        if until_date:
            query = query.filter(Temperatura.timestamp <= until_date)

        temperatures = query.all()
        return jsonify([{
            'id': temp.id,
            'valoare': temp.valoare,
            'timestamp': temp.timestamp.isoformat()
        } for temp in temperatures]), 200

    # GET /api/temperatures/cities/:id_oras - Get temperatures by city ID
    @app.route('/api/temperatures/cities/<int:id_oras>', methods=['GET'])
    def get_temperatures_by_city(id_oras):
        from_date = request.args.get('from', type=str)
        until_date = request.args.get('until', type=str)

        query = Temperatura.query.filter_by(id_oras=id_oras)

        if from_date:
            query = query.filter(Temperatura.timestamp >= from_date)
        if until_date:
            query = query.filter(Temperatura.timestamp <= until_date)

        temperatures = query.all()
        return jsonify([{
            'id': temp.id,
            'valoare': temp.valoare,
            'timestamp': temp.timestamp.isoformat()
        } for temp in temperatures]), 200

    # GET /api/temperatures/countries/:id_tara - Get temperatures by country ID
    @app.route('/api/temperatures/countries/<int:id_tara>', methods=['GET'])
    def get_temperatures_by_country(id_tara):
        from_date = request.args.get('from', type=str)
        until_date = request.args.get('until', type=str)

        query = Temperatura.query.join(Oras).filter(Oras.id_tara == id_tara)

        if from_date:
            query = query.filter(Temperatura.timestamp >= from_date)
        if until_date:
            query = query.filter(Temperatura.timestamp <= until_date)

        temperatures = query.all()
        return jsonify([{
            'id': temp.id,
            'valoare': temp.valoare,
            'timestamp': temp.timestamp.isoformat()
        } for temp in temperatures]), 200

    # PUT /api/temperatures/:id - Update a temperature
    @app.route('/api/temperatures/<int:id>', methods=['PUT'])
    def update_temperature(id):
        data = request.get_json()
        if not data or 'id_oras' not in data or 'valoare' not in data:
            return jsonify({'error': 'Bad Request'}), 400

        temp = Temperatura.query.get(id)
        if not temp:
            return jsonify({'error': 'Not Found'}), 404

        try:
            temp.id_oras = data['id_oras']
            temp.valoare = data['valoare']
            db.session.commit()
            return jsonify({'message': 'Temperature updated successfully'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 400

    # DELETE /api/temperatures/:id - Delete a temperature
    @app.route('/api/temperatures/<int:id>', methods=['DELETE'])
    def delete_temperature(id):
        temp = Temperatura.query.get(id)
        if not temp:
            return jsonify({'error': 'Not Found'}), 404

        try:
            db.session.delete(temp)
            db.session.commit()
            return jsonify({'message': 'Temperature deleted successfully'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 400
