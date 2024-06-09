class AMQPPort:
    def send_message(self, message: dict):
        raise NotImplementedError
    
    def receive_messages(self):
        raise NotImplementedError
