from pages.googlePage import *
from selenium import webdriver

def googleSearchOrtnecTest():
    driver = webdriver.Chrome()
    googlePage = GooglePage (driver)
    googlePage.googleIsLoaded()
    googlePage.doSearchByTextUsingEnter('Ortnec')
    googlePage.openFirstResultFirstLink().getTitle()
    assert "Ortnec" in driver.title
    driver.quit()

if __name__ == '__main__':
    googleSearchOrtnecTest()