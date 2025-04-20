class GroupLimitError(Exception):
    def __init__(self, message, current_count):
        super().__init__(message)
        self.current_count = current_count
