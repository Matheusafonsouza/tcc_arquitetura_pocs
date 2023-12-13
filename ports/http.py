class HTTPPort:
    def __init__(self, base_url: str):
        self.base_url = base_url
    
    def request(self, method: str, route: str, data: dict = None):
        raise NotImplementedError
    
    def get(self, route: str):
        raise NotImplementedError
    
    def post(self, route: str, data: str):
        raise NotImplementedError
    
    def put(self, route: str, data: str):
        raise NotImplementedError
    
    def delete(self, route: str):
        raise NotImplementedError
    
    def patch(self, route: str, data: str):
        raise NotImplementedError
