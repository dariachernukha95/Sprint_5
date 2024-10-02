from selenium.webdriver.common.by import By

class Locators:
    # Кнопка Войти в аккаунт/Оформить заказ на главной странице
    LOGIN_INTO_ACCOUNT_BUTTON = (By.XPATH, "//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")
    # Кнопка Зарегистрироваться на странице входа в аккаунт
    REGISTER_BUTTON = (By.CSS_SELECTOR, "a.Auth_link__1fOlj")
    # Поле ввода Имя в форме
    INPUT_FIELD_NAME = (By.XPATH, "//label[text() = 'Имя']/parent::div/input")
    # Поле ввода Email в форме
    INPUT_FIELD_EMAIL = (By.XPATH, "//label[text() = 'Email']/parent::div/input")
    # Поле ввода Имя в форме
    INPUT_FIELD_PASSWORD = (By.XPATH, "//label[text() = 'Пароль']/parent::div/input")
    # Кнопка Зарегистрироваться в форме регистрации
    REGISTRATION_BUTTON = (By.XPATH, "//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
    # Заголовок формы Вход
    LOG_IN_FORM_HEADER = (By.CSS_SELECTOR, "h2")
    # Кнопка Войти на странице входа в аккаунт
    LOGIN_BUTTON = (By.XPATH,"//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
    # Кнопка Войти на странице регистрации/восстановления пароля
    LOGIN_BUTTON_ON_REGISTRATION_PAGE = (By.CSS_SELECTOR, "a.Auth_link__1fOlj")
    # Текст об ошибке Некорректный пароль
    INVALID_PASSWORD_TEXT = (By.CSS_SELECTOR, "p.input__error.text_type_main-default")
    # Кнопка Личный кабинет на главной странице
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text() = 'Личный Кабинет']")
    # Кнопка Восстановить пароль
    CHANGE_PASSWORD_BUTTON = (By.XPATH,"//a[@class = 'Auth_link__1fOlj']")
    # Кнопка Выйти на странице личного кабинета
    LOGOUT_BUTTON = (By.XPATH, "//button[@class = 'Account_button__14Yp3 text text_type_main-medium text_color_inactive']")
    # Текст на странице профиля "В этом разделе вы можете изменить свои персональные данные"
    DESCRIPTION_OF_PROFILE_PAGE = (By.XPATH, "//p[text() = 'В этом разделе вы можете изменить свои персональные данные']")
    # Кнопка Конструктор в шапке страницы
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text() = 'Конструктор']")
    # Заголовок Соберите бургер
    MAKE_BURGER_HEADER = (By.XPATH, "//h1[text() = 'Соберите бургер']")
    # Логотип Stellar Burgers
    STELLAR_BURGERS_LOGO = (By.XPATH, "//div[@class = 'AppHeader_header__logo__2D0X2']")
    # Вкладка Соусы
    SAUCE_PAGE = (By.XPATH, "//span[text() = 'Соусы']")
    # Вкладка Булки
    BUN_PAGE = (By.XPATH, "//span[text() = 'Булки']")
    # Вкладка Начинки
    FILLING_PAGE = (By.XPATH, "//span[text() = 'Начинки']")
    # Активная вкладка
    ACTIVE_PAGE = (By.XPATH, "//div[@class = 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")