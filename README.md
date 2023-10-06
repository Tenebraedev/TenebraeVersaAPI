# TenebraeVersaAPI

TenebraeVersaAPI - это API для получения случайных данных, таких как изображения животных, случайные числа, цвета и многое другое. API предоставляет доступ через токены авторизации и поддерживает несколько функций для получения различных данных.

## Установка и использование

1. Клонируйте репозиторий:

```bash
git clone https://github.com/Tenebraedev/TenebraeVersaAPI.git
```
## Установите зависимости:
```python
pip install flask
```
Создайте файл user_token.json с данными пользователей и их API ключами.</br>
Пример файла user_token.json:

```json
[
    {
        "id": 1,
        "api_key": "your_api_key_here"
    },
    {
        "id": 2,
        "api_key": "another_api_key_here"
    }
]
```
## Запустите приложение:
```bash
python app.py
```
## Доступные методы API
GET /api/v1/random_fox: Получение случайного изображения с лисой.
GET /api/v1/random_dog: Получение случайного изображения с собакой.
GET /api/v1/random_cat: Получение случайного изображения с котами.
GET /api/v1/random_numbers: Получение случайных чисел в заданном диапазоне.
GET /api/v1/random_color: Получение случайного цвета в указанном формате.
GET /api/v1/generate_password: Генерация случайного пароля.
GET /api/v1/check_website: Проверка доступности веб-сайта по URL.
## Авторизация
Для доступа к API необходимо передавать заголовок Authorization с токеном авторизации в формате Bearer:
```makefile
Authorization: Bearer your_api_key_here
```
## UI
API также предоставляет простой интерфейс пользователя (UI) для некоторых методов, доступных по следующим URL:

/api/v1/randomphotofox: Получение случайного фото лисы.
/api/v1/randomphotodog: Получение случайного фото собаки.
/api/v1/randomphotocat: Получение случайного фото кота.
/api/v1/randomnumber: Получение случайного числа.
/api/v1/randomcolor: Получение случайного цвета.
/api/v1/password: Генерация случайного пароля.
/api/v1/websitecheck: Проверка доступности веб-сайта.
