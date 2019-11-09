import time

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(5)
    btn = browser.find_elements_by_class_name("vbtn-add-to-basket")
    assert len(btn) > 0, 'Buttom not find...'
    time.sleep(3)







