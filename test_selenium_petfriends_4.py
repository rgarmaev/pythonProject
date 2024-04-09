import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    # Переходим на страницу авторизации
    driver.get('https://petfriends.skillfactory.ru/login')

    yield driver

    driver.quit()


def test_show_all_pets(driver):
    # Вводим email
    driver.find_element(By.ID, 'email').send_keys('rgarmaev@mail.ru')
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys('xy6nY36uq6')
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    images = driver.find_elements(By.CSS_SELECTOR, 'div#all_my_pets > table > tbody > tr > th > img')
    names = driver.find_elements(By.CSS_SELECTOR, 'div#all_my_pets > table > tbody > tr > td')
    breeds = driver.find_elements(By.CSS_SELECTOR, 'div#all_my_pets > table > tbody > tr > td:nth-of-type(2)')
    ages = driver.find_elements(By.CSS_SELECTOR, 'div#all_my_pets > table > tbody > tr > td:nth-of-type(3)')
    print(names)
    driver.get('https://petfriends.skillfactory.ru/my_pets')

    pets_count = driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(': ')[1]
    pets_count = int(pets_count)
    print(f'количество питомцев в статистике', pets_count)
    images_count = 0
    list_names = []
    for i in range(len(names)):
        list_names.append(names[i].text)
        if images[i].get_attribute('src') != '':
            images_count += 1
        else:
            images_count += 0
        assert names[i].text != ''
        assert breeds[i].text != ''
        assert ages[i].text != ''
        print(images_count)
        if pets_count == 0:
            print("No pets")
        else:
            assert images_count / pets_count >= 0.5
    print(images_count)

    # Проверяем, что у питомцев разные имена
    set_name = set(list_names)
    assert len(set_name) == len(list_names)

