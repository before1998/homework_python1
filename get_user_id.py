import requests
import json

TOKEN = "eGKDc_xzz3hRd9taGOn6IMRhIFdIfxJs4spfBhUENlfpC9_KYXjEWn5zUDzna_W4"

url = "https://yougile.com/api-v2/users"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {TOKEN}"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print("✅ Ответ получен. Вот его полная структура:")
    print("=" * 50)
    # Выводим красиво с отступами
    print(json.dumps(data, indent=2, ensure_ascii=False))
    print("=" * 50)
else:
    print(f"❌ Ошибка {response.status_code}: {response.text}")