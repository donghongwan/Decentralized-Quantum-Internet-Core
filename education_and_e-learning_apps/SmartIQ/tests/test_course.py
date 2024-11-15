import unittest
from main import app, db
from models import Course, User

class CourseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        
        # Create a new database for testing
        with app.app_context():
            db.create_all()
            # Create a test user
            test_user = User(username='testuser', email='test@example.com', password='password')
            db.session.add(test_user)
            db.session.commit()

    def tearDown(self):
        # Drop the database after each test
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_course(self):
        # Test creating a new course
        response = self.app.post('/courses', json={
            'title': 'Test Course',
            'description': 'A course for testing',
            'content': 'Course content goes here.'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Course created successfully!', response.data)

        # Verify that the course was added to the database
        with app.app_context():
            course = Course.query.filter_by(title='Test Course').first()
            self.assertIsNotNone(course)
            self.assertEqual(course.description, 'A course for testing')
            self.assertEqual(course.content, 'Course content goes here.')

    def test_create_course_missing_fields(self):
        # Test creating a course with missing fields
        response = self.app.post('/courses', json={
            'title': 'Incomplete Course'
            # Missing description and content
        })
        self.assertEqual(response.status_code, 400)  # Assuming the API returns 400 for bad requests
        self.assertIn(b'Missing required fields', response.data)

    def test_create_course_invalid_data(self):
        # Test creating a course with invalid data
        response = self.app.post('/courses', json={
            'title': '',
            'description': 'A course with no title',
            'content': 'Course content goes here.'
        })
        self.assertEqual(response.status_code, 400)  # Assuming the API returns 400 for bad requests
        self.assertIn(b'Invalid course title', response.data)

if __name__ == '__main__':
    unittest.main()
