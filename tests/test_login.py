from locators import BurgerLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestBurgerLogin:
    def test_login_in_main_page_success(self, driver):
        enter_button = driver.find_element(*BurgerLocators.ENTER_BUTTON_MAIN)
        enter_button.click()
        login_field_email = driver.find_element(*BurgerLocators.REGISTRATION_FIELD_EMAIL)
        login_field_email.send_keys("bukatkin@yandex.ru")
        login_field_password = driver.find_element(*BurgerLocators.REGISTRATION_FIELD_PASSWORD)
        login_field_password.send_keys("123456")
        driver.find_element(*BurgerLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(BurgerLocators.ORDER_BUTTON))
        assert driver.find_element(*BurgerLocators.TITLE_CONSTRUCTOR).is_displayed(), "Title don't exist"

    def test_login_in_personal_account_success(self, driver):
        account_button = driver.find_element(*BurgerLocators.ACCOUNT_BUTTON)
        account_button.click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(BurgerLocators.REGISTRATION_TITLE))
        login_field_email = driver.find_element(*BurgerLocators.REGISTRATION_FIELD_EMAIL)
        login_field_email.send_keys("bukatkin@yandex.ru")
        login_field_password = driver.find_element(*BurgerLocators.REGISTRATION_FIELD_PASSWORD)
        login_field_password.send_keys("123456")
        driver.find_element(*BurgerLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(BurgerLocators.ORDER_BUTTON))
        assert driver.find_element(*BurgerLocators.TITLE_CONSTRUCTOR).is_displayed(), "Title don't exist"

    def test_login_button_in_registration_form_success(self, driver):
        enter_button = driver.find_element(*BurgerLocators.ENTER_BUTTON_MAIN)
        enter_button.click()
        register_button = driver.find_element(*BurgerLocators.REGISTRATION_LINK)
        register_button.click()
        driver.find_element(*BurgerLocators.BUTTON_ENTER).click()
        login_field_email = driver.find_element(*BurgerLocators.REGISTRATION_FIELD_EMAIL)
        login_field_email.send_keys("bukatkin@yandex.ru")
        login_field_password = driver.find_element(*BurgerLocators.REGISTRATION_FIELD_PASSWORD)
        login_field_password.send_keys("123456")
        driver.find_element(*BurgerLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(BurgerLocators.ORDER_BUTTON))
        assert driver.find_element(*BurgerLocators.TITLE_CONSTRUCTOR).is_displayed(), "Title don't exist"

    def test_login_button_form_recovery_form_success(self, driver):
        enter_button = driver.find_element(*BurgerLocators.ENTER_BUTTON_MAIN)
        enter_button.click()
        recover_button = driver.find_element(*BurgerLocators.RECOVER_BUTTON)
        recover_button.click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(BurgerLocators.TITLE_RECOVER))
        driver.find_element(*BurgerLocators.BUTTON_ENTER_RECOVER).click()
        login_field_email = driver.find_element(*BurgerLocators.REGISTRATION_FIELD_EMAIL)
        login_field_email.send_keys("bukatkin@yandex.ru")
        login_field_password = driver.find_element(*BurgerLocators.REGISTRATION_FIELD_PASSWORD)
        login_field_password.send_keys("123456")
        driver.find_element(*BurgerLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(BurgerLocators.ORDER_BUTTON))
        assert driver.find_element(*BurgerLocators.TITLE_CONSTRUCTOR).is_displayed(), "Title don't exist"
