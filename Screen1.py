import tkinter as tk
from backend1 import *
import backend1
from tkinter import messagebox

 
#Creando la pantalla
root = tk.Tk()
root.title("Helpdesk")
root.geometry("1800x1200")
root.resizable(True,True)
root.config(bg="#D3D3D3")
 
#creando el frame principal
screen1 = tk.Frame(root, bg="#D3D3D3")
screen1.pack(fill="both", expand=True)
 
#Creando una pestaña para los botones
frame_menu = tk.Frame(root, height=800, width=150, bg="#040430")
frame_menu.place(x=0, y=0)
 
#Creando un título para la pestaña
label_tittle = tk.Label(frame_menu, text="HELPDESK", height=2, width=17, bg="#030325", fg="White", font=("century gothic", 11, "bold"), bd=1, relief="solid")
label_tittle.place(x=0, y=0)
 
#Creando el botón para añadir tickets
def changescreen1():
    pantalla2.pack_forget()
    screen1.pack(fill="both", expand=True)
 
button_new_ticket = tk.Button(frame_menu, text="+\n NEW TICKET", height=5, width=17, bg="#040430", fg="White", font=("century gothic", 11, "bold"), borderwidth=1, relief="solid", cursor="hand2", anchor="center", command=lambda:changescreen2())
button_new_ticket.place(x=0, y=40)
def log_in(event):
    button_new_ticket.config(bg="#02021A")
def go_out(event):
    button_new_ticket.config(bg="#040430")
 
button_new_ticket.bind("<Enter>", log_in)
button_new_ticket.bind("<Leave>", go_out)
 

#PANTALLA 2
pantalla2 = tk.Frame(root, bg="#D3D3D3")
 
# Frame principal del formulario
frame_form = tk.Frame(
    pantalla2,
    bg="white",
    bd=2,
    relief="groove",
    width=1360,
    height=1800
)
frame_form.place(x=0, y=0)
frame_form.pack_propagate(False)
 
# Encabezado
header = tk.Label(
    frame_form,
    text="NEW TICKET",
    bg="#55638F",
    fg="white",
    font=("Century Gothic", 16, "bold"),
    height=2
)
header.pack(fill="x")
 
# Contenido
contenido = tk.Frame(frame_form, bg="white")
contenido.pack(pady=20)
 
# Ticket Number
tk.Label(
    contenido,
    text="Ticket Number:",
    bg="white",
    font=("Century Gothic",14)
).grid(row=0, column=0, padx=10, pady=15, sticky="w")
 
search_input = tk.Entry(contenido, width=40, font=("Century Gothic",11))
search_input.grid(row=0, column=1)
 
# User Name
tk.Label(
    contenido,
    text="User Name:",
    bg="white",
    font=("Century Gothic",10)
).grid(row=1, column=0, padx=10, pady=15, sticky="w")
 
user_name_input = tk.Entry(contenido, width=30)
user_name_input.grid(row=1, column=1)
 
# Problem
tk.Label(
    contenido,
    text="Problem:",
    bg="white",
    font=("Century Gothic",10)
).grid(row=2, column=0, padx=10, pady=15, sticky="nw")
 
problem_input = tk.Text(
    contenido,
    width=40,
    height=8
)
problem_input.grid(row=2, column=1)

 
# Prioridad
tk.Label(
    contenido,
    text="Priority:",
    bg="white",
    font=("Century Gothic", 10)
).grid(row=3, column=0, padx=10, pady=15, sticky="w")
 
priority = tk.StringVar()
priority.set("Medium")
 
priority_menu = tk.OptionMenu(
    contenido,
    priority,
    "Low",
    "Medium",
    "High",
    "Critical"
)
 
priority_menu.config(
    width=27,
    font=("Century Gothic", 9),
    bg="white"
)
 
priority_menu.grid(row=3, column=1, padx=5, pady=15)

#Creando una función para guardar los tickets
def guardar_ticket():

    almacenar_en_json(
        search_input.get(),
        user_name_input.get(),
        problem_input.get("1.0", tk.END).strip(),
        priority.get(),
    )

    messagebox.showinfo(
        "Éxito",
        "Ticket creado correctamente"
    )

    search_input.delete(0, tk.END)
    user_name_input.delete(0, tk.END)
    problem_input.delete("1.0", tk.END)

    changescreen1()

