import sender_stand_request

# Сохранение номера заказа
def get_track_of_order():

    track = sender_stand_request.post_new_order()

    return track.json()["track"]

# Запрос на получения заказа по треку заказа
def test_create_and_track_order():

    track = get_track_of_order()

    get_response = sender_stand_request.get_order(track)
# Проверка, что код ответа равен 200
    assert get_response.status_code == 200