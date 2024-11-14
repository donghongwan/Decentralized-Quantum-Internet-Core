import unittest
from services.analytics_service import AnalyticsService

class AnalyticsServiceTest(unittest.TestCase):
    def test_analyze_data(self):
        insights = AnalyticsService.analyze_data()
        self.assertIsNotNone(insights)

if __name__ == '__main__':
    unittest.main()