save_button = tk.Button(frame_form, text="GUARDAR", command=guardar_ticket, bg="#55638F", fg="white", font=("Century Gothic",11,"bold"), relief="flat", cursor="hand2", width=18, height=2)
save_button.place(x=400, y=500)


 
#creando boton para regresar a ventana principal
def changescreen2():
    screen1.pack_forget()
    pantalla2.pack(fill="both", expand=True)
    button_back = tk.Button(pantalla2, text="←\n", bg="#d3d3d3", fg="black", command=lambda:changescreen1() )
    button_back.place(x=20, y=50)
 
#PANTALLA 3
pantalla3 = tk.Frame(root, bg="#d3d3d3")
 

#Creando un botón para que el usuario vea sus tickets
def changescreen4():
    pantalla3.pack_forget()
    screen1.pack(fill="both", expand=True)
 
button_my_tickets = tk.Button(frame_menu, text="☰\n MY TICKETS", height=5, width=17, bg="#040430", fg="White", font=("century gothic", 11, "bold"), borderwidth=1, relief="solid", cursor="hand2", anchor="center", command=lambda:changescreen5())
button_my_tickets.place(x=0, y=141)
def log_in(event):
    button_my_tickets.config(bg="#02021A")
def go_out(event):
    button_my_tickets.config(bg="#040430")
 
button_my_tickets.bind("<Enter>", log_in)
button_my_tickets.bind("<Leave>", go_out)

# Lugar donde se almacenan y muestran los tickets creados en pantalla
def mostrar_tickets():
    # 1. LIMPIEZA VISUAL: Buscamos etiquetas viejas en pantalla3 y las destruimos
    for componente in pantalla3.winfo_children():
        # Validamos que no sea un botón (para no borrar la flecha de regresar)
        if isinstance(componente, tk.Label):
            componente.destroy()

    # 2. DIBUJAR: Traemos los datos frescos recién guardados del backend
    tickets = backend1.obtener_tickets()

    if not tickets:
        lbl_vacio = tk.Label(pantalla3, text="No hay tickets registrados.", bg="#d3d3d3", font=("century gothic", 10))
        lbl_vacio.pack(pady=20)
        return

    # 3. CREAR LABELS: Generamos las etiquetas dinámicas por cada ticket
    for datos in tickets:
        texto = f"ID: {datos['ID']}   |   User: {datos['User']}   |   ISSUE: {datos['Issue']}"
        
        my_tickets = tk.Label(
            pantalla3, 
            text=texto, 
            font=("century gothic", 10), 
            bg="white", 
            fg="black", 
            bd=1, 
            relief="solid", 
            padx=15, 
            pady=8,
            anchor="w"
        )
        my_tickets.pack(fill="x", padx=40, pady=5)

#creando boton para regresar a ventana principal
def changescreen5():
    screen1.pack_forget()
    pantalla3.pack(fill="both", expand=True)
    button_back2 = tk.Button(pantalla3, text="←\n", bg="#d3d3d3", fg="black", command=lambda:changescreen4() )
    button_back2.place(x=20, y=50)

    mostrar_tickets()
 
 
#Creando una pestaña para que el usuario pueda ver sus tickets
frame_user_tickets = tk.Frame(screen1, height=300, width=1153, bg="#C4C3C3", bd=2, borderwidth=0, relief="groove")
frame_user_tickets.place(x=180, y=150)
 
label_text1 = tk.Label(frame_user_tickets, text="Ticket ID", font=("Monserrat Black", 9, "bold"), anchor="center", height=2, width=24, bg="#55638F", fg="Black")
label_text1.place(x=0, y=0)
 
label_text2 = tk.Label(frame_user_tickets, text="Case", font=("Monserrat Black", 9, "bold"), anchor="center", height=2, width=42, bg="#55638F")
label_text2.place(x=172, y=0)
 
label_text3 = tk.Label(frame_user_tickets, text="User", font=("Monserrat Black", 9, "bold"), anchor="center", height=2, width=20, bg="#55638F")
label_text3.place(x=472, y=0)
 
label_text4 = tk.Label(frame_user_tickets, text="Creation Date", font=("Monserrat Black", 9, "bold"), anchor="center", height=2, width=26, bg="#55638F")
label_text4.place(x=618, y=0)
 
label_text5 = tk.Label(frame_user_tickets, text="Priority", font=("Monserrat Black", 9, "bold"), anchor="center", height=2, width=20, bg="#55638F")
label_text5.place(x=806, y=0)
 
