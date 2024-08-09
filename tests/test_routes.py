import unittest
from fastapi.testclient import TestClient
from main import create_app

app = create_app()
client = TestClient(app)

class AdvisorBotTestCase(unittest.TestCase):
    def test_advisor_endpoint(self):
        response = client.post('/api/advisor', json={"query": "How can I improve my productivity?"})
        self.assertEqual(response.status_code, 200)

    def test_advisor_missing_query(self):
        response = client.post('/api/advisor', json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn("Query is required", response.json().get("detail"))

if __name__ == "__main__":
    unittest.main()