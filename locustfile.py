# locustfile.py
from locust import HttpUser, task, between


class RecargaUser(HttpUser):
    wait_time = between(0.1, 0.5)

    @task(3)
    def recarga_normal(self):
        self.client.get("/recarga?monto=10000&premium=false")

    @task(2)
    def recarga_premium(self):
        self.client.get("/recarga?monto=30000&premium=true")

    @task(1)
    def recarga_minima(self):
        self.client.get("/recarga?monto=1000&premium=false")