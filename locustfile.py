from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def numerical_integration_task(self):
        self.client.get("/numericalintegralservice/0/3.14159")

