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

    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text() = 'Конструктор']")      # Кнопка Кноструктор в шапке
    BUTTON_FILLING = (By.XPATH, "//span[text() = 'Начинки']")           # Кнокпа Начинки для перемотки меню
    BUTTON_SAUCE = (By.XPATH, "//span[text() = 'Соусы']")               # Кнопка Соусы для перемотки меню
    BUTTON_BUNS = (By.XPATH, "//span[text() = 'Булки']")                # Кнопка Булки для перемотки меню

    BUTTON_ENTER = (By.XPATH, "//a[@class = 'Auth_link__1fOlj']")   # Кнопка Войти на экране регистраци
    BUTTON_ENTER_RECOVER = (By.XPATH, "//a[text() = 'Войти']")      # Кнопка войти на экране Восстановления пароля

    TITLE_CONSTRUCTOR = (By.XPATH, "//h1[text() = 'Соберите бургер']")  # Заголовок "Соберите бургер" на главной странице
    TITLE_FILLING = (By.XPATH, "//h2[text() = 'Начинки']")              # Заголовок "Начинки" в меню
    TITLE_SAUCE = (By.XPATH, "//h2[text() = 'Соусы']")                  # Заголовок "Соусы" в меню
    TITLE_BUNS = (By.XPATH, "//h2[text() = 'Булки']")                   # Заголовок "Булки" в меню
    TITLE_RECOVER = (By.XPATH, "//h2[text() = 'Восстановление пароля']")    # Заголовок "Восстановление пароля"

    LOGO_BURGERS = (By.XPATH, "//*[@id='root']/div/header/nav/div/a")   # Логотип сайта Бургер
    TEXT_DESCRIPTION = (By.XPATH, "//p[text() = 'В этом разделе вы можете изменить свои персональные данные']") # Текст описания в Личном кабинете
    TEXT_ERROR = (By.XPATH, "//p[text() = 'Некорректный пароль']")  # Сообщение об ошибке ввода пароля
    TEXT_ERROR_REGISTRATION = (By.XPATH, "//p[text() = 'Такой пользователь уже существует']")   # Сообщение об ошибке при регистрации
