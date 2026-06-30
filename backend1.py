from tkinter import messagebox


#Creando los tickets.

tickets = []
contador = 1

def crear_new_ticket (user, ID , issue):
    global contador 

    if user == "" or ID == "" or issue == "":
        messagebox.showerror("Campos Incomletos", "Debe completar todos los campos") 
        return

    datos = {
        "Ticket": contador,
        "ID" : ID,
        "User" : user,
        "Issue": issue
    }

    tickets.append (datos)
    print(tickets)
    contador += 1

    messagebox.showinfo("EXITO" , "Ticket creado correctamente")

def obtener_tickets():
    return tickets


    

    




