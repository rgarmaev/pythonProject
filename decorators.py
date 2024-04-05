from settings import valid_email, valid_password
import requests
import pytest
from datetime import datetime
@pytest.fixture(scope="class")

def get_key(request):
    # переменные email и password нужно заменить своими учетными данными
    response = requests.post(url='https://petfriends.skillfactory.ru/login',
                             data={"email": valid_email, "pass": valid_password})
    assert response.status_code == 200, 'Запрос выполнен неуспешно'
    assert 'Cookie' in response.request.headers, 'В запросе не передан ключ авторизации'
    print("\nreturn auth_key")
    return response.request.headers.get('Cookie')


@pytest.fixture(autouse=True)
def request_fixture(request):
    if 'Pets' in request.function.__name__:
        print(f"\nЗапущен тест из сьюта Дом Питомца: {request.function.__name__}")




