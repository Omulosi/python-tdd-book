from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Edith has heard about a cool online to-do app. She goes
        # check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test')

        # she is invited to enter a to-do item straight away

        # She types 'Buy peacock feather' into a text boc (Edith's hobby is tying
        # fly-fishing lures)

        # When she hits enter, the page updates and now the page lists 
        # "1: But peacock feathers" as an item in a to-do list

        # There is still a text inviting her to add anothe ritem. She enters 
        # "Use peacock feathers to make a fly"

        # The page updates again with both items on the list

        # The site generates a unique URL for Edith -- there is some explanatory text
        # to that effect

        # She visits that URL - her to-do list is still there

        # Satisfied she goes back to sleep


if __name__ == '__main__':
    unittest.main(warnings='ignore')
