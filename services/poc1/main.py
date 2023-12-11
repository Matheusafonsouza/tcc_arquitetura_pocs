from multiprocessing import Process


class ServiceConsumer():
    def __init__(self, adapters):
        self.processes = []
        self.adapters = adapters

    def mount_processes(self):
        self.processes = [
            Process(target=adapter.start)
            for adapter in self.adapters
        ]

    def start(self):
        for process in self.processes:
            process.start()

    def stop(self):
        for process in self.processes:
            process.join()


if __name__ == "__main__":
    service = ServiceConsumer(adapters=[])
    try:
        service.start()
    except Exception:
        service.stop()
