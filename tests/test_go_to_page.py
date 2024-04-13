import settings
from locators import BurgerLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestGoToPage:
    def test_go_to_constructor_success(self, driver):
        driver.find_element(*BurgerLocators.ENTER_BUTTON_MAIN).click()
        driver.find_element(*BurgerLocators.BUTTON_CONSTRUCTOR).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(BurgerLocators.TITLE_CONSTRUCTOR))

        assert driver.current_url == settings.URL
        driver.quit()

    def test_go_to_stellar_burgers_logo_success(self, driver):
        driver.find_element(*BurgerLocators.ENTER_BUTTON_MAIN).click()
        driver.find_element(*BurgerLocators.LOGO_BURGERS).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(BurgerLocators.TITLE_CONSTRUCTOR))

        assert driver.current_url == settings.URL
        driver.quit()

    def test_go_to_filling_success(self, driver):
        driver.find_element(*BurgerLocators.BUTTON_FILLING).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(BurgerLocators.TITLE_FILLING))

        assert driver.find_element(*BurgerLocators.TITLE_FILLING).is_displayed(), "Error. The menu won't scroll."
        driver.quit()

    def test_go_to_sauce_success(self, driver):
        driver.find_element(*BurgerLocators.BUTTON_SAUCE).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(BurgerLocators.TITLE_SAUCE))

        assert driver.find_element(*BurgerLocators.TITLE_SAUCE).is_displayed(), "Error. The menu won't scroll."
        driver.quit()

    def test_go_to_buns_success(self, driver):
        driver.find_element(*BurgerLocators.BUTTON_FILLING).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(BurgerLocators.TITLE_FILLING))
        driver.find_element(*BurgerLocators.BUTTON_BUNS).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(BurgerLocators.TITLE_BUNS))

        assert driver.find_element(*BurgerLocators.TITLE_BUNS).is_displayed(), "Error. The menu won't scroll."
        driver.quit()


