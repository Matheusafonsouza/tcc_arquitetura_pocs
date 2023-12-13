import requests

from ports.http import HTTPPort


class HTTPRequestAdapter(HTTPPort):
    def request(self, method: str, route: str, data: dict = None):
        try:
            response = requests.request(
                method,
                f"{self.base_url}{route}",
                data=data
            )
            response.raise_for_status()
            return {
                "status_code": response.status_code,
                "content": response.json(),
            }
        except (
            requests.exceptions.ConnectionError,
            requests.exceptions.Timeout,
            requests.exceptions.RequestException,
        ) as e:
            return {
                "status_code": 500,
                "content": {
                    "message": str(e),
                }
            }
        except requests.exceptions.HTTPError as e:
            return {
                "status_code": response.status_code,
                "content": {
                    "message": str(e),
                }
            }

    def get(self, route: str):
        return self.request("GET", route)
    
    def post(self, route: str, data: dict):
        return self.request("POST", route, data=data)
    
    def put(self, route: str, data: dict):
        return self.request("PUT", route, data=data)
    
    def delete(self, route: str):
        return self.request("DELETE", route)
    
    def patch(self, route: str, data: dict):
        return self.request("PATCH", route, data=data)
