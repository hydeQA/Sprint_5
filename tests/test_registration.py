import time

import settings
from locators import BurgerLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from helpers import user_email_generator
from selenium.webdriver.common.by import By


class TestBurgerRegistration:
    def test_min_6_symbols_password_succes_registration(self, driver):
        enter_button = driver.find_element(*BurgerLocators.ENTER_BUTTON_MAIN)
        enter_button.click()
        register_button = driver.find_element(*BurgerLocators.REGISTRATION_LINK)
        register_button.click()
        registration_field_name = driver.find_element(*BurgerLocators.REGISTRATION_FIELD_NAME)
        registration_field_name.send_keys("Алексей")
        registration_field_email = driver.find_element(*BurgerLocators.REGISTRATION_FIELD_EMAIL)
        registration_field_email.send_keys(user_email_generator()['email'])
        registration_field_password = driver.find_element(*BurgerLocators.REGISTRATION_FIELD_PASSWORD)
        registration_field_password.send_keys("123456")
        driver.find_element(*BurgerLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(BurgerLocators.LOGIN_BUTTON))
        assert driver.current_url == settings.URL_LOGIN
        driver.quit()

    def test_5_symbols_password_appear_error(self, driver):
        enter_button = driver.find_element(*BurgerLocators.ENTER_BUTTON_MAIN)
        enter_button.click()
        register_button = driver.find_element(*BurgerLocators.REGISTRATION_LINK)
        register_button.click()
        registration_field_name = driver.find_element(*BurgerLocators.REGISTRATION_FIELD_NAME)
        registration_field_name.send_keys("Алексей")
        registration_field_email = driver.find_element(*BurgerLocators.REGISTRATION_FIELD_EMAIL)
        registration_field_email.send_keys(user_email_generator()['email'])
        registration_field_password = driver.find_element(*BurgerLocators.REGISTRATION_FIELD_PASSWORD)
        registration_field_password.send_keys("12345")
        driver.find_element(*BurgerLocators.REGISTRATION_BUTTON).click()
        assert driver.find_element(*BurgerLocators.TEXT_ERROR).is_displayed(), "Error. A password less than 6 characters long is accepted."
        driver.quit()

    def test_empty_password_appear_error(self, driver):
        enter_button = driver.find_element(*BurgerLocators.ENTER_BUTTON_MAIN)
        enter_button.click()
        register_button = driver.find_element(*BurgerLocators.REGISTRATION_LINK)
        register_button.click()
        registration_field_name = driver.find_element(*BurgerLocators.REGISTRATION_FIELD_NAME)
        registration_field_name.send_keys("Алексей")
        registration_field_email = driver.find_element(*BurgerLocators.REGISTRATION_FIELD_EMAIL)
        registration_field_email.send_keys(user_email_generator()['email'])
        driver.find_element(*BurgerLocators.REGISTRATION_BUTTON).click()
        assert driver.current_url == settings.URL_REGISTER
        driver.quit()

    def test_empty_name_appear_error(self, driver):
        enter_button = driver.find_element(*BurgerLocators.ENTER_BUTTON_MAIN)
        enter_button.click()
        register_button = driver.find_element(*BurgerLocators.REGISTRATION_LINK)
        register_button.click()
        registration_field_email = driver.find_element(*BurgerLocators.REGISTRATION_FIELD_EMAIL)
        registration_field_email.send_keys(user_email_generator()['email'])
        registration_field_password = driver.find_element(*BurgerLocators.REGISTRATION_FIELD_PASSWORD)
        registration_field_password.send_keys("123456")
        driver.find_element(*BurgerLocators.REGISTRATION_BUTTON).click()
        assert driver.current_url == settings.URL_REGISTER
        driver.quit()

    def test_incorrect_password_appear_error(self, driver):
        enter_button = driver.find_element(*BurgerLocators.ENTER_BUTTON_MAIN)
        enter_button.click()
        register_button = driver.find_element(*BurgerLocators.REGISTRATION_LINK)
        register_button.click()
        registration_field_name = driver.find_element(*BurgerLocators.REGISTRATION_FIELD_NAME)
        registration_field_name.send_keys("Алексей")
        registration_field_email = driver.find_element(*BurgerLocators.REGISTRATION_FIELD_EMAIL)
        registration_field_email.send_keys('54321ya.ru')
        registration_field_password = driver.find_element(*BurgerLocators.REGISTRATION_FIELD_PASSWORD)
        registration_field_password.send_keys("123456")
        driver.find_element(*BurgerLocators.REGISTRATION_BUTTON).click()
        time.sleep(3)
        assert driver.find_element(*BurgerLocators.TEXT_ERROR_REGISTRATION).is_displayed(), "Error. Email that does not match the mask is accepted."
        driver.quit()
