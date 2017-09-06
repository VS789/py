from pages.googlePage import *
from selenium import webdriver
import unittest
import HtmlTestRunner

class OrtnectSearchViaGoogleSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_via_first_link_in_search_result(self):
        page = GooglePage(self.driver)
        page.googleIsLoaded()
        page.doSearchByTextUsingEnter('Ortnec')
        assert "Ortnec" in page.openFirstResultFirstLink().getTitle()

    def test_search_via_second_link_in_google_search_result(self):
        page = GooglePage(self.driver)
        page.googleIsLoaded()
        page.doSearchByTextUsingEnter('Ortnec')
        assert "Ortnec" in page.openFirstResultSecondLink().getTitle()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="./"))