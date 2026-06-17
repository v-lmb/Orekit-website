from locust import HttpUser, task, between


class TleApiUser(HttpUser):
    host = "http://localhost:8001"
    wait_time = between(1, 3)

    @task(1)
    def health(self):
        """Load test for /health endpoint, weight 1"""
        self.client.get("/health")

    @task(3)
    def get_all_tle(self):
        """Load test for /api/tle endpoint, weight 3"""
        self.client.get("/api/tle")

    @task(3)
    def get_tle_by_id(self):
        """Load test for /api/tle/{satellite_id} endpoint, weight 3"""
        self.client.get("/api/tle/25544")

    @task(1)
    def get_tle_not_found(self):
        """verifies that the API handles errors properly under load, weight 1"""
        with self.client.get("/api/tle/99999999999", catch_response=True) as resp:
            if resp.status_code == 404:
                resp.success()
