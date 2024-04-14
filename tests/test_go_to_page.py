import settings
from locators import BurgerLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestGoToPage:
    def test_go_to_constructor_success(self, driver):
        driver.find_element(*BurgerLocators.ENTER_BUTTON_MAIN).click()
        driver.find_element(*BurgerLocators.BUTTON_CONSTRUCTOR).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(BurgerLocators.TITLE_CONSTRUCTOR))
        assert driver.current_url == settings.URL

    def test_go_to_stellar_burgers_logo_success(self, driver):
        driver.find_element(*BurgerLocators.ENTER_BUTTON_MAIN).click()
        driver.find_element(*BurgerLocators.LOGO_BURGERS).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(BurgerLocators.TITLE_CONSTRUCTOR))
        assert driver.current_url == settings.URL

