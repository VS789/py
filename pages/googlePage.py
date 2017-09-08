from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pages.ortnecPage import *

class GooglePage():

    driver = webdriver

    #google start search page selectors
    searchField = "#gs_lc0 input:nth-child(1)"

    #search result selectors
    listOfSearchResult = ".srg"
    firstResult = ".srg .g:nth-child(1)"

    #first search Result Selectors
    linkOfFirstResult = ".srg .g:nth-child(1) .f.kv._SWb ._Rm"
    firstLink = ".srg .g:nth-child(1) .r a"
    secondLink = ".srg .g:nth-child(1) .s .f.kv._SWb > a"

    def __init__(self,driver):
        self.driver = driver
        #1. Open google.com
        driver.get("http://google.com/")
        # check that page is loaded
        self.driver.find_element_by_css_selector(css_selector=self.searchField)

    #input text in search field, after that imitate Enter press on keyboard and wait result of search
    def doSearchByTextUsingEnter(self,text):
        searchField = self.driver.find_element_by_css_selector(self.searchField)
        #2. Type Ortnec in search input field
        searchField.send_keys(text)
        #3. Press "Enter" button
        searchField.send_keys(Keys.ENTER)
        #wait result of search
        self.driver.find_element_by_css_selector(self.listOfSearchResult)

    #return text of first link from search result
    def getTextFirstLinkInResultList(self):
        return self.driver.find_element_by_css_selector(css_selector=self.linkOfFirstResult).text


    #4. On Search Result page click on first link
    #use first link(Big blue link) for navigation
    def openFirstResultFirstLink(self):
        self.driver.find_element_by_css_selector(css_selector=self.firstLink).click()
        return OrtnecPage(self.driver)

    #4. On Search Result page click on second link
    #use second link (Navigete to this page) for navigation
    def openFirstResultSecondLink(self):
        self.driver.find_element_by_css_selector(css_selector=self.secondLink).click()
        return OrtnecPage(self.driver)