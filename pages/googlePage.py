from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pages.ortnecPage import *

class GooglePage():

    driver = webdriver
    searchField = "#gs_lc0 input:nth-child(1)"
    resultOfSearch = ".srg"
    firstResult = ".srg .g:nth-child(1)"

    def __init__(self,driver):
        self.driver = driver
        driver.get("http://google.com/")
    def googleIsLoaded(self):
        self.driver.find_element_by_css_selector(css_selector=self.searchField)

    def doSearchByTextUsingEnter(self,text):
        searchField = self.driver.find_element_by_css_selector(self.searchField)
        searchField.send_keys(text)
        searchField.send_keys(Keys.ENTER)
        self.driver.find_element_by_css_selector(self.resultOfSearch)

    def openFirstResultFirstLink(self):
        firstLink = self.driver.find_element_by_css_selector(css_selector=".srg .g:nth-child(1) .r a")
        firstLink.click()
        return OrtnecPage(self.driver)

    def openFirstResultSecondLink(self):
        secondLink = self.driver.find_element_by_css_selector(css_selector=".srg .g:nth-child(1) .s .f.kv._SWb > a")
        secondLink.click()
        return OrtnecPage(self.driver)