import unittest
from examples.voting_system.app import VotingSystem

class TestVotingSystemIntegration(unittest.TestCase):
    def setUp(self):
        self.voting_app = VotingSystem()

    def test_cast_receive_vote(self):
        vote = '{"candidate": "Candidate A"}'
        self.voting_app.cast_vote(vote)
        self.voting_app.receive_vote()

        # Assert that the received vote matches the sent vote
        self.assertEqual(self.voting_app.node_b.state, self.voting_app.node_a.encrypt(vote))

if __name__ == "__main__":
    unittest.main()
