import requests
import uuid

class Task:
    def __init__(self):
        self.ENDPOIN = "https://todo.pixegami.io"

    def create_task(self, payload):
        return requests.put(self.ENDPOIN + "/create-task", json=payload)
    
    def update_task(self, payload):
        return requests.put(self.ENDPOIN + "/update-task", json=payload)
    
    def get_task_id(self, task_id):
        return requests.get(self.ENDPOIN + f"/get-task/{task_id}")
    
    def list_task(self, user_id):
        return requests.get(self.ENDPOIN + f"/list-tasks/{user_id}")
    
    def get_task(self):
        return requests.get(self.ENDPOIN)
    
    def delete_task(self, user_id):
        return requests.delete(self.ENDPOIN + f"/delete-task/{user_id}")
    
    def new_task_payload(self):
        user_id = f"test_user_{uuid.uuid4().hex}"
        content = f"test_content_{uuid.uuid4().hex}"
        return {
            "content": content,
            "user_id": user_id,
            "task_id": "test_task_id",
            "is_done": False
        }