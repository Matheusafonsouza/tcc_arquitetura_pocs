class HTTPPort:
    def __init__(self, base_url) -> None:
        self.base_url = base_url
    
    def request(self, method, route, data=None):
        raise NotImplementedError
    
    def get(self, route):
        raise NotImplementedError
    
    def post(self, route, data):
        raise NotImplementedError
    
    def put(self, route, data):
        raise NotImplementedError
    
    def delete(self, route):
        raise NotImplementedError
    
    def patch(self, route, data):
        raise NotImplementedError
