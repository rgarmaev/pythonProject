import json
import pytest
import requests
from api import PetFriends
from requests_toolbelt.multipart.encoder import MultipartEncoder

pf = PetFriends()

def generate_string(num):
   return "x" * num


def russian_chars():
   return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def chinese_chars():
   return '的一是不了人我在有他这为之大来以个中上们'


def special_chars():
   return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'



def add_new_pet_simple(self, auth_key: json, name: str, animal_type: str, age: str) -> json:
   """Метод отправляет (постит) на сервер данные о добавляемом питомце и возвращает статус
   запроса и результат в формате JSON с данными добавленного питомца"""

   data = MultipartEncoder(
       fields={
           'name': name,
           'animal_type': animal_type,
           'age': age
       })
   headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

   res = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, data=data)
   status = res.status_code
   result = ""
   try:
       result = res.json()
   except json.decoder.JSONDecodeError:
       result = res.text
       print(result)
       return status, result

@pytest.mark.parametrize("name", [
   ''
   , generate_string(255)
   , generate_string(1001)
   , russian_chars()
   , russian_chars().upper()
   , chinese_chars()
   , special_chars()
   , '123'
], ids=[
   'empty'
   , '255 symbols'
   , 'more than 1000 symbols'
   , 'russian'
   , 'RUSSIAN'
   , 'chinese'
   , 'specials'
   , 'digit'
])
def test_add_new_pet_simple(name, animal_type='двортерьер',
                           age='4'):
   """Проверяем, что можно добавить питомца с различными данными"""

   # Добавляем питомца
   pytest.status, result = pf.add_new_pet_simple(pytest.key, name, animal_type, age)

   # Сверяем полученный ответ с ожидаемым результатом
   if name == '':
       assert pytest.status == 400
   else:
	    assert pytest.status == 200
   assert result['name'] == name
   assert result['age'] == age
   assert result['animal_type'] == animal_type