import unittest
from services.election_service import ElectionService
from models.election import Election

class TestElectionService(unittest.TestCase):
    def setUp(self):
        self.election_service = ElectionService()
        self.election_service.elections = []  # Mocking the elections list

    def test_create_election(self):
        # Test creating a new election
        title = "Presidential Election 2024"
        start_time = "2024-11-01T08:00:00Z"
        end_time = "2024-11-01T20:00:00Z"
        
        self.election_service.create_election(title, start_time, end_time)
        
        # Check if the election was added
        self.assertEqual(len(self.election_service.elections), 1)
        self.assertEqual(self.election_service.elections[0].title, title)
        self.assertEqual(self.election_service.elections[0].start_time, start_time)
        self.assertEqual(self.election_service.elections[0].end_time, end_time)

    def test_get_elections(self):
        # Test retrieving all elections
        title1 = "Presidential Election 2024"
        start_time1 = "2024-11-01T08:00:00Z"
        end_time1 = "2024-11-01T20:00:00Z"
        
        title2 = "Local Election 2024"
        start_time2 = "2024-05-01T08:00:00Z"
        end_time2 = "2024-05-01T20:00:00Z"
        
        # Create two elections
        self.election_service.create_election(title1, start_time1, end_time1)
        self.election_service.create_election(title2, start_time2, end_time2)
        
        elections = self.election_service.get_elections()
        
        # Check if the correct number of elections is returned
        self.assertEqual(len(elections), 2)
        
        # Check if the details of the elections are correct
        self.assertEqual(elections[0].title, title1)
        self.assertEqual(elections[1].title, title2)

    def test_election_time_validation(self):
        # Test that an election cannot be created with an end time before the start time
        title = "Invalid Election"
        start_time = "2024-11-01T20:00:00Z"
        end_time = "2024-11-01T08:00:00Z"
        
        with self.assertRaises(ValueError) as context:
            self.election_service.create_election(title, start_time, end_time)
        
        self.assertEqual(str(context.exception), "End time must be after start time.")

if __name__ == '__main__':
    unittest.main()
