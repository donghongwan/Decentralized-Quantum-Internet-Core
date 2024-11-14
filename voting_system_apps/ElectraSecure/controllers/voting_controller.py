from flask import request, jsonify
from services.voting_service import VotingService

class VotingController:
    def __init__(self, app):
        self.voting_service = VotingService()
        app.add_url_rule('/vote', 'cast_vote', self.cast_vote, methods=['POST'])
        app.add_url_rule('/results/<int:election_id>', 'get_results', self.get_results, methods=['GET'])

    def cast_vote(self):
        data = request.json
        self.voting_service.cast_vote(data['user_id'], data['election_id'], data['candidate_id'])
        return jsonify({"message": "Vote cast successfully"}), 201

    def get_results(self, election_id):
        results = self.voting_service.get_results(election_id)
        return jsonify(results), 200
