import json
import os
from tkinter import messagebox
import tkinter as tk

# BACKEND

def user_credenciales(user, password):

    usuarios = {}

    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r", encoding="utf-8") as archivo:
            try:
                usuarios = json.load(archivo)
            except json.JSONDecodeError:
                usuarios = {}

    if user in usuarios:
        return False

    usuarios[user] = password

    with open("usuarios.json", "w", encoding="utf-8") as archivo:
        json.dump(usuarios, archivo, indent=4)

    return True


def ejecutar_login(root,
                   txt_login_user,
                   txt_login_pass):
    
    user = txt_login_user.get().strip()
    password = txt_login_pass.get()


    if not user or not password:
        messagebox.showwarning("Atención", "Por favor llena todos los campos.")
        return

    usuarios = {}

    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r", encoding="utf-8") as archivo:
            try:
                usuarios = json.load(archivo)
            except json.JSONDecodeError:
                usuarios = {}

    if user in usuarios and usuarios[user] == password:

        messagebox.showinfo("Éxito", f"¡Bienvenido al sistema, {user}!")

        root.destroy()
        __import__("Screen1")

    else:
        messagebox.showerror("Error", "Credenciales incorrectas.")


def ejecutar_registro(root,
                      txt_reg_user,
                      txt_reg_pass,
                      txt_reg_confirm):
    user = txt_reg_user.get().strip()
    password = txt_reg_pass.get()
    conf = txt_reg_confirm.get()



    if not user or not password or not conf:
        messagebox.showwarning("Atención", "Todos los campos son obligatorios.")
        return

    if password != conf:
        messagebox.showerror("Error", "Las contraseñas no coinciden.")
        return

    if not user_credenciales(user, password):
        messagebox.showerror("Error", "El usuario ya existe.")
        return

    messagebox.showinfo("Éxito", "¡Usuario registrado correctamente!")

    root.destroy()
    __import__("Screen1")

    # Limpiando los campos de texto
    txt_reg_user.delete(0, tk.END)
    txt_reg_pass.delete(0, tk.END)
    txt_reg_confirm.delete(0, tk.END)




