import unittest

from app import app


class AppRoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_index_page_loads(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        content = response.get_data(as_text=True)
        self.assertIn("B2B Lead Intelligence Dashboard", content)
        self.assertIn("Download Filtered CSV", content)

    def test_index_filters_by_city(self):
        response = self.client.get("/?city=Brooklyn")
        self.assertEqual(response.status_code, 200)
        content = response.get_data(as_text=True)
        self.assertIn("Brooklyn Tech Solutions", content)
        self.assertNotIn("Smile Care Dental", content)

    def test_export_returns_csv_file(self):
        response = self.client.get("/export?country=USA&category=Dentist")
        self.assertEqual(response.status_code, 200)
        self.assertIn("text/csv", response.content_type)
        self.assertEqual(
            response.headers.get("Content-Disposition"),
            "attachment; filename=filtered_leads.csv",
        )
        content = response.get_data(as_text=True)
        self.assertIn("company_name", content)
        self.assertIn("Smile Care Dental", content)


if __name__ == "__main__":
    unittest.main()
