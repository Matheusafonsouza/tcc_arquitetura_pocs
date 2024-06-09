class DatabasePort:
    def create(self, data: dict):
        raise NotImplementedError
    
    def update(self, data: dict):
        raise NotImplementedError
    
    def delete(self, id: int):
        raise NotImplementedError
    
    def get(self, where: dict):
        raise NotImplementedError
