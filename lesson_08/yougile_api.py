"""Клиент для взаимодействия с YouGile API v2 (паттерн PageObject)."""
import os
import requests
from typing import Dict, Any
from dotenv import load_dotenv

# Загружаем переменные из файла .env
load_dotenv()


class YougileAPI:
    def __init__(self):
        self.base_url = os.getenv(
            "YOUGILE_BASE_URL", "https://yougile.com/api-v2"
        )
        self.token = os.getenv("YOUGILE_TOKEN")
        self.user_id = os.getenv("YOUGILE_USER_ID")

        if not self.token:
            raise ValueError(
                "Переменная окружения YOUGILE_TOKEN не установлена"
            )
        if not self.user_id:
            raise ValueError(
                "Переменная окружения YOUGILE_USER_ID не установлена"
            )

        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

    def create_project(self, payload: Dict[str, Any]) -> requests.Response:
        return requests.post(
            f"{self.base_url}/projects", json=payload, headers=self.headers
        )

    def get_project(self, project_id: str) -> requests.Response:
        return requests.get(
            f"{self.base_url}/projects/{project_id}", headers=self.headers
        )

    def update_project(
        self, project_id: str, payload: Dict[str, Any]
    ) -> requests.Response:
        return requests.put(
            f"{self.base_url}/projects/{project_id}",
            json=payload,
            headers=self.headers
        )

    def delete_project(self, project_id: str) -> requests.Response:
        return requests.delete(
            f"{self.base_url}/projects/{project_id}", headers=self.headers
        )
