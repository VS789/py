from pages.ortnecPage import *
from selenium import webdriver

def checkOrtnecTextInOrtnecPage():
    ortnecPage = OrtnecPage(webdriver.Chrome())
    assert "Ortnec" in ortnecPage.getTitle()
    print(ortnecPage.getTitle())
    print(ortnecPage.getElement())

if __name__ == '__main__':
    checkOrtnecTextInOrtnecPage()
