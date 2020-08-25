class FileReader:
    def __init__(self, path):
        self.path = path

    def read(self):
        try:
            f = open(self.path)
        except FileNotFoundError:
            return ""
        else:
            f.close()
            with open(self.path) as f:
                return f.read()
