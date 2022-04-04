
class NotFoundException(Exception):
    
    def __init__(self):
        self.message = f"Key not found"
        super().__init__(self.message)

    def __str__(self):
        return self.message

class ItemExistsException(Exception):
    
    def __init__(self):
        self.message = f"Key already exists"
        super().__init__(self.message)

    def __str__(self):
        return self.message