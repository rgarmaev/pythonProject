import pytest
from pages.auth_page import AuthPage

def test_authorisation(web_browser):

    page = AuthPage(web_browser)

    page.email.send_keys('rgarmaev@mail.ru')

    page.password.send_keys("xy6nY36uq6")

    page.btn.click()

    assert page.get_current_url() == 'https://petfriends.skillfactory.ru/all_pets'
