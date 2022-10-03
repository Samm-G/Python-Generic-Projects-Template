class GenericException(Exception):
    def __init__(
        self, message: str = "This is a dummy exception, definition is not valid."
    ):
        self.message = message
        super().__init__(self.message)
