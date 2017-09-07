from selenium import webdriver

class OrtnecPage:

    driver = webdriver

    def __init__(self,driver):
        self.driver = driver
        driver.get("http://ortnec.com/")

    def getTitle(self):
        return self.driver.title

    def getElement(self):
        return self.driver.find_element_by_css_selector(css_selector='.fleft h3')

    #returt text that contain in Copyright block on the bottom of page
    def getCopyrightBlockText(self):
        return self.driver.find_element_by_css_selector(css_selector='.copyright').text