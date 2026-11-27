import requests

# 1. Вставьте сюда ваши реальные данные (в кавычках)
LOGIN = "banan.roman@bk.ru"          # Ваш логин от YouGile
PASSWORD = "Wargaming5"                # Ваш пароль от YouGile
COMPANY_ID = "0b7a09f6-2775-4b0e-8fc7-2d59e1d49067"  # Например: "44eccf40-a027-4d06-b5c2-18f4c02bb026"

# 2. Формируем запрос точно как в документации
url = "https://yougile.com/api-v2/auth/keys"
headers = {"Content-Type": "application/json"}
payload = {
    "login": LOGIN,
    "password": PASSWORD,
    "companyId": COMPANY_ID
}

# 3. Отправляем запрос
response = requests.post(url, json=payload, headers=headers)

# 4. Выводим результат
if response.status_code == 200:
    token = response.json().get("key")
    print("✅ Ваш токен успешно получен!")
    print(f"Скопируйте эту строку в файл .env как YOUGILE_TOKEN:\n{token}")
else:
    print(f"❌ Ошибка {response.status_code}: {response.text}")
    print("Проверьте правильность логина, пароля и companyId.")