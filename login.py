import tkinter as tk
from tkinter import messagebox
import backend_login


# VENTANA PRINCIPAL DE BIENVENIDA (LAS 2 OPCIONES)
root = tk.Tk()
root.title("Bienvenido al sistema")
root.state("zoomed")
root.resizable(True, True)
root.config(bg="#FFFFFF")

# Frame central que contiene las opciones de bienvenida
frame_opciones = tk.Frame(root, bg="#FFFFFF", width=450, height=350, bd=2, relief="solid")
frame_opciones.place(relx=0.5, rely=0.5, anchor="center")
frame_opciones.pack_propagate(False)

tk.Label(frame_opciones, text="¡BIENVENIDO!", font=("Arial", 22, "bold"), bg="#FFFFFF", fg="Black").pack(pady=(40, 20))
tk.Label(frame_opciones, text="Selecciona una opción para continuar", font=("Arial", 11), bg="#FFFFFF", fg="#1B1A1A").pack(pady=(0, 40))

# Funciones para abrir los formularios ocultando la ventana de opciones
def abrir_login():
 frame_opciones.place_forget()
 frame_login.place(relx=0.5, rely=0.5, anchor="center")

def abrir_registro():
 frame_opciones.place_forget()
 frame_registro.place(relx=0.5, rely=0.5, anchor="center")

def regresar_al_menu():
 frame_login.place_forget()
 frame_registro.place_forget()
 frame_opciones.place(relx=0.5, rely=0.5, anchor="center")

# Los dos botones principales en la pantalla de inicio
btn_opcion_login = tk.Button(frame_opciones, text="LOG IN", font=("Arial", 12, "bold"), bg="#1877f2", fg="white", width=20, bd=2, command=abrir_login)
btn_opcion_login.pack(pady=10, ipady=5)

btn_opcion_signup = tk.Button(frame_opciones, text="SIGN UP", font=("Arial", 12, "bold"), bg="#42b72a", fg="white", width=20, bd=2, command=abrir_registro)
btn_opcion_signup.pack(pady=10, ipady=5)

# VENTANA INTERNA: LOGIN
frame_login = tk.Frame(root, bg="#ffffff", width=400, height=500, bd=1, relief="solid")
frame_login.pack_propagate(False)

tk.Label(frame_login, text="Iniciar Sesión", font=("Arial", 18, "bold"), bg="#ffffff").pack(pady=30)
tk.Label(frame_login, text="Usuario", bg="#ffffff").pack(anchor="w", padx=40)
txt_login_user = tk.Entry(frame_login, font=("Arial", 12), bd=1, relief="solid")
txt_login_user.pack(fill="x", padx=40, pady=5, ipady=3)

tk.Label(frame_login, text="Contraseña", bg="#ffffff").pack(anchor="w", padx=40)
txt_login_pass = tk.Entry(frame_login, font=("Arial", 12), show="*", bd=1, relief="solid")
txt_login_pass.pack(fill="x", padx=40, pady=5, ipady=3)

btn_enviar_login = tk.Button(frame_login, text="Ingresar", bg="#1877f2", fg="white", font=("Arial", 11, "bold"), bd=0)
btn_enviar_login.pack(fill="x", padx=40, pady=25, ipady=5)

tk.Button(frame_login, text="← Volver al inicio", font=("Arial", 9), bg="#ffffff", fg="gray", bd=0, command=regresar_al_menu).pack(pady=10)

# VENTANA INTERNA: SIGN UP
frame_registro = tk.Frame(root, bg="#ffffff", width=400, height=500, bd=1, relief="solid")
frame_registro.pack_propagate(False)

tk.Label(frame_registro, text="Crear Cuenta", font=("Arial", 18, "bold"), bg="#ffffff").pack(pady=20)
tk.Label(frame_registro, text="Usuario Nuevo", bg="#ffffff").pack(anchor="w", padx=40)
txt_reg_user = tk.Entry(frame_registro, font=("Arial", 12), bd=1, relief="solid")
txt_reg_user.pack(fill="x", padx=40, pady=5, ipady=3)

tk.Label(frame_registro, text="Contraseña", bg="#ffffff").pack(anchor="w", padx=40)
txt_reg_pass = tk.Entry(frame_registro, font=("Arial", 12), show="*", bd=1, relief="solid")
txt_reg_pass.pack(fill="x", padx=40, pady=5, ipady=3)

tk.Label(frame_registro, text="Confirmar Contraseña", bg="#ffffff").pack(anchor="w", padx=40)
txt_reg_confirm = tk.Entry(frame_registro, font=("Arial", 12), show="*", bd=1, relief="solid")
txt_reg_confirm.pack(fill="x", padx=40, pady=5, ipady=3)

btn_enviar_registro = tk.Button(frame_registro, text="Registrarse", bg="#42b72a", fg="white", font=("Arial", 11, "bold"), bd=0)
btn_enviar_registro.pack(fill="x", padx=40, pady=25, ipady=5)

tk.Button(frame_registro, text="← Volver al inicio", font=("Arial", 9), bg="#ffffff", fg="gray", bd=0, command=regresar_al_menu).pack(pady=10)


import backend_login
btn_enviar_login.config(
    command=lambda: backend_login.ejecutar_login(
        root,
        txt_login_user,
        txt_login_pass
    )
)
btn_enviar_registro.config(
    command=lambda: backend_login.ejecutar_registro(
        root,
        txt_reg_user,
        txt_reg_pass,
        txt_reg_confirm
    )
)
root.mainloop()
