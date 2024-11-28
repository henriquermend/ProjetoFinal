# basic_ransomware.py

import os
from ransomware_interface import Ransomware

class BasicRansomware(Ransomware):
    def encrypt_files(self, directory):
        print(f"Encrypting files in {directory}...")
        for filename in os.listdir(directory):
            if filename.endswith(".txt"):  # Apenas arquivos .txt
                filepath = os.path.join(directory, filename)
                try:
                    with open(filepath, "r") as file:
                        content = file.read()
                    with open(filepath, "w") as file:
                        file.write(content[::-1])  # Simula criptografia invertendo o texto
                    print(f"Encrypted: {filename}")
                except Exception as e:
                    print(f"Error encrypting {filename}: {e}")

    def decrypt_files(self, directory, key):
        print(f"Decrypting files in {directory}...")
        if key != "1234":  # Chave fictícia
            print("Invalid decryption key!")
            return
        for filename in os.listdir(directory):
            if filename.endswith(".txt"):
                filepath = os.path.join(directory, filename)
                try:
                    with open(filepath, "r") as file:
                        content = file.read()
                    with open(filepath, "w") as file:
                        file.write(content[::-1])  # Reverte o texto
                    print(f"Decrypted: {filename}")
                except Exception as e:
                    print(f"Error decrypting {filename}: {e}")
