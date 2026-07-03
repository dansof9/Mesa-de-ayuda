import os
import json
from tkinter import messagebox

#Creando función para almacenar los tickets en JSON
def almacenar_en_json(ID, user, issue, priority):
    if user == "" or ID == "" or issue == "" or priority == "":
        messagebox.showerror("Campos Incompletos", "Debe completar todos los campos") 
        return

    datos = {
        "ID" : ID,
        "User" : user,
        "Issue": issue,
        "Priority": priority
    }
#proceso para guardar
    tickets_guardados = [] 
#Leyendo los tickets en JSON
    if os.path.exists("tickets.json"):
        with open("tickets.json", "r", encoding="utf-8") as f:
            try:
                tickets_guardados = json.load(f)
            except json.JSONDecodeError: 
                tickets_guardados = []

    tickets_guardados.append(datos) 

#escribeindo en el archivo JSON
    with open("tickets.json", "w", encoding="utf-8") as f:
        json.dump(tickets_guardados, f, indent=4, ensure_ascii=False)

# NUEVA FUNCIÓN: Sirve para que tu interfaz pueda pedirle los datos al backend
def obtener_tickets():
    if not os.path.exists("tickets.json"):
        return []
    with open("tickets.json", "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []
