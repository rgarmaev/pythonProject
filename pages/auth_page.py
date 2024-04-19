from pages.base import WebPage
from pages.elements import WebElement
import pickle

class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://petfriends.skillfactory.ru/login'
        super().__init__(web_driver, url)

    email = WebElement(id='email')
    password = WebElement(id='pass')
    btn = WebElement(class_name='btn.btn-success')

    def login(self, user_email, user_password):
        self.email.send_keys(user_email)
        self.password.send_keys(user_password)
        self.btn.click()

        # После успешной аутентификации сохраняем cookies в файл
        cookies = self.web_driver.get_cookies()
        with open('my_cookies.txt', 'wb') as cookies_file:
            pickle.dump(cookies, cookies_file)
    
    


