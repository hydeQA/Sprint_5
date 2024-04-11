from selenium.webdriver.common.by import By

class BurgerLocators:
    ENTER_BUTTON_MAIN = (By.XPATH, "//button[text() = 'Войти в аккаунт']")  # Кнопка "Войти в аккаунт" на главной странице
    REGISTRATION_TITLE = (By.XPATH, "//h2[text() = 'Вход']")  # Заголовок на странице Регистрации

    REGISTRATION_LINK = (By.XPATH, "//a[text() = 'Зарегистрироваться']") # Кнопка "Зарегистрироваться"
    REGISTRATION_FIELD_NAME = (By.XPATH, "//label[text() = 'Имя']/following-sibling::input") # Поле ввода "Имя" на странице регистрации
    REGISTRATION_FIELD_EMAIL = (By.XPATH, "//label[text() = 'Email']/following-sibling::input") # Поле ввода "Email" на странице регистрации
    REGISTRATION_FIELD_PASSWORD = (By.XPATH, "//label[text() = 'Пароль']/following-sibling::input") # Поле ввода "password" на странице регистрации
    REGISTRATION_BUTTON = (By.XPATH, "//button[text() = 'Зарегистрироваться']") # Кнопка "Зарегистрироваться" на странице регистрации

    LOGIN_BUTTON = (By.XPATH, "//button[text() = 'Войти']")   # Кнопка "Войти" на странице авторизации
    EXIT_BUTTON = (By.XPATH, "//button[text() = 'Выход']")      # Кнопка "Выход" в Личном Кабинете
    ACCOUNT_BUTTON = (By.XPATH, "//p[text() = 'Личный Кабинет']")   # Кнопка "Личный Кабинет"
    RECOVER_BUTTON = (By.XPATH, "//a[text() = 'Восстановить пароль']")  # Кнопка "Восстановить пароль" на экране авторизации

    ORDER_BUTTON = (By.XPATH, "//button[text() = 'Оформить заказ']")    # Кнопка "Оформить" заказ на главной у авторизованного пользователя

