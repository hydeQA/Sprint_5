import settings
from locators import BurgerLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestGoToPage:
    def test_go_to_constructor_success(self, driver):
        driver.find_element(*BurgerLocators.ENTER_BUTTON_MAIN).click()
        driver.find_element(By.XPATH, "//p[text() = 'Конструктор']").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[text() = 'Соберите бургер']")))

        assert driver.current_url == settings.URL
        driver.quit()

    def test_go_to_stellar_burgers_logo_success(self, driver):
        driver.find_element(*BurgerLocators.ENTER_BUTTON_MAIN).click()
        driver.find_element(By.XPATH, "//*[@id='root']/div/header/nav/div/a").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[text() = 'Соберите бургер']")))

        assert driver.current_url == settings.URL
        driver.quit()

    def test_go_to_filling_success(self, driver):
        driver.find_element(By.XPATH, "//span[text() = 'Начинки']").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[text() = 'Начинки']")))

        assert driver.find_element(By.XPATH, "//h2[text() = 'Начинки']").is_displayed(), "Error. The menu won't scroll."
        driver.quit()

    def test_go_to_sauce_success(self, driver):
        driver.find_element(By.XPATH, "//span[text() = 'Соусы']").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[text() = 'Соусы']")))

        assert driver.find_element(By.XPATH, "//h2[text() = 'Соусы']").is_displayed(), "Error. The menu won't scroll."
        driver.quit()

    def test_go_to_buns_success(self, driver):
        driver.find_element(By.XPATH, "//span[text() = 'Начинки']").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[text() = 'Начинки']")))
        driver.find_element(By.XPATH, "//span[text() = 'Булки']").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[text() = 'Булки']")))

        assert driver.find_element(By.XPATH, "//h2[text() = 'Булки']").is_displayed(), "Error. The menu won't scroll."
        driver.quit()


