from pages.googlePage import *
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

def googleSearchOrtnecTest():
    driver = webdriver.Chrome()
    googlePage = GooglePage (driver)
    googlePage.doSearchByTextUsingEnter('Ortnec')
    print(len(googlePage.listOfAllElementsOfSearch()))
    #googlePage.listOfAllElementsOfSearch()[0].find_element_by_css_selector(css_selector=' .r a').click()
    listOfSearchedItems = googlePage.listOfAllElementsOfSearch()
    for each in googlePage.listOfAllElementsOfSearch():
        actions = ActionChains(driver)
        actions.key_down(Keys.CONTROL).click(googlePage.getLinkOfElementFormSearchList(each)).key_up(
            Keys.CONTROL).perform()
        assert "ortnec" in googlePage.getAllTextOnOpenedPage()
        print("Element with index ", listOfSearchedItems.index(each), " contains ortnec text")
        driver.switch_to.window(driver.window_handles[0])
    driver.quit()

if __name__ == '__main__':
    googleSearchOrtnecTest()