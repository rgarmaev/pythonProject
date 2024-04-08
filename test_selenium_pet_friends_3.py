from selenium import webdriver
from selenium.webdriver.common.by import By
import re
# Инициализация браузера
driver = webdriver.Chrome()
driver.get("https://petfriends.skillfactory.ru/login")
driver.find_element(By.ID, 'email').send_keys('rgarmaev@mail.ru')
# Вводим пароль
driver.find_element(By.ID, 'pass').send_keys('xy6nY36uq6')
# Нажимаем на кнопку входа в аккаунт
driver.find_element(By.CLASS_NAME, 'btn-success').click()

# Проверяем, что мы оказались на главной странице пользователя
assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

driver.get('https://petfriends.skillfactory.ru/my_pets')

def test_pets_list():
    # Получаем список всех питомцев
    pets = driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')

    text = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]').text
    total_pets = int(re.search(r'Питомцев: (\d+)', text).group(1)) if 'Питомцев:' in text else 0
    assert len(pets) == total_pets

    # Проверяем наличие фото у половины питомцев
    pets_with_photos = 0
    for pet in pets:
        if pet.find_element(By.TAG_NAME, 'img').is_displayed():
            pets_with_photos += 1
    assert pets_with_photos >= len(pets) / 2

    # Проверяем, что у всех питомцев есть имя, возраст и порода
    for pet in pets:
        assert len(pet.find_element(By.XPATH, 'td[1]').text) > 0
        assert len(pet.find_element(By.XPATH, 'td[3]').text) > 0
        assert len(pet.find_element(By.XPATH, 'td[2]').text) > 0

    # Убеждаемся, что у всех питомцев разные имена
    pet_names = [pet.find_element(By.XPATH, 'td[1]').text for pet in pets]
    assert len(pet_names) == len(set(pet_names))

    # Проверяем, что в списке нет повторяющихся питомцев
    all_attributes = []
    for pet in pets:
        attributes = [attr.text for attr in pet.find_elements(By.TAG_NAME, 'td')]
        all_attributes.extend(attributes)

    assert len(all_attributes) == len(set(all_attributes))