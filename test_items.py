from selenium.webdriver.common.by import By

def test_add_to_basket_exists(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    assert browser.find_element(By.ID, "add_to_basket_form"), "Кнопка не найдена"
