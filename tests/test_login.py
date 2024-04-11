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
        assert driver.find_element(By.XPATH, "//h1[text()='Соберите бургер']").is_displayed(), "Title don't exist"
        driver.quit()

    def test_login_in_personal_account_success(self, driver):
        account_button = driver.find_element(*BurgerLocators.ACCOUNT_BUTTON)
        account_button.click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((BurgerLocators.REGISTRATION_TITLE)))
        login_field_email = driver.find_element(*BurgerLocators.REGISTRATION_FIELD_EMAIL)
        login_field_email.send_keys("bukatkin@yandex.ru")
        login_field_password = driver.find_element(*BurgerLocators.REGISTRATION_FIELD_PASSWORD)
        login_field_password.send_keys("123456")
        driver.find_element(*BurgerLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(BurgerLocators.ORDER_BUTTON))
        assert driver.find_element(By.XPATH, "//h1[text()='Соберите бургер']").is_displayed(), "Title don't exist"
        driver.quit()

    def test_login_button_in_registration_form_success(self, driver):
        enter_button = driver.find_element(*BurgerLocators.ENTER_BUTTON_MAIN)
        enter_button.click()
        register_button = driver.find_element(*BurgerLocators.REGISTRATION_LINK)
        register_button.click()
        driver.find_element(By.XPATH, "//a[@class = 'Auth_link__1fOlj']").click()
        login_field_email = driver.find_element(*BurgerLocators.REGISTRATION_FIELD_EMAIL)
        login_field_email.send_keys("bukatkin@yandex.ru")
        login_field_password = driver.find_element(*BurgerLocators.REGISTRATION_FIELD_PASSWORD)
        login_field_password.send_keys("123456")
        driver.find_element(By.XPATH, "//button[text() = 'Войти']").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(BurgerLocators.ORDER_BUTTON))
        assert driver.find_element(By.XPATH, "//h1[text()='Соберите бургер']").is_displayed(), "Title don't exist"
        driver.quit()

    def test_login_button_form_recovery_form_success(self, driver):
        enter_button = driver.find_element(*BurgerLocators.ENTER_BUTTON_MAIN)
        enter_button.click()
        recover_button = driver.find_element(*BurgerLocators.RECOVER_BUTTON)
        recover_button.click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[text() = 'Восстановление пароля']")))
        driver.find_element(By.XPATH, "//a[text() = 'Войти']").click()
        login_field_email = driver.find_element(*BurgerLocators.REGISTRATION_FIELD_EMAIL)
        login_field_email.send_keys("bukatkin@yandex.ru")
        login_field_password = driver.find_element(*BurgerLocators.REGISTRATION_FIELD_PASSWORD)
        login_field_password.send_keys("123456")
        driver.find_element(By.XPATH, "//button[text() = 'Войти']").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(BurgerLocators.ORDER_BUTTON))
        assert driver.find_element(By.XPATH, "//h1[text()='Соберите бургер']").is_displayed(), "Title don't exist"
        driver.quit()
