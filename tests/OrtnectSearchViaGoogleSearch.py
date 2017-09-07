from pages.googlePage import *
from selenium import webdriver
import unittest
import HtmlTestRunner

class OrtnectSearchViaGoogleSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    #this tets checks that 'ortnec' text is present after navigation via first link (Big blue link) in serch result list
    def test_search_via_first_link_in_search_result(self):
        page = GooglePage(self.driver)
        page.googleIsLoaded()
        page.doSearchByTextUsingEnter('Ortnec')
        assert "ortnec" in page.openFirstResultFirstLink().getCopyrightBlockText()

    #this tets checks that 'ortnec' text is present after navigation via second link (Navigate to this page) in serch result list
    def test_search_via_second_link_in_google_search_result(self):
        page = GooglePage(self.driver)
        page.googleIsLoaded()
        page.doSearchByTextUsingEnter('Ortnec')
        assert "ortnec" in page.openFirstResultSecondLink().getCopyrightBlockText()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="./"))