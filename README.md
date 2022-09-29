# Тестовое API для работы с платежной системой (Stripe) [https://stripe.com/]


## Сделано:
    - Создал модель Item с полями (name, description, price)
    - Создал API (api/v1) с методам GET:
        - endpoint /api/v1/buy/{Item_id}. При выполнении запроса к этому endpint, c помощью python библиотеки stripe выполняется запрос stripe.checkout.Session.create(...) для получения id сессии. Ответ - {str: stripe_session_id}
        - endpoint /api/v1/item/{Item_id}. При выполнении запроса к этому endpoint, возвращается HTML страница, на которой будет информация о выбранном Item и кнопка "Купить". По нажатию на кнопку "Купить" происходит запрос на endpoint endpoint /api/v1/buy/{Item_id}, а полученый в отвтете stripe_session_id, с помощью JavaScript библиотеки Stripe происходить редирект на Checkout форму

![image](https://user-images.githubusercontent.com/75985452/193028321-0220e05b-2580-4220-a114-a1f0a799658e.png)

