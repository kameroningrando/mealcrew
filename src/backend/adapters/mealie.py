import httpx


class MealieAdapter:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key
        self.headers = {"accept": "application/json"}

    def get_version(self):
        response = httpx.get(
            url=f"https://{self.base_url}/api/app/about", headers=self.headers
        )

        return response.json()

    def get_recipes(self):
        self.headers["Authorization"] = f"Bearer {self.api_key}"

        response = httpx.get(
            url=f"https://{self.base_url}/api/recipes", headers=self.headers
        )

        return response.json()
