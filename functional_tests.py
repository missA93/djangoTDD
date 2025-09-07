import unittest
from selenium import webdriver 


class NewVisitortest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()
        
    def test_new_visitors_website_title(self):
        self.browser.get("http://127.0.0.1:8000/")
        self.assertIn("ToDo",self.browser.title) 


if __name__ == "__main__":
    unittest.main()
