# Григорьева Людмила 10-я когорта — Финальный проект. Инженер по тестированию плюс
import requests
import configuration
import data

# Запрос на создание заказа

def post_new_order():

    return requests.post(configuration.URL_SERVICE + configuration.CREATE_TRACK_ORDER,
           json=data.order_body)

# Получение номера заказа
def get_order(track):

    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER,
           params={"t": track})

# Автотест
def test_create_order_and_getting_an_order_by_track():

    response = post_new_order()

    track = response.json()["track"]

    order_response = get_order(track)

    assert order_response.status_code == 200

# Григорьева Людмила 10-я когорта — Финальный проект. Инженер по тестированию плюс