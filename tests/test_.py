import unittest
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.edge.service import Service


class RegexAidUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()

    def test_valid_regex_match_highlighting(self):
        driver = self.driver
        driver.get("http://localhost:8000/RegEx-It.html")  # Replace with your local server path
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

    def test_invalid_regex_input(self):
        self.driver.get("http://localhost:8000/RegEx-It.html")  # Replace with the actual local server path and HTML

        # Find the input elements by their IDs
        regex_input = self.driver.find_element(By.ID, 'regex-input')
        text_input = self.driver.find_element(By.ID, 'text-input')
        output_div = self.driver.find_element(By.ID, 'output')

        # Input an invalid regex pattern
        invalid_regex = '[a-z'
        regex_input.send_keys(invalid_regex)
        text_input.send_keys("Some sample text that won't be matched due to invalid regex.")

        # Wait until the error message appears or until a reasonable timeout
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.text_to_be_present_in_element((By.ID, 'output'), "Error:"))

        # Check that an error message is displayed and input fields are highlighted with an error color
        error_message = output_div.text
        regex_input_bgcolor = regex_input.value_of_css_property('background-color')
        self.assertIn("Error:", error_message, "No error message displayed when invalid regex input is given.")
        self.assertEqual(regex_input_bgcolor, 'rgba(250, 128, 114, 1)', "Regex input field not highlighted correctly.")

    def test_regex_flags_functionality(self):
        driver = self.driver
        driver.get(
            "http://localhost:8000/your_html_file.html")  # Replace with the actual local server path and HTML file name

        # Find the regex input and text input elements by their IDs.
        regex_input = driver.find_element(By.ID, 'regex-input')
        flags_input = driver.find_element(By.ID, 'flags-input')
        text_input = driver.find_element(By.ID, 'text-input')
        output_div = driver.find_element(By.ID, 'output')

        # Input regex pattern that matches the word "sample" at the end of a string.
        regex_input.send_keys('sample$')
        # Add "m" flag for multi-line search.
        flags_input.send_keys('m')
        # Input text with "sample" at the end of a line, but not at the end of the entire text string.
        text_input.send_keys("This is a sample\nThis line doesn't end with the target word.")

        # Assert that the match is found and highlighted appropriately.
        highlighted_text = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'highlight-blue'))
        )

        self.assertIsNotNone(highlighted_text, "The regex pattern wasn't highlighted with the flags provided.")
        self.assertEqual(highlighted_text.text, 'sample', "The highlighted text does not match 'sample'.")

    def test_unsupported_flag(self):
        driver = self.driver
        driver.get("http://localhost:8000/your_html_file.html")  # Replace with the actual URL

        # Find the regex input and flags input element by their IDs
        regex_input = driver.find_element(By.ID, 'regex-input')
        flags_input = driver.find_element(By.ID, 'flags-input')
        output_div = driver.find_element(By.ID, 'output')

        # Input a valid regex pattern followed by an unsupported flag 'x'
        regex_input.send_keys('ab+c')
        flags_input.send_keys('x')  # 'x' is not a valid flag in JavaScript regex

        # If the application correctly handles unsupported flags, an error message
        # should be displayed, and potentially the flags input field is styled differently
        # to indicate the error - adjust the CSS value check as per your application's response design.
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'output'))
        ).text
        flags_input_error_style = flags_input.value_of_css_property(
            'border-color')  # Example CSS property that might be used to indicate an error

        # Verify that the error message is displayed
        self.assertIn("Error:", error_message, "No error message displayed when unsupported flag input is given.")
        self.assertEqual(flags_input_error_style, 'rgba(255, 0, 0, 1)',
                         "Flags input field is not styled correctly to indicate an error.")  # Adjust RGBA to your
        # error indication color

    def test_empty_regex_input(self):
        driver = self.driver
        driver.get(
            "http://localhost:8000/your_html_file.html")  # Replace with the actual local server path and HTML file name

        # Find the input elements by their IDs
        regex_input = driver.find_element(By.ID, 'regex-input')
        text_input = driver.find_element(By.ID, 'text-input')
        output_div = driver.find_element(By.ID, 'output')

        # Clear any pre-filled values and leave the regex input empty
        regex_input.clear()
        text_input.send_keys("Some sample text to match against the regex.")

        # Either wait for a specific message or check immediately that no results are displayed
        # This example assumes your application will have a default "No matches found." or similar message displayed
        wait = WebDriverWait(driver, 10)
        wait.until(EC.text_to_be_present_in_element((By.ID, 'output'), "No matches found."))

        # Check that the output contains a 'no matches' message or is indeed empty
        message_displayed = output_div.text
        self.assertIn("No matches found.", message_displayed,
                      "Expected a 'no matches' message for an empty regex input.")

    def test_escaped_characters(self):
        # The pattern includes escaped special characters
        pattern = r'\(escaped\) \[brackets\] \{curly braces\} \* \+ \? \^ \$ \.'
        # The test input string which includes the literal characters we want to match
        test_input = r"This input \(escaped\) [brackets] {curly braces} includes special regex characters * + ? ^ $ ."
        # Performing the search
        match = re.search(pattern, test_input)
        # Verifying that the match is successful
        self.assertIsNotNone(match, "The pattern with escaped special characters did not match the input as expected.")
    def test_multiple_matches_with_global_flag(self):
        driver = self.driver
        driver.get(
            "http://localhost:8000/your_html_file.html")  # Replace with the actual local server path and HTML file name

        # Find the regex input and text input elements by their IDs.
        regex_input = driver.find_element(By.ID, 'regex-input')
        flags_input = driver.find_element(By.ID, 'flags-input')
        text_input = driver.find_element(By.ID, 'text-input')

        # Input regex pattern that matches the word "sample" at the end of a string.
        regex_input.send_keys('sample$')
        # Add "gm" flags for global, multi-line search.
        flags_input.send_keys('gm')
        # Input text with the word "sample" at the end of two lines.
        text_input.send_keys("This is a sample\nAnother sample")

        # Give the page time to process and highlight matches.
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'highlight-blue'))
        )

        # Get all highlighted elements.
        highlighted_elements = driver.find_elements(By.CLASS_NAME, 'highlight-blue')

        # There should be two highlighted "sample" occurrences in the text.
        self.assertEqual(len(highlighted_elements), 2,
                         f"Expected 2 highlighted elements, got {len(highlighted_elements)} instead.")
        for element in highlighted_elements:
            self.assertEqual(element.text, 'sample', "The highlighted text does not match 'sample'.")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
