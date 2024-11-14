from models.group import Group

def create_group(name, description):
    new_group = Group(name=name, description=description)
    db.session.add(new_group)
    db.session.commit()
    return new_group
