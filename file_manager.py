# file_manager.py

import os

class FileManager:
    @staticmethod
    def create_dummy_files(directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
        for i in range(5):
            filepath = os.path.join(directory, f"file{i}.txt")
            with open(filepath, "w") as file:
                file.write(f"Dummy content {i}")
