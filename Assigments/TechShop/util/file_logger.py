# # util/file_logger.py
# import os
# from exception.file_io_exception import FileIOException

# class FileLogger:
#     @staticmethod
#     def log_to_file(filename: str, message: str):
#         try:
#             # Check if the directory exists; if not, create it
#             os.makedirs(os.path.dirname(filename), exist_ok=True)
            
#             # Open the file in append mode and write the log message
#             with open(filename, 'a') as file:
#                 file.write(message + "\n")
#         except IOError as e:
#             # Raise custom file I/O exception if there's an issue
#             raise FileIOException(f"Failed to log to file: {filename}. Error: {str(e)}")


# # main/main_module.py
# from util.file_logger import FileLogger
# from exception.file_io_exception import FileIOException

# def main():
#     try:
#         # Example of logging an event
#         FileLogger.log_to_file("logs/app.log", "Application started successfully.")
#         print("Log entry created.")
#     except FileIOException as e:
#         # Handle the file I/O exception
#         print(f"Logging failed: {e}")
#         # Optionally, log this error to a different place or take alternative action

# if __name__ == "__main__":
#     main()


# Smjhna hai 