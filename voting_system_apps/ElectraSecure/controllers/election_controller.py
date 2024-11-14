from flask import request, jsonify
from services.election_service import ElectionService

class ElectionController:
    def __init__(self, app):
        self.election_service = ElectionService()
        app.add_url_rule('/elections', 'create_election', self.create_election, methods=['POST'])
        app.add_url_rule('/elections', 'get_elections', self.get_elections, methods=['GET'])

    def create_election(self):
        data = request.json
        self.election_service.create_election(data['title'], data['start_time'], data['end_time'])
        return jsonify({"message": "Election created successfully"}), 201

    def get_elections(self):
        elections = self.election_service.get_elections()
        return jsonify(elections), 200
