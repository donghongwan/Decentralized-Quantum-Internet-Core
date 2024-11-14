from models.resource import Resource

def share_resource(title, description, owner_id):
    new_resource = Resource(title=title, description=description, owner_id=owner_id)
    db.session.add(new_resource)
    db.session.commit()
    return new_resource
