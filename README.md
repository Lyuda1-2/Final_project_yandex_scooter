Тесты на проверку параметра name в поле запроса на создание набора с продуктами для авторизованного пользователя в Яндекс.Прилавке с помощью API Яндекс.Прилавок.
- Для запуска тестов должны быть установлены пакеты pytest и requests
- Запуск всех тестов выполянется командой pytest

В работе с БД были выполнены следующие запросы: 

1 задание) SELECT c. login, COUNT(o. id) AS "deliveryCount" FROM "Couriers" AS c LEFT JOIN "Orders" AS o ON c.id = o."courierId" WHERE o."inDelivery" = true GROUP BY c.login;

2 заданиие) SELECT track, CASE WHEN finished = true THEN 2 WHEN cancelled = true THEN -1 WHEN "inDelivery" = true THEN 1 ELSE 0 END AS status FROM "Orders";
