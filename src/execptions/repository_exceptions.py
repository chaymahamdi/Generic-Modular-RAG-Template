
class DatabaseConnectionError(Exception):
    def __init__(self, message: str ="Database connection error") -> None:
        self.message = message
        super().__init__(self.message)

class DocumentNotFound(Exception):
    def __init__(self, document_id):
        self.document_id = document_id
        super().__init__(f"Document {document_id} not found")
