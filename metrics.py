class Metrics:

    def __init__(self):
        self.requests = 0

    def record(self):
        self.requests += 1

    def get(self):
        return self.requests
