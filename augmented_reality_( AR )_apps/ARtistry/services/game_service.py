from models import GameSession

class GameService:
    @staticmethod
    def create_game_session(user_id, score, duration):
        session = GameSession(user_id=user_id, score=score, duration=duration)
        db.session.add(session)
        db.session.commit()
        return session
