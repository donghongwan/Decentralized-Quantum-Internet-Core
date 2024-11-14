class Election:
    def __init__(self, election_id, title, start_time, end_time):
        self.election_id = election_id
        self.title = title
        self.start_time = start_time
        self.end_time = end_time
        self.votes = []
