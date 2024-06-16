import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegexAidUITest(unittest.TestCase):

    def set_up(self):
        # Set up the WebDriver (geckodriver for Firefox, or use chromedriver for Chrome)
        self.driver = webdriver.Firefox()

    def test_valid_regex_match_highlighting(self):
        driver = self.driver
        driver.get("http://localhost:8000/index.html")  # Replace with your local server path
        regex_input = driver.find_element(By.ID, 'regex-input')
        flags_input = driver.find_element(By.ID, 'flags-input')
        text_input = driver.find_element(By.ID, 'text-input')

        regex_input.send_keys('a+b*')
        flags_input.send_keys('g')
        text_input.send_keys('caaab cbb abbb')

        # Wait until the highlights appear
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'highlight-blue'))
        )

        # Check highlights
        highlights = driver.find_elements(By.CLASS_NAME, 'highlight-blue')
        self.assertTrue(len(highlights) > 0, "Matches should be highlighted.")

        # Add more tests following the similar pattern

    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()