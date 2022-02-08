import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(10)
    btn_list = browser.find_elements_by_css_selector(".btn-add-to-basket")
    assert len(btn_list) == 1, "Кнопка добовления в корзину не найдена." 