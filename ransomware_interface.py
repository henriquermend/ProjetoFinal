# ransomware_interface.py

class Ransomware:
    def encrypt_files(self, directory):
        raise NotImplementedError("This method must be implemented by subclasses.")

    def decrypt_files(self, directory, key):
        raise NotImplementedError("This method must be implemented by subclasses.")
