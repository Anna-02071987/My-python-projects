import requests
from config import Config

class YougileAPIClient:
    def __init__(self):
        self.base_url = Config.BASE_URL
        self.headers = Config.get_headers()
    
    def create_project(self, project_data):
        """Создание проекта"""
        response = requests.post(
            f"{self.base_url}/projects",
            headers=self.headers,
            json=project_data
        )
        return response
    
    def get_project(self, project_id):
        """Получение проекта по ID"""
        response = requests.get(
            f"{self.base_url}/projects/{project_id}",
            headers=self.headers
        )
        return response
    
    def update_project(self, project_id, update_data):
        """Обновление проекта"""
        response = requests.put(
            f"{self.base_url}/projects/{project_id}",
            headers=self.headers,
            json=update_data
        )
        return response
    
    def delete_project(self, project_id):
        """Удаление проекта (для очистки)"""
        response = requests.delete(
            f"{self.base_url}/projects/{project_id}",
            headers=self.headers
        )
        return response
        