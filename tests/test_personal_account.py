import settings
from locators import BurgerLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestPersonalAccount:
    def test_go_to_personal_account_success(self, driver):
        enter_button = driver.find_element(*BurgerLocators.ENTER_BUTTON_MAIN)
        enter_button.click()
        login_field_email = driver.find_element(*BurgerLocators.REGISTRATION_FIELD_EMAIL)
        login_field_email.send_keys("bukatkin@yandex.ru")
        login_field_password = driver.find_element(*BurgerLocators.REGISTRATION_FIELD_PASSWORD)
        login_field_password.send_keys("123456")
        driver.find_element(By.XPATH, "//button[text() = 'Войти']").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(BurgerLocators.ORDER_BUTTON))
        driver.find_element(*BurgerLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//p[text() = 'В этом разделе вы можете изменить свои персональные данные']")))
        assert driver.current_url == settings.URL_PROFILE
        driver.quit()

    def test_exit_from_account_success(self, driver):
        enter_button = driver.find_element(*BurgerLocators.ENTER_BUTTON_MAIN)
        enter_button.click()
        login_field_email = driver.find_element(*BurgerLocators.REGISTRATION_FIELD_EMAIL)
        login_field_email.send_keys("bukatkin@yandex.ru")
        login_field_password = driver.find_element(*BurgerLocators.REGISTRATION_FIELD_PASSWORD)
        login_field_password.send_keys("123456")
        driver.find_element(By.XPATH, "//button[text() = 'Войти']").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(BurgerLocators.ORDER_BUTTON))
        driver.find_element(*BurgerLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//p[text() = 'В этом разделе вы можете изменить свои персональные данные']")))
        driver.find_element(*BurgerLocators.EXIT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(BurgerLocators.REGISTRATION_TITLE))
        assert driver.current_url == settings.URL_LOGIN
        driver.quit()