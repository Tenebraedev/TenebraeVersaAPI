import os
import json
import random
from flask import Flask, render_template, jsonify, send_from_directory, url_for, request
from datetime import datetime
import string
import requests

app = Flask(__name__)

# Заголовок авторизации
AUTH_HEADER = "Authorization"

# Загрузка данных пользователей и их API ключей из JSON файла
with open("user_token.json", "r") as f:
    API_KEY = json.load(f)

# Путь к папке с фотографиями
media_folder_fox = "static/animals/fox/"
media_folder_dog = "static/animals/dog/"
media_folder_cat = "static/animals/cat/"
existing_numbers = set()  # Сюда будем добавлять сгенерированные числа

# Получение случайного медиафайла с лисой
@app.route('/api/v1/random_fox', methods=['GET'])
def random_fox():
    # Получение строки авторизации из заголовка Authorization
    auth_header = request.headers.get('Authorization')
    if auth_header and auth_header.startswith("Bearer "):
        auth_key = auth_header.split(" ")[1]
        for user in API_KEY:
            if user["api_key"] == auth_key:
                random_media_file = random.choice(os.listdir(media_folder_fox))
                media_url = f'/static/animals/fox/{random_media_file}'
                return jsonify({"url": media_url})
        return jsonify({"error": "Unauthorized"}), 401
    else:
        return jsonify({"error": "Unauthorized"}), 401

# Получение случайного медиафайла с собакой
@app.route('/api/v1/random_dog', methods=['GET'])
def random_dog():
    auth_header = request.headers.get('Authorization')
    if auth_header and auth_header.startswith("Bearer "):
        auth_key = auth_header.split(" ")[1]
        for user in API_KEY:
            if user["api_key"] == auth_key:
                random_media_file = random.choice(os.listdir(media_folder_dog))
                media_url = f'/static/animals/dog/{random_media_file}'
                return jsonify({"url": media_url})
        return jsonify({"error": "Unauthorized"}), 401
    else:
        return jsonify({"error": "Unauthorized"}), 401

# Получение случайного медиафайла с котами 
@app.route('/api/v1/random_cat', methods=['GET'])
def random_cat():
    auth_header = request.headers.get('Authorization')
    if auth_header and auth_header.startswith("Bearer "):
        auth_key = auth_header.split(" ")[1]
        for user in API_KEY:
            if user["api_key"] == auth_key:
                random_media_file = random.choice(os.listdir(media_folder_cat))
                media_url = f'/static/animals/cat/{random_media_file}'
                return jsonify({"url": media_url})
        return jsonify({"error": "Unauthorized"}), 401
    else:
        return jsonify({"error": "Unauthorized"}), 401

@app.route('/api/v1/random_numbers', methods=['GET'])
def random_numbers():
    auth_header = request.headers.get('Authorization')
    if auth_header and auth_header.startswith("Bearer "):
        auth_key = auth_header.split(" ")[1]
        for user in API_KEY:
            if user["api_key"] == auth_key:
                min_num = int(request.args.get('minnum'))
                max_num = int(request.args.get('maxnum'))
                count_num = int(request.args.get('countnum', 1))
                random_nums = []

                try:
                    while len(random_nums) < count_num:
                        new_num = random.randint(min_num, max_num)
                        if new_num not in existing_numbers:
                            existing_numbers.add(new_num)
                            random_nums.append(new_num)
                except Exception as e:
                    return jsonify({"error": str(e)}), 500  # Обработка ошибки генерации чисел

                media_url = random_nums
                # Очистка множества для будущих генераций
                existing_numbers.clear()
                
                return jsonify({"numbers": random_nums})
        return jsonify({"error": "Unauthorized"}), 401
    else:
        return jsonify({"error": "Unauthorized"}), 401


def generate_random_color(format='hex'):
    if format == 'hex':
        color = "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    elif format == 'rgb':
        color = "{}, {}, {}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    else:
        return {"error": "Invalid format specified"}

    return color

@app.route('/api/v1/random_color', methods=['GET'])
def get_random_color():
    auth_header = request.headers.get('Authorization')
    if auth_header and auth_header.startswith("Bearer "):
        auth_key = auth_header.split(" ")[1]
        for user in API_KEY:
            if user["api_key"] == auth_key:
                color_format = request.args.get('format', 'hex')
                color = generate_random_color(color_format)
                return jsonify({"color": color})
        return jsonify({"error": "Unauthorized"}), 401
    else:
        return jsonify({"error": "Unauthorized"}), 401

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/api/v1/generate_password', methods=['GET'])
def generate_password():
    auth_header = request.headers.get('Authorization')
    if auth_header and auth_header.startswith("Bearer "):
        auth_key = auth_header.split(" ")[1]
        for user in API_KEY:
            if user["api_key"] == auth_key:
                length = int(request.args.get('length', default=12))
                password = generate_random_password(length)
                return jsonify({"password": password})
        return jsonify({"error": "Unauthorized"}), 401
    else:
        return jsonify({"error": "Unauthorized"}), 401

# Функция для проверки доступности веб-сайта
def check_website_availability(website_url):
    try:
        response = requests.get(website_url)
        if response.status_code == 200:
            return "Online"
        else:
            return "Offline"
    except:
        return "Offline"

# Маршрут для проверки доступности веб-сайта
@app.route('/api/v1/check_website', methods=['GET'])
def check_website():
    auth_header = request.headers.get('Authorization')
    if auth_header and auth_header.startswith("Bearer "):
        auth_key = auth_header.split(" ")[1]
        for user in API_KEY:
            if user["api_key"] == auth_key:
                website_url = request.args.get('url')
                if website_url:
                    status = check_website_availability(website_url)
                    return jsonify({"status": status})
                else:
                    return jsonify({"error": "Invalid website URL"}), 400
        return jsonify({"error": "Unauthorized"}), 401
    else:
        return jsonify({"error": "Unauthorized"}), 401


# Отображение UI
@app.route('/api/v1/randomphotofox', methods=['GET'])
def randomfoxs():
    return render_template('randomphotofox.html')

@app.route('/api/v1/randomphotodog', methods=['GET'])
def randomdogs():
    return render_template('randomphotodog.html')

@app.route('/api/v1/randomphotocat', methods=['GET'])
def randompcats():
    return render_template('randomphotocat.html')

@app.route('/api/v1/randomnumber', methods=['GET'])
def randomnumber():
    return render_template('randomnum.html')

@app.route('/api/v1/randomcolor', methods=['GET'])
def randomcolor():
    return render_template('randomcolor.html')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/api/v1/password', methods=['GET'])
def privacy_policy():
    return render_template('generate_password.html')

@app.route('/api/v1/websitecheck', methods=['GET'])
def checkweb():
    return render_template('checkweb.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