label_text5 = tk.Label(frame_user_tickets, text="Status", font=("Monserrat Black", 9, "bold"), anchor="w", padx=16, height=2, width=26, bg="#55638F")
label_text5.place(x=949, y=0)


 
 
#Creando tickets de ejemplo
frame_ticket1 = tk.Label(frame_user_tickets, height=3, width=166, bg="#DFD8D8", bd=2, borderwidth=1, relief="groove")
frame_ticket1.place(x=0, y=30)
 
label_icon_document = tk.PhotoImage(file="document1_icon.png")
label_icon_document = label_icon_document.subsample(2,2)
label_document = tk.Label(frame_ticket1, image=label_icon_document, bg="#DFD8D8")
label_document.place(x=16, y=8)
 
label_icon_id = tk.Label(frame_ticket1, text="#TI-000553", bg="#DFD8D8", fg="#1F2937", font=("century gothic", 8, "bold"))
label_icon_id.place(x=56, y=13)

label_icon_problem = tk.Label(frame_ticket1, text="I can´t access my account", bg="#DFD8D8", fg="#1F2937", font=("century gothic", 8, "bold"))
label_icon_problem.place(x=254, y=13)

label_icon_user = tk.PhotoImage(file="user.png")
label_icon_user = label_icon_user.subsample(2,2)
label_user = tk.Label(frame_ticket1, image=label_icon_user, bg="#DFD8D8")
label_user.place(x=464, y=8)

label_user = tk.Label(frame_ticket1, text="dansof9", bg="#DFD8D8", fg="#1F2937", font=("century gothic", 8, "bold"))
label_user.place(x=500, y=13)
 
label_icon_date = tk.Label(frame_ticket1, text="25/06/2026 9:14", bg="#DFD8D8", fg="#1F2937", font=("century gothic", 8, "bold"))
label_icon_date.place(x=666, y=13)


#Creando el boton para abrir el menu en cascada de priority
def selecionar_opcion2(texto_selecionado):
    button_priority.configure(text=f"{texto_selecionado}")
 
def mostrar_menu2():
    x = button_priority.winfo_rootx()
    y = button_priority.winfo_rooty() + button_priority.winfo_height()
    menu_opciones2.post(x, y)
 
button_priority = tk.Button(frame_ticket1, text="Low", command=mostrar_menu2, bg="#00B40F", fg="#000000", width=9, font=("century gothic", 8, "bold"))
button_priority.place(x=844, y=13)
 
#Creando menu cascada
menu_opciones2 = tk.Menu(frame_ticket1, tearoff=0, bg="white", fg="black", font=("century gothic", 8, "bold"))
menu_opciones2.add_command(label="High", command=lambda: selecionar_opcion2("High"))
menu_opciones2.add_command(label="Medium", command=lambda: selecionar_opcion2("Medium"))
menu_opciones2.add_command(label="Low", command=lambda: selecionar_opcion2("Low"))

#Creando el boton para abrir el menu en cascada de status
def selecionar_opcion(texto_selecionado):
    button_status.configure(text=f"{texto_selecionado}")
 
def mostrar_menu():
    x = button_status.winfo_rootx()
    y = button_status.winfo_rooty() + button_status.winfo_height()
    menu_opciones.post(x, y)
 
button_status = tk.Button(frame_ticket1, text="Open", command=mostrar_menu, bg="#55638F", fg="#DFD8D8", width=9, font=("century gothic", 8, "bold"))
button_status.place(x=953, y=13)
 
#Creando menu cascada
menu_opciones = tk.Menu(frame_ticket1, tearoff=0, bg="white", fg="black", font=("century gothic", 8, "bold"))
menu_opciones.add_command(label="Pendiente", command=lambda: selecionar_opcion("pendiente"))
menu_opciones.add_command(label="En progreso", command=lambda: selecionar_opcion("En progreso"))
menu_opciones.add_command(label="Resuelto", command=lambda: selecionar_opcion("Resuelto"))

button_delete = tk.Button(frame_ticket1, text="Eliminar", bg="#A70000", fg="#DFD8D8", width=8, font=("century gothic", 8, "bold"))
button_delete.place(x=1062, y=13)

