import settings
from data import UserData
from locators import BurgerLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestPersonalAccount:
    def test_go_to_personal_account_success(self, driver):
        enter_button = driver.find_element(*BurgerLocators.ENTER_BUTTON_MAIN)
        enter_button.click()
        login_field_email = driver.find_element(*BurgerLocators.REGISTRATION_FIELD_EMAIL)
        login_field_email.send_keys(UserData.USER_EMAIL)
        login_field_password = driver.find_element(*BurgerLocators.REGISTRATION_FIELD_PASSWORD)
        login_field_password.send_keys(UserData.USER_PASSWORD)
        driver.find_element(*BurgerLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(BurgerLocators.ORDER_BUTTON))
        driver.find_element(*BurgerLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(BurgerLocators.TEXT_DESCRIPTION))
        assert driver.current_url == settings.URL_PROFILE

    def test_exit_from_account_success(self, driver):
        enter_button = driver.find_element(*BurgerLocators.ENTER_BUTTON_MAIN)
        enter_button.click()
        login_field_email = driver.find_element(*BurgerLocators.REGISTRATION_FIELD_EMAIL)
        login_field_email.send_keys(UserData.USER_EMAIL)
        login_field_password = driver.find_element(*BurgerLocators.REGISTRATION_FIELD_PASSWORD)
        login_field_password.send_keys(UserData.USER_PASSWORD)
        driver.find_element(*BurgerLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(BurgerLocators.ORDER_BUTTON))
        driver.find_element(*BurgerLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(BurgerLocators.TEXT_DESCRIPTION))
        driver.find_element(*BurgerLocators.EXIT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(BurgerLocators.REGISTRATION_TITLE))
        assert driver.current_url == settings.URL_LOGIN
