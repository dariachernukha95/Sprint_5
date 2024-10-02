from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators

class TestConstructorPage:
    def test_press_constructor_button_from_personal_account(self,driver,log_in):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.DESCRIPTION_OF_PROFILE_PAGE))
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.MAKE_BURGER_HEADER))
        constructor_url = "https://stellarburgers.nomoreparties.site/"
        assert driver.current_url == constructor_url

    def test_press_logo_stellar_burgers_from_personal_account(self,driver,log_in):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.DESCRIPTION_OF_PROFILE_PAGE))
        driver.find_element(*Locators.STELLAR_BURGERS_LOGO).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.MAKE_BURGER_HEADER))
        constructor_url = "https://stellarburgers.nomoreparties.site/"
        assert driver.current_url == constructor_url

    def test_select_sauce_page(self, driver):
        driver.find_element(*Locators.SAUCE_PAGE).click()
        active_page_text = driver.find_element(*Locators.ACTIVE_PAGE).text
        assert active_page_text == "Соусы"

    def test_select_filling_page(self, driver):
        driver.find_element(*Locators.FILLING_PAGE).click()
        active_page_text = driver.find_element(*Locators.ACTIVE_PAGE).text
        assert active_page_text == "Начинки"

    def test_select_bun_page(self, driver):
        driver.find_element(*Locators.SAUCE_PAGE).click()
        driver.find_element(*Locators.BUN_PAGE).click()
        active_page_text = driver.find_element(*Locators.ACTIVE_PAGE).text
        assert active_page_text == "Булки"