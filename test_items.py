import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_find_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    browser.implicitly_wait(5)
    button = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert button, "No button"
