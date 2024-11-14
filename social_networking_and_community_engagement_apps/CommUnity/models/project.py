class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True ```python
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    members = db.relationship('User ', secondary='project_members')

class ProjectMembers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
