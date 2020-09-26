import time


LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_login_link(browser):
    browser.get(LINK)
    browser.find_element_by_css_selector("button.btn.btn-lg.btn-primary.btn-add-to-basket")
    time.sleep(10)
