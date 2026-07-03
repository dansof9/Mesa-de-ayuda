import tkinter as tk
from backend1 import guardar_ticket

def openform(root):
    ventana = tk.Toplevel(root)
    ventana.title("nuevo ticket")
    ventana.geometry("500x500")
    ventana.resizable(True,True)
    ventana.config(bg="black")
 
    #solicitando el numero de ticket
    search = tk.Label(ventana, text="ticket number", bg="black", fg="white")
    search.pack(pady=20)

    search_input = tk.Entry(ventana)
    search_input.pack(pady=14)

    #solcitando el nombre de usuario
    user_name = tk.Label(ventana, text="User name:", bg="Black", fg="white")
    user_name.pack(pady=15)

    user_name_input = tk.Entry(ventana)
    user_name_input.pack(pady=17)

    #solicitando tipo de problema
    problem = tk.Label(ventana, text="What's your problem?", bg="black", fg="white")
    problem.pack(pady=5)
    problem_input = tk.Entry(ventana)
    problem_input.pack(pady=10)

    tk.Button(ventana,text="Guardar",command=lambda: guardar_ticket(user_name_input.get(),problem_input.get())).pack()
