import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    yield driver
    driver.quit()

@pytest.fixture
def log_in(driver):
    driver.find_element(*Locators.LOGIN_INTO_ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.INPUT_FIELD_EMAIL).send_keys("dariachernukha14465@yandex.ru")
    driver.find_element(*Locators.INPUT_FIELD_PASSWORD).send_keys("123456")
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.text_to_be_present_in_element(Locators.LOGIN_INTO_ACCOUNT_BUTTON, "Оформить заказ"))