from locust import HttpLocust, TaskSet, task, between
import random
import string


class UserTaskSet(TaskSet):
    def on_start(self):
        self.client.headers = {'Content-Type': 'application/json;'}

    @task(1)
    def fetch_user(self):
        self.client.get("/users/{}".format(random.randint(0, 100)))

    @task(2)
    def create_user(self):
        # ランダムに適当に名前を生成
        name = ''.join(random.choices(string.ascii_letters, k=10))
        age = random.randint(0, 80)
        self.client.post("/users?name={}&age={}".format(name, age))


class UserLocust(HttpLocust):
    task_set = UserTaskSet

    wait_time = between(0.100, 1.500)
