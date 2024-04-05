import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # Для Chrome

def test_petfriends(web_browser):
    # Open PetFriends base page:
    web_browser.get("https://petfriends.skillfactory.ru/")

    time.sleep(2)  # just for demo purposes, do NOT repeat it on real projects!

    # click on the new user button
    btn_newuser = web_browser.find_element(By.XPATH,"//button[@onclick=\"document.location='/new_user';\"]")

    btn_newuser.click()

    # click existing user button
    btn_exist_acc = web_browser.find_element(By.LINK_TEXT,u"У меня уже есть аккаунт")
    btn_exist_acc.click()

    # add email
    field_email = web_browser.find_element(By.ID,"email")
    field_email.clear()
    field_email.send_keys("rgarmaev@mail.ru")

    # add password
    field_pass = web_browser.find_element(By.ID,"pass")
    field_pass.clear()
    field_pass.send_keys("xy6nY36uq6")

    # click submit button
    btn_submit = web_browser.find_element(By.XPATH,"//button[@type='submit']")
    btn_submit.click()

    time.sleep(3)  # just for demo purposes, do NOT repeat it on real projects!
    if web_browser.current_url == 'https://petfriends.skillfactory.ru/all_pets':
        # Make the screenshot of browser window:
        web_browser.save_screenshot('result_petfriends.png')
    else:
        raise Exception("login error")