frame_ticket2= tk.Label(frame_user_tickets, height=3, width=166, bg="#DFD8D8", bd=2, borderwidth=1, relief="groove")
frame_ticket2.place(x=0, y=79)

label_icon_wifi = tk.PhotoImage(file="wifi.png")
label_icon_wifi = label_icon_wifi.subsample(2,2)
label_wifi = tk.Label(frame_ticket2, image=label_icon_wifi, bg="#DFD8D8")
label_wifi.place(x=16, y=8)

label_id2 = tk.Label(frame_ticket2, text="#TI-000673", bg="#DFD8D8", fg="#1F2937", font=("century gothic", 8, "bold"))
label_id2.place(x=56, y=13)

label_icon_problem2 = tk.Label(frame_ticket2, text="Connection problems", bg="#DFD8D8", fg="#1F2937", font=("century gothic", 8, "bold"))
label_icon_problem2.place(x=276, y=13)

label_icon_user2 = tk.PhotoImage(file="user.png")
label_icon_user2 = label_icon_user2.subsample(2,2)
label_user2 = tk.Label(frame_ticket2, image=label_icon_user2, bg="#DFD8D8")
label_user2.place(x=464, y=8)

label_user2 = tk.Label(frame_ticket2, text="Jos10-30ue", bg="#DFD8D8", fg="#1F2937", font=("century gothic", 8, "bold"))
label_user2.place(x=500, y=13)

label_icon_date2 = tk.Label(frame_ticket2, text="29/05/2026 11:14", bg="#DFD8D8", fg="#1F2937", font=("century gothic", 8, "bold"))
label_icon_date2.place(x=665, y=13)

button_priority2 = tk.Button(frame_ticket2, text="High", bg="#FFD104", fg="#000000", width=8, font=("century gothic", 8, "bold"))
button_priority2.place(x=844, y=13)

button_status2 = tk.Button(frame_ticket2, text="Open", bg="#55638F", fg="#DFD8D8", width=8, font=("century gothic", 8, "bold"))
button_status2.place(x=953, y=13)

button_delete2 = tk.Button(frame_ticket2, text="Eliminar", bg="#A70000", fg="#DFD8D8", width=8, font=("century gothic", 8, "bold"))
button_delete2.place(x=1062, y=13)

frame_ticket3= tk.Label(frame_user_tickets, height=3, width=166, bg="#DFD8D8", bd=2, borderwidth=1, relief="groove")
frame_ticket3.place(x=0, y=128)

label_icon_wifi2 = tk.PhotoImage(file="wifi.png")
label_icon_wifi2 = label_icon_wifi2.subsample(2,2)
label_wifi2 = tk.Label(frame_ticket3, image=label_icon_wifi, bg="#DFD8D8")
label_wifi2.place(x=16, y=8)

label_id3 = tk.Label(frame_ticket3, text="#TI-002610", bg="#DFD8D8", fg="#1F2937", font=("century gothic", 8, "bold"))
label_id3.place(x=56, y=13)

label_icon_problem3 = tk.Label(frame_ticket3, text="Connection problems", bg="#DFD8D8", fg="#1F2937", font=("century gothic", 8, "bold"))
label_icon_problem3.place(x=276, y=13)

label_icon_user3 = tk.PhotoImage(file="user.png")
label_icon_user3 = label_icon_user2.subsample(2,2)
label_user3 = tk.Label(frame_ticket3, image=label_icon_user2, bg="#DFD8D8")
label_user3.place(x=464, y=8)

label_user3 = tk.Label(frame_ticket3, text="Javersols8", bg="#DFD8D8", fg="#1F2937", font=("century gothic", 8, "bold"))
label_user3.place(x=500, y=13)

label_icon_date3 = tk.Label(frame_ticket3, text="18/10/2026 11:18", bg="#DFD8D8", fg="#1F2937", font=("century gothic", 8, "bold"))
label_icon_date3.place(x=665, y=13)

button_priority3 = tk.Button(frame_ticket3, text="Medium", bg="#FF8E0D", fg="#000000", width=8, font=("century gothic", 8, "bold"))
button_priority3.place(x=844, y=13)

button_status3 = tk.Button(frame_ticket3, text="Open", bg="#55638F", fg="#DFD8D8", width=8, font=("century gothic", 8, "bold"))
button_status3.place(x=953, y=13)

