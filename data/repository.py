class Repository:
    def __init__(self):
        self.data = []
        self.seen = set()

    def add(self, record):
        if record and record.name not in self.seen:
            self.data.append(record)
            self.seen.add(record.name)