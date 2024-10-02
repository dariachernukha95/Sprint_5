from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
from registration_data import RegistrationData
class TestRegistration:
    def test_registration_success(self,driver):
        driver.find_element(*Locators.LOGIN_INTO_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        driver.find_element(*Locators.INPUT_FIELD_NAME).send_keys("Дарья")
        driver.find_element(*Locators.INPUT_FIELD_EMAIL).send_keys(RegistrationData.random_email())
        driver.find_element(*Locators.INPUT_FIELD_PASSWORD).send_keys(RegistrationData.random_password())
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.text_to_be_present_in_element(Locators.LOG_IN_FORM_HEADER, "Вход"))
        name_of_form = driver.find_element(*Locators.LOG_IN_FORM_HEADER).text
        assert name_of_form == 'Вход'

    def test_registration_invalid_password(self,driver):
        driver.find_element(*Locators.LOGIN_INTO_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        driver.find_element(*Locators.INPUT_FIELD_NAME).send_keys("Дарья")
        driver.find_element(*Locators.INPUT_FIELD_EMAIL).send_keys(RegistrationData.random_email())
        driver.find_element(*Locators.INPUT_FIELD_PASSWORD).send_keys(RegistrationData.random_password()[:5])
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located(Locators.INVALID_PASSWORD_TEXT))
        error_text = driver.find_element(*Locators.INVALID_PASSWORD_TEXT).text
        assert error_text == 'Некорректный пароль'