button_delete3 = tk.Button(frame_ticket3, text="Eliminar", bg="#A70000", fg="#DFD8D8", width=8, font=("century gothic", 8, "bold"))
button_delete3.place(x=1062, y=13)

frame_ticket4= tk.Label(frame_user_tickets, height=3, width=166, bg="#DFD8D8", bd=2, borderwidth=1, relief="groove")
frame_ticket4.place(x=0, y=177)

label_icon_padlock = tk.PhotoImage(file="padlock.png")
label_icon_padlock = label_icon_padlock.subsample(2,2)
label_padlock2 = tk.Label(frame_ticket4, image=label_icon_padlock, bg="#DFD8D8")
label_padlock2.place(x=16, y=8)

label_id4 = tk.Label(frame_ticket4, text="#TI-102010", bg="#DFD8D8", fg="#1F2937", font=("century gothic", 8, "bold"))
label_id4.place(x=56, y=13)

label_icon_problem4 = tk.Label(frame_ticket4, text="Password problems", bg="#DFD8D8", fg="#1F2937", font=("century gothic", 8, "bold"))
label_icon_problem4.place(x=276, y=13)

label_icon_user4 = tk.PhotoImage(file="user.png")
label_icon_user4 = label_icon_user2.subsample(2,2)
label_user4 = tk.Label(frame_ticket4, image=label_icon_user2, bg="#DFD8D8")
label_user4.place(x=464, y=8)

label_user4 = tk.Label(frame_ticket4, text="Metz07", bg="#DFD8D8", fg="#1F2937", font=("century gothic", 8, "bold"))
label_user4.place(x=500, y=13)

label_icon_date4 = tk.Label(frame_ticket4, text="03/12/2026 08:18", bg="#DFD8D8", fg="#1F2937", font=("century gothic", 8, "bold"))
label_icon_date4.place(x=665, y=13)

button_priority4 = tk.Button(frame_ticket4, text="High", bg="#FFD104", fg="#000000", width=8, font=("century gothic", 8, "bold"))
button_priority4.place(x=844, y=13)

button_status4 = tk.Button(frame_ticket4, text="Open", bg="#55638F", fg="#DFD8D8", width=8, font=("century gothic", 8, "bold"))
button_status4.place(x=953, y=13)

button_delete4 = tk.Button(frame_ticket4, text="Eliminar", bg="#A70000", fg="#DFD8D8", width=8, font=("century gothic", 8, "bold"))
button_delete4.place(x=1062, y=13)

frame_pending_tickets = tk.Frame(screen1, bg="#818EB9", width=30, height=11)
frame_pending_tickets.place(x=180, y=490)

label_icon_clock = tk.PhotoImage(file="clock.png")
label_clock = tk.Label(
    frame_pending_tickets,
    image=label_icon_clock,
    bg="#818EB9")

                         
#Añadiendo un título para la pantalla
label_title = tk.Label(screen1,
    text="HELPDESK: INCIDENT MANAGEMENT",
    bg="#D3D3D3",
    fg="black",
    font=("Century Gothic", 25, "bold")
)
label_title.place(x=180, y=8)
 
#Creando un buscador
label_search = tk.Label(
    screen1,
    bg="#D3D3D3",
    fg="black",
    font=("Century Gothic", 14, "bold")
)
label_search.place(x=180, y=25)
 

entry_search = tk.Entry(
    screen1,
    width=110,
    font=("Century Gothic", 11)
)
entry_search.place(x=180, y=60)
 
def remove_text(event):
    if entry_search.get() == "Insert your ticket ID...":
        entry_search.delete(0, tk.END)
def add_text(event):
    if entry_search.get() == "":
        entry_search.insert(0, "Insert your ticket ID...")
entry_search.insert(0, "Insert your ticket ID...")
entry_search.bind("<FocusIn>", remove_text)
entry_search.bind("<FocusOut>", add_text)
search_icon = tk.PhotoImage(file="search.png")
search_icon = search_icon.subsample(2, 2)
button_search = tk.Button(
    screen1,
    image=search_icon,
    bg="#818EB9",
    fg="white",
    borderwidth=0,
    cursor="hand2",
    relief="flat"
)
button_search.place(x=1050, y=56)
 
def log_in(event):
    button_search.config(bg="#818EB9")
def go_out(event):
    button_search.config(bg="White")
 
button_search.bind("<Enter>", log_in)
button_search.bind("<Leave>", go_out)


 
 
root.mainloop()
 
 