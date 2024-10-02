from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators

class TestPersonalAccount:
    def test_go_to_personal_account_by_unauthorized_user(self,driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.LOG_IN_FORM_HEADER))
        login_url = "https://stellarburgers.nomoreparties.site/login"
        assert driver.current_url == login_url

    def test_go_to_personal_account_by_authorized_user(self,driver,log_in):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.DESCRIPTION_OF_PROFILE_PAGE))
        profile_url = "https://stellarburgers.nomoreparties.site/account/profile"
        assert driver.current_url == profile_url

    def test_log_out_from_personal_account(self,driver,log_in):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.LOGOUT_BUTTON))
        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.LOG_IN_FORM_HEADER))
        login_url = "https://stellarburgers.nomoreparties.site/login"
        assert driver.current_url == login_url