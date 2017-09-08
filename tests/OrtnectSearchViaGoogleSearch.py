from pages.googlePage import *
from selenium import webdriver
import unittest
import HtmlTestRunner

class OrtnectSearchViaGoogleSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    #this tets checks that 'ortnec' text is present after navigation via first link (Big blue link) in serch result list
    def test_search_via_first_link_in_search_result(self):
        #1. Open google.com and check that page is loaded
        page = GooglePage(self.driver)
        #2. Type Ortnec in search input field and #3. Press "Enter" button
        page.doSearchByTextUsingEnter('Ortnec')
        #a) check http://ortnec.com link is first in the list of results
        assert "ortnec.com/" == page.getTextFirstLinkInResultList()
        #b) for EACH link on the 1-st result page: click on link and check 'ortnec' text is present on opened page
        assert "ortnec" in page.openFirstResultFirstLink().getCopyrightBlockText()

    #this tets checks that 'ortnec' text is present after navigation via second link (Navigate to this page) in serch result list
    def test_search_via_second_link_in_google_search_result(self):
        #1. Open google.com and check that page is loaded
        page = GooglePage(self.driver)
        #2. Type Ortnec in search input field and #3. Press "Enter" button
        page.doSearchByTextUsingEnter('Ortnec')
        #a) check http://ortnec.com link is first in the list of results
        assert "ortnec.com/" == page.getTextFirstLinkInResultList()
        #b) for EACH link on the 1-st result page: click on link and check 'ortnec' text is present on opened page
        assert "ortnec" in page.openFirstResultSecondLink().getCopyrightBlockText()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="./"))