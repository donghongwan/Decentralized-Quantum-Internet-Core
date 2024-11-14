from models.project import Project

def create_project(title, description):
    new_project = Project(title=title, description=description)
    db.session.add(new_project)
    db.session.commit()
    return new_project
