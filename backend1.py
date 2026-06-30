import os
from tkinter import messagebox
import os
import json


#Creando los tickets.


def almacenar_en_json (ID, user, issue):
 

    if user == "" or ID == "" or issue == "":
        messagebox.showerror("Campos Incomletos", "Debe completar todos los campos") 
        return

    datos = {
        "ID" : ID,
        "User" : user,
        "Issue": issue
    }

  #INCORPORANDO JSON Y LEYENDO SI YA EXISTEN LOS TICKETS
    tickets_guradados =[] 

    if os.path.exists("tickets.json"):
     with open("tickets.json", "r" , encoding="utf-8") as f:
        try:

            tickets_guardados = json.load(f)
        except: json.JSONDecodeError 
        tickets_guardados = []

#ESCRIBIENDO CON JSON
    tickets_guardados.append(datos) 

    with open("tickets.json", "w", encoding="utf-8") as f:
       json.dump(tickets_guardados, f ,indent= 4 ,ensure_ascii=False )

       messagebox.showinfo("EXITO", "Ticket creado y almacenado correctamente")