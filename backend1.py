import os
import json
from tkinter import messagebox

#Almacenado los tickets en un archivo JSON
def almacenar_en_json(user, issue, priority):

    if user == "" or issue == "":
        messagebox.showerror("Campos Incompletos", "Debe completar todos los campos") 
        return False

    tickets_guardados = [] 
    
    #Leyendo los tickets en JSON primero para saber cuál será el siguiente ID
    if os.path.exists("tickets.json"):
        with open("tickets.json", "r", encoding="utf-8") as f:
            try:
                tickets_guardados = json.load(f)
            except json.JSONDecodeError: 
                tickets_guardados = []

    # Generando ID automático consecutivo, se continua un orden numerico.
    if tickets_guardados:
        ultimo_id = tickets_guardados[-1].get("ID", 0)
        nuevo_id = ultimo_id + 1
    else:
        nuevo_id = 1

    #Datos que se almacenan
    datos = {
        "ID": nuevo_id,
        "User" : user,
        "Issue": issue,
        "Priority": priority
    }

    #ACTUALIZAR
    tickets_guardados.append(datos) 

    # Escribiendo en el archivo JSON
    with open("tickets.json", "w", encoding="utf-8") as f:
        json.dump(tickets_guardados, f, indent=4, ensure_ascii=False)

    messagebox.showinfo("Ticket Creado", f"El ticket #{nuevo_id:03d} se ha registrado con éxito.")
    return True


# obteniendo de JSON
def obtener_tickets():
    if not os.path.exists("tickets.json"):
        return []
    with open("tickets.json", "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []
