from models.event import Event

def create_event(title, description, date, group_id):
    new_event = Event(title=title, description=description, date=date, group_id=group_id)
    db.session.add(new_event)
    db.session.commit()
    return new_event
