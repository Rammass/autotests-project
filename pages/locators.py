from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM_ID = (By.ID, "login_form")
    REGISTRATION_FORM_ID = (By.ID, "register_form")
    LOGIN_URL = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
