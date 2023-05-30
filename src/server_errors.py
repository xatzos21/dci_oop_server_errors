class OK:
    def __init__(self):
        self.code = 200
        self.message = "OK"

    def status(self):
        print(f"Error {self.code}: {self.message}")


class NotFound:
    def __init__(self):
        self.code = 404
        self.message = "Not Found"

    def status(self):
        print(f"Error {self.code}: {self.message}")


class ServerError:
    def __init__(self):
        self.code = 500
        self.message = "Server Error"

    def status(self):
        print(f"Error {self.code}: {self.message}")
