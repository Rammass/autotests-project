from .pages.login_page import LoginPage


LINK = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"


def test_login_page(browser):
    browser.get(LINK)
    page = LoginPage(browser, LINK)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.should_be_login_page()  # выполняем метод страницы - переходим на страницу логина

