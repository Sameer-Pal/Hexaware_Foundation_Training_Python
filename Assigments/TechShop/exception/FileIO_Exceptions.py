# exceptions/file_io_exception.py
class FileIOException(Exception):
    def __init__(self, message="Error during file I/O operation"):
        super().__init__(message)