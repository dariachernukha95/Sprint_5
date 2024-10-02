from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators

class TestLogIn:
    def test_login_by_login_button_on_main_page(self,driver):
        driver.find_element(*Locators.LOGIN_INTO_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.INPUT_FIELD_EMAIL).send_keys("dariachernukha14465@yandex.ru")
        driver.find_element(*Locators.INPUT_FIELD_PASSWORD).send_keys("123456")
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.text_to_be_present_in_element(Locators.LOGIN_INTO_ACCOUNT_BUTTON, "Оформить заказ"))
        make_order_button_text = driver.find_element(*Locators.LOGIN_INTO_ACCOUNT_BUTTON).text
        assert make_order_button_text == 'Оформить заказ'

    def test_login_by_personal_account_button(self,driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.INPUT_FIELD_EMAIL).send_keys("dariachernukha14465@yandex.ru")
        driver.find_element(*Locators.INPUT_FIELD_PASSWORD).send_keys("123456")
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.text_to_be_present_in_element(Locators.LOGIN_INTO_ACCOUNT_BUTTON, "Оформить заказ"))
        make_order_button_text = driver.find_element(*Locators.LOGIN_INTO_ACCOUNT_BUTTON).text
        assert make_order_button_text == 'Оформить заказ'

    def test_login_by_login_button_on_registration_page(self,driver):
        driver.find_element(*Locators.LOGIN_INTO_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        driver.find_element(*Locators.LOGIN_BUTTON_ON_REGISTRATION_PAGE).click()
        driver.find_element(*Locators.INPUT_FIELD_EMAIL).send_keys("dariachernukha14465@yandex.ru")
        driver.find_element(*Locators.INPUT_FIELD_PASSWORD).send_keys("123456")
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.text_to_be_present_in_element(Locators.LOGIN_INTO_ACCOUNT_BUTTON, "Оформить заказ"))
        make_order_button_text = driver.find_element(*Locators.LOGIN_INTO_ACCOUNT_BUTTON).text
        assert make_order_button_text == 'Оформить заказ'

    def test_login_by_change_password_button(self,driver):
        driver.find_element(*Locators.LOGIN_INTO_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.CHANGE_PASSWORD_BUTTON).click()
        driver.find_element(*Locators.LOGIN_BUTTON_ON_REGISTRATION_PAGE).click()
        driver.find_element(*Locators.INPUT_FIELD_EMAIL).send_keys("dariachernukha14465@yandex.ru")
        driver.find_element(*Locators.INPUT_FIELD_PASSWORD).send_keys("123456")
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.text_to_be_present_in_element(Locators.LOGIN_INTO_ACCOUNT_BUTTON, "Оформить заказ"))
        make_order_button_text = driver.find_element(*Locators.LOGIN_INTO_ACCOUNT_BUTTON).text
        assert make_order_button_text == 'Оформить заказ'
