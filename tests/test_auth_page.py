import pickle
from pages.auth_page import AuthPage


def test_authorisation(web_browser):
    page = AuthPage(web_browser)

    page.email.send_keys('rgarmaev@mail.ru')
    page.password.send_keys("xy6nY36uq6")
    page.btn.click()

    # Получаем cookies из текущего веб-драйвера страницы
    cookies = web_browser.get_cookies()

    # Сохраняем cookies в файл с помощью pickle
    with open('my_cookies.txt', 'wb') as cookies_file:
        pickle.dump(cookies, cookies_file)

    # Проверяем текущий URL после аутентификации
    assert page.get_current_url() == 'https://petfriends.skillfactory.ru/all_pets'




