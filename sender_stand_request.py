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