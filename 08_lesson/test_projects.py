import pytest
from api_client import YougileAPIClient
import time

class TestProjects:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = YougileAPIClient()
        self.created_projects = []
        yield
        # Очистка после тестов
        for project_id in self.created_projects:
            try:
                self.client.delete_project(project_id)
            except:
                pass
    
    def generate_project_name(self):
        """Генерация уникального имени проекта"""
        return f"TestProject_{int(time.time())}"
    
    # POSITIVE TESTS
    
    def test_create_project_positive(self):
        """Позитивный тест создания проекта"""
        project_data = {
            "title": self.generate_project_name(),
            "description": "Test project description"
        }
        
        response = self.client.create_project(project_data)
        
        assert response.status_code == 201
        data = response.json()
        assert "id" in data
        assert data["title"] == project_data["title"]
        assert data["description"] == project_data["description"]
        
        # Сохраняем для очистки
        self.created_projects.append(data["id"])
    
    def test_get_project_positive(self):
        """Позитивный тест получения проекта"""
        # Сначала создаем проект
        project_data = {
            "title": self.generate_project_name(),
            "description": "Project for get test"
        }
        create_response = self.client.create_project(project_data)
        project_id = create_response.json()["id"]
        self.created_projects.append(project_id)
        
        # Получаем проект
        response = self.client.get_project(project_id)
        
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == project_id
        assert data["title"] == project_data["title"]
    
    def test_update_project_positive(self):
        """Позитивный тест обновления проекта"""
        # Сначала создаем проект
        project_data = {
            "title": self.generate_project_name(),
            "description": "Original description"
        }
        create_response = self.client.create_project(project_data)
        project_id = create_response.json()["id"]
        self.created_projects.append(project_id)
        
        # Обновляем проект
        update_data = {
            "title": f"{project_data['title']}_updated",
            "description": "Updated description"
        }
        response = self.client.update_project(project_id, update_data)
        
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == update_data["title"]
        assert data["description"] == update_data["description"]
    
    # NEGATIVE TESTS
    
    def test_create_project_negative_missing_title(self):
        """Негативный тест создания проекта без обязательного поля title"""
        project_data = {
            "description": "Project without title"
        }
        
        response = self.client.create_project(project_data)
        
        assert response.status_code == 400
        data = response.json()
        assert "error" in data or "message" in data
    
    def test_get_project_negative_invalid_id(self):
        """Негативный тест получения проекта с несуществующим ID"""
        invalid_id = "invalid_id_12345"
        
        response = self.client.get_project(invalid_id)
        
        assert response.status_code == 404
        data = response.json()
        assert "error" in data or "message" in data
    
    def test_update_project_negative_invalid_id(self):
        """Негативный тест обновления проекта с несуществующим ID"""
        invalid_id = "invalid_id_12345"
        update_data = {
            "title": "Updated title"
        }
        
        response = self.client.update_project(invalid_id, update_data)
        
        assert response.status_code == 404
        data = response.json()
        assert "error" in data or "message" in data
        