# gui.py

import tkinter as tk
from tkinter import scrolledtext
from basic_ransomware import BasicRansomware
from file_manager import FileManager

# Imagem ASCII
ASCII_IMAGE = """
                       .,,uod8B8bou,,.                             
              ..,uod8BBBBBBBBBBBBBBBBRPFT?l!i:.                    
         ,=m8BBBBBBBBBBBBBBBRPFT?!||||||||||||||                   
         !...:!TVBBBRPFT||||||||||!!^^""'   ||||                   
         !.......:!?|||||!!^^""'            ||||                   
         !.........||||                     ||||                   
         !.........||||  ##                 ||||                   
         !.........||||                     ||||                   
         !.........||||                     ||||                   
         !.........||||                     ||||                   
         !.........||||                     ||||                   
         `.........||||                    ,||||                   
          .;.......||||               _.-!!|||||                   
   .,uodWBBBBb.....||||       _.-!!|||||||||!:'                    
!YBBBBBBBBBBBBBBb..!|||:..-!!|||||||!iof68BBBBBb....               
!..YBBBBBBBBBBBBBBb!!||||||||!iof68BBBBBBRPFT?!::   `.             
!....YBBBBBBBBBBBBBBbaaitf68BBBBBBRPFT?!:::::::::     `.           
!......YBBBBBBBBBBBBBBBBBBBRPFT?!::::::;:!^"`;:::       `.         
!........YBBBBBBBBBBRPFT?!::::::::::^''...::::::;         iBBbo.   
`..........YBRPFT?!::::::::::::::::::::::::;iof68bo.      WBBBBbo. 
  `..........:::::::::::::::::::::::;iof688888888888b.     `YBBBP^'
    `........::::::::::::::::;iof688888888888888888888b.     `     
      `......:::::::::;iof688888888888888888888888888888b.         
        `....:::;iof688888888888888888888888888888888899fT!        
          `..::!8888888888888888888888888888888899fT|!^"'          
            `' !!988888888888888888888888899fT|!^"'                
                `!!8888888888888888899fT|!^"'                      
                  `!988888888899fT|!^"'                            
                    `!9899fT|!^"'                                  
"""

class RansomwareSimulatorGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Simulador de Ransomware")
        self.window.geometry("900x700")
        self.window.configure(bg="black")

        self.logs = []

        # Imagem ASCII
        self.ascii_label = tk.Label(
            self.window,
            text=ASCII_IMAGE,
            font=("Courier", 8, "bold"),
            bg="black",
            fg="lime"
        )
        self.ascii_label.pack(pady=10)

        # Título
        self.title_label = tk.Label(
            self.window,
            text="Simulador de Ransomware",
            font=("Courier", 24, "bold"),
            bg="black",
            fg="lime"
        )
        self.title_label.pack(pady=20)

        # Botões
        self.encrypt_button = tk.Button(
            self.window,
            text="Criptografar Arquivos",
            command=self.encrypt_files,
            font=("Courier", 14),
            bg="black",
            fg="lime",
            activebackground="lime",
            activeforeground="black"
        )
        self.encrypt_button.pack(pady=10)

        self.decrypt_button = tk.Button(
            self.window,
            text="Descriptografar Arquivos",
            command=self.decrypt_files,
            font=("Courier", 14),
            bg="black",
            fg="lime",
            activebackground="lime",
            activeforeground="black"
        )
        self.decrypt_button.pack(pady=10)

        # Área de Logs
        self.log_area = scrolledtext.ScrolledText(
            self.window,
            wrap=tk.WORD,
            font=("Courier", 12),
            bg="black",
            fg="lime",
            width=80,
            height=20
        )
        self.log_area.pack(pady=20)

        # Criar arquivos dummy no início
        FileManager.create_dummy_files("simulated_folder")
        self.add_log("Dummy files created in 'simulated_folder'.")

    def add_log(self, message):
        self.logs.append(message)
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.see(tk.END)

    def encrypt_files(self):
        ransomware = BasicRansomware()
        logs = ransomware.encrypt_files("simulated_folder")
        for log in logs:
            self.add_log(log)

    def decrypt_files(self):
        key = "1234"  # Chave fixa para o exemplo
        ransomware = BasicRansomware()
        logs = ransomware.decrypt_files("simulated_folder", key)
        for log in logs:
            self.add_log(log)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    gui = RansomwareSimulatorGUI()
    gui.run()
