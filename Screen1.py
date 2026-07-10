import tkinter as tk
from backend1 import *
import backend1
from tkinter import messagebox

 
#Creando la pantalla
root = tk.Tk()
root.title("Helpdesk")
root.state("zoomed")
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
#PANTALLA 2
pantalla2 = tk.Frame(root, bg="#F3F5F7")
 
# Frame principal del formulario
frame_form = tk.Frame(
    pantalla2,
    bg="#F3F5F7",
    bd=2,
    relief="groove",
    width=1360,
    height=700
)
frame_form.place(x=0, y=0)
 
# Encabezado
header = tk.Label(
    frame_form,
    text="NEW TICKET",
    anchor="center",
    bg="#55638F",
    fg="white",
    font=("Century Gothic",16,"bold"),
    width=104,
    height=3
)
header.place(x=0, y=0)
 
# User Name
user_icon = tk.PhotoImage(file="user.png")
user_icon = user_icon.subsample(2,2)
user = tk.Label(frame_form, image=user_icon, bg="#F3F5F7")
user.place(x=270, y=160)

label_user = tk.Label(
    frame_form,
    text="User Name:",
    bg="#F3F5F7",
    font=("Century Gothic",14)
)
label_user.place(x=310, y=160)

user_name_input = tk.Entry(
    frame_form,
    width=40,
    font=("Century Gothic",11),
    bg="#FCF9F9",
    fg="#333333",
    relief="ridge",
    bd=1
)

user_name_input.place(x=550, y=160)
# Problem
problem_icon = tk.PhotoImage(file="problem.png")
problem_icon = problem_icon.subsample(2,2)
problem = tk.Label(frame_form, image=problem_icon, bg="#F3F5F7")
problem.place(x=270, y=220)

label_problem = tk.Label(
    frame_form,
    text="Problem:",
    bg="#F3F5F7",
    font=("Century Gothic",14)
)
label_problem.place(x=310, y=220)

problem_input = tk.Text(
    frame_form,
    width=60,
    height=12,
    font=("Century Gothic",11),
    bg="#FCF9F9",
    fg="#333333",
    relief="ridge",
    bd=1
    )
problem_input.place(x=550, y=220)

# Prioridad
priority_icon = tk.PhotoImage(file="priority.png")
priority_icon = priority_icon.subsample(2,2)
priority = tk.Label(frame_form, image=priority_icon, bg="#F3F5F7")
priority.place(x=270, y=464)

label_priority = tk.Label(
    frame_form,
    text="Priority:",
    bg="#F3F5F7",
    font=("Century Gothic",14),
   )

label_priority.place(x=310, y=464)

priority = tk.StringVar(value="Medium")
priority_menu = tk.OptionMenu(
    frame_form,
    priority,
    "Low",
    "Medium",
    "High",
    )

def cambiar_color(*args):
    colores = {
        "Low": "#4CAF50",
        "Medium": "#FF9800",
        "High": "#FFC107",
        
    }

    color = colores.get(priority.get(), "white")

    priority_menu.config(
        bg=color,
        width=40,
        font=("Century Gothic",10)
    )

priority.trace_add("write", cambiar_color)

# Pintar el color inicial
cambiar_color()

priority_menu.place(x=550, y=464)

#Creando una función para guardar los tickets
def guardar_ticket():

    usuario = user_name_input.get()
    problema = problem_input.get("1.0", "end-1c")
    prioridad = priority.get()

    if almacenar_en_json(usuario, problema, prioridad):

        user_name_input.delete(0, tk.END)
        problem_input.delete("1.0", tk.END)

        changescreen1()

    else:
        # Si faltan campos, solo limpiar el formulario
        user_name_input.delete(0, tk.END)
        problem_input.delete("1.0", tk.END)

    

#Creando el botón para guardar 
save_button = tk.Button(frame_form, text="GUARDAR", command=guardar_ticket, bg="#36405F", fg="white", font=("Century Gothic",11,"bold"), relief="flat", cursor="hand2", width=34, height=2)
save_button.place(x=550, y=580)

#creando boton para regresar a ventana principal
def changescreen2():
    screen1.pack_forget()
    pantalla2.pack(fill="both", expand=True)
    button_back = tk.Button(pantalla2, text="←\n", bg="#55638F", height=4, fg="White", command=lambda:changescreen1() )
    button_back.place(x=4, y=5)

#PANTALLA 3

# PANTALLA 3 (
pantalla3 = tk.Frame(root, bg="#d3d3d3")
 
# Creando un botón para que el usuario vea sus tickets
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
 
def mostrar_tickets():
 
    for componente in pantalla3.winfo_children():
        if isinstance(componente, tk.Button) and "←" in componente.cget("text"):
            continue
        componente.destroy()
 
    try:
        with open("tickets.json", "r", encoding="utf-8") as archivo:
            tickets_cargados = json.load(archivo)
    except FileNotFoundError:
        tickets_cargados = []
 
    if not tickets_cargados:
        lbl_vacio = tk.Label(pantalla3, text="No hay tickets registrados.", bg="#d3d3d3", font=("century gothic", 12, "bold"))
        lbl_vacio.pack(pady=50)
        return
 
    colores = {
        "Low": "#2ECC71",
        "Medium": "#F1C40F",
        "High": "#E67E22",
        "Critical": "#E74C3C"
    }
 
    # Generar de forma ordenada las tarjetas dentro de pantalla3
    for ticket in tickets_cargados:
        prioridad = ticket.get("Priority", "Medium")
        color_barra = colores.get(prioridad, "#F1C40F")
        
        tarjeta = tk.Frame(pantalla3, bg="white", bd=1, relief="solid")
        tarjeta.pack(padx=40, pady=10, fill="x")
 
        barra_prioridad = tk.Label(
            tarjeta,
            text=prioridad.upper(),
            bg=color_barra,
            fg="white",
            font=("century gothic", 9, "bold")
        )
        barra_prioridad.pack(fill="x")
 
        lbl_issue = tk.Label(
            tarjeta,
            text=ticket["Issue"],
            font=("century gothic", 11, "bold"),
            bg="white",
            anchor="w",
            padx=10,
            pady=5
        )
        lbl_issue.pack(anchor="w", fill="x")
 
        lbl_user = tk.Label(
            tarjeta,
            text=f"Responsable: {ticket['User']}",
            font=("century gothic", 9),
            bg="white",
            fg="#555555",
            anchor="w",
            padx=10,
            pady=2
        )
        lbl_user.pack(anchor="w", fill="x")
 
# creando boton para regresar a ventana principal
def changescreen5():
    screen1.pack_forget()
    pantalla3.pack(fill="both", expand=True)
    button_back2 = tk.Button(pantalla3, text="←", bg="#d3d3d3", fg="black", width=1, height=1, command=lambda:changescreen4() )
    button_back2.place(x=1, y=50)
 


# === BOTÓN CERRAR SESIÓN === #

# Función para salir de la aplicación 
def cerrar_sesion():
    confirmacion = messagebox.askyesno("LOG OUT", "¿Está seguro de que desea salir del sistema?")
    if confirmacion:
        os.system("python login.py")
        root.destroy() 

# Creando el botón
button_logout = tk.Button(
    frame_menu, 
    text="LOG OUT", 
    height=1, 
    width=17, 
    bg="#A70000",      
    fg="White", 
    font=("century gothic", 11, "bold"), 
    borderwidth=1, 
    relief="solid", 
    cursor="hand2", 
    anchor="center", 
    command=cerrar_sesion
)
button_logout.place(x=0, y=650) 

def log_in_logout(event):
    button_logout.config(bg="#7A0000") 
def go_out_logout(event):
    button_logout.config(bg="#A70000") 

button_logout.bind("<Enter>", log_in_logout)
button_logout.bind("<Leave>", go_out_logout)

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


 
#Pantalla de tickets recientes
def act_tickets_recientes():
    for componente in frame_user_tickets.winfo_children():
        if isinstance(componente, tk.Label) and componente.winfo_y() > 0:
            componente.destroy()
        elif isinstance(componente, tk.Frame) and componente.winfo_y() > 0:
            componente.destroy()
 
#bteniendo los datos reales desde el backend
lista_tickets = backend1.obtener_tickets()
tickets_recientes = list(reversed(lista_tickets))[:4]
posicion_y = 30
 
#Creando vizualizacion de ticket
for datos in tickets_recientes:
        #Contenedor del ticket individual
        ticket_view = tk.Frame(frame_user_tickets, height=45, width=1153, bg="#DFD8D8", bd=1, relief="groove")
        ticket_view.place(x=0, y=posicion_y)
        ticket_view.pack_propagate(False)
       
        #ID del Ticket
        lbl_id = tk.Label(ticket_view, text=f"#TI-{datos['ID']:04d}", bg="#DFD8D8", fg="#1F2937", font=("century gothic", 8, "bold"))
        lbl_id.place(x=56, y=13)
       
        #issue
        lbl_prob = tk.Label(ticket_view, text=datos['Issue'], bg="#DFD8D8", fg="#1F2937", font=("century gothic", 8, "bold"))
        lbl_prob.place(x=175, y=13)
       
        #Icono de usuario y Nombre
        lbl_user_img = tk.Label(ticket_view, bg="#DFD8D8")
        lbl_user_img.place(x=464, y=8)
       
        lbl_user_name = tk.Label(ticket_view, text=datos['User'], bg="#DFD8D8", fg="#1F2937", font=("century gothic", 8, "bold"))
        lbl_user_name.place(x=500, y=13)
       
        #Fecha de creación
        lbl_date = tk.Label(ticket_view, text=datos.get('Date'), bg="#DFD8D8", fg="#1F2937", font=("century gothic", 8, "bold"))
        lbl_date.place(x=666, y=13)
 
 
        #Botón Prioridad
        color_p = {"Low": "#00B40F", "Medium": "#FF8E0D", "High": "#FFD104"}.get(datos['Priority'], "#00B40F")
        btn_p = tk.Button(ticket_view, text=datos['Priority'].lower(), bg=color_p, fg="#000000", width=9, font=("century gothic", 8, "bold"))
        btn_p.place(x=844, y=13)
        btn_p.configure(command=lambda b=btn_p: mostrar_menu_priority(b))
       
        #Botón Estatus
        estado_actual = datos.get('Status', "Pending")
        color_s = {"Pending": "#FFD104", "In progress": "#FF8E0D", "Resolved": "#00B40F"}.get(estado_actual, "#FFD104")
        btn_s = tk.Button(ticket_view, text=estado_actual, bg=color_s, fg="Black", width=9, font=("century gothic", 8, "bold"))
        btn_s.place(x=953, y=13)
        btn_s.configure(command=lambda b=btn_s: mostrar_menu_status(b))
       
        #Botón Eliminar
        btn_d = tk.Button(ticket_view, text="Delete", bg="#A70000", fg="#DFD8D8", width=8, font=("century gothic", 8, "bold"))
        btn_d.place(x=1062, y=13)
        btn_d.configure(command=lambda r=ticket_view: ejecutar_eliminacion_logica(r))
       
        posicion_y += 49
 
def ejecutar_eliminacion_logica(fila_widget):
    confirmacion = messagebox.askyesno("elimination", "Do you want to eliminate this ticket?")
    if confirmacion:
        id_limpio = "1" 
        
        # Eliminamos del archivo JSON
        backend1.eliminar_ticket_json(id_limpio)
        
        # Eliminamos la interfaz visual
        fila_widget.destroy()
    else:
        print("Eliminación cancelada")




#Creando el boton para abrir el menu en cascada de priority
def selecionar_opcion2(boton_selecionado2, texto_selecionado2, color_selecionado2):
    boton_selecionado2.configure(text=f"{texto_selecionado2}", bg=color_selecionado2, activebackground=color_selecionado2)

def mostrar_menu_priority(boton_actual):
 x = boton_actual.winfo_rootx()
 y = boton_actual.winfo_rooty() + btn_p.winfo_height()
 menu_opciones_priority.post(x, y)

#creando menu cascada para todos los botones
 menu_opciones_priority.entryconfigure(0, command=lambda: selecionar_opcion2(boton_actual, "High", "#FFD104") )
 menu_opciones_priority.entryconfigure(1, command=lambda: selecionar_opcion2(boton_actual, "Medium","#FF8E0D" ))
 menu_opciones_priority.entryconfigure(2, command=lambda: selecionar_opcion2(boton_actual, "Low","#00B40F"))

#Creando menu cascada
menu_opciones_priority = tk.Menu(frame_user_tickets, tearoff=0, bg="white", fg="black", font=("century gothic", 8, "bold"))
menu_opciones_priority.add_command(label="High")
menu_opciones_priority.add_command(label="Medium")
menu_opciones_priority.add_command(label="Low")

#BOTON DE STATUS

#Creando el boton para abrir el menu en cascada de status
def selecionar_opcion(boton_selecionado, texto_selecionado, color_selecionado):
    boton_selecionado.configure(text=f"{texto_selecionado}", bg=color_selecionado, activebackground=color_selecionado)

def mostrar_menu_status(boton_actual2):
 x = boton_actual2.winfo_rootx()
 y = boton_actual2.winfo_rooty() + btn_s.winfo_height()
 menu_opciones_status.post(x, y)

#creando menu cascada para todos los botones
 menu_opciones_status.entryconfigure(0, command=lambda: selecionar_opcion(boton_actual2, "Pending", "#FFD104") )
 menu_opciones_status.entryconfigure(1, command=lambda: selecionar_opcion(boton_actual2, "In progress","#FF8E0D" ))
 menu_opciones_status.entryconfigure(2, command=lambda: selecionar_opcion(boton_actual2, "Resolved","#00B40F"))


#Creando menu cascada
menu_opciones_status = tk.Menu(frame_user_tickets, tearoff=0, bg="white", fg="black", font=("century gothic", 8, "bold"))
menu_opciones_status.add_command(label="Pending")
menu_opciones_status.add_command(label="In progress")
menu_opciones_status.add_command(label="Resolved")


#ELMINANDO TICKET DE LA PARTE VISUAL Y DE JSON
def delete_ticket(button_delete):
    confirmacion = messagebox.askyesno("elimination", "Do you want to eliminate this ticket?")
    if confirmacion:
        id_limpio = "2" 
        
        # Eliminamos del archivo JSON
        backend1.eliminar_ticket_json(id_limpio)
        
        # Eliminamos la interfaz visual
        frame_ticket1 = button_delete.master
        frame_ticket1.destroy()
    else:
        print("Eliminación cancelada")

def delete_ticket2(button_delete2):
    confirmacion = messagebox.askyesno("elimination", "Do you want to eliminate this ticket?")
    if confirmacion:
        id_limpio = "3"
        backend1.eliminar_ticket_json(id_limpio)
        
        frame_ticket2 = button_delete2.master
        frame_ticket2.destroy()
    else:
        print("Eliminación cancelada")


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

# Creando una lista de tickets
tickets = []

for i in range(1, 1001):
    tickets.append(f"#TI-{i:03}")

#Creando una lista de sugerencias
listbox = tk.Listbox(
    screen1,
    width=110,
    height=5,
    font=("Century Gothic", 10)
)

listbox.place_forget()

 
#Creando una función para buscar tickets
def buscar(event):

    print("Estoy buscando")

    texto = entry_search.get()
    listbox.delete(0, tk.END)

    if texto == "" or texto == "Insert your ticket ID...":
        listbox.place_forget()
        return

    encontrados = 0

# Buscando coincidencias con los tickets 
    for ticket in tickets:

        if ticket.lower().startswith(texto.lower()):

            listbox.insert(tk.END, ticket)

            encontrados += 1
            if encontrados == 5:
                break

    if encontrados > 0:
        listbox.place(x=180, y=88)
    else:
        listbox.place_forget()


def seleccionar(event):

    if listbox.curselection():

        ticket = listbox.get(listbox.curselection())

        entry_search.delete(0, tk.END)

        entry_search.insert(0, ticket)

        listbox.place_forget()

entry_search.bind("<KeyRelease>", buscar)
listbox.bind("<<ListboxSelect>>", seleccionar)

#Creando una funciones para que el texto del buscador desaparezca
def remove_text(event):
    if entry_search.get() == "Insert your ticket ID...":
        entry_search.delete(0, tk.END)
def add_text(event):
    if entry_search.get() == "":
        entry_search.insert(0, "Insert your ticket ID...")

entry_search.insert(0, "Insert your ticket ID...")
entry_search.bind("<FocusIn>", remove_text)
entry_search.bind("<FocusOut>", add_text)

# === PANTALLA 4 ===  #

pantalla4 = tk.Frame(root, bg="#d3d3d3")

def changescreen6():
    pantalla4.pack_forget()
    screen1.pack(fill="both", expand=True)

def cambiar_pantalla(event):
    id_buscado = entry_search.get().strip()
    listbox.place_forget() 

    if id_buscado == "" or id_buscado == "Insert your ticket ID...":
        return

    try:
        id_limpio = str(int(id_buscado.replace("#TI-", "")))
    except ValueError:
        id_limpio = "0"

    ticket_encontrado = backend1.buscar_ticket(id_limpio)

    if ticket_encontrado:
        
        # Limpiando pantalla4 
        for componente in pantalla4.winfo_children():
            componente.destroy()

        # Botón para regresar a la pantalla principal
        button_back3 = tk.Button(pantalla4, text="←\n", bg="#d3d3d3", fg="black", font=("century gothic", 11, "bold"), command=changescreen6)
        button_back3.place(x=20, y=50)

      # DESING #
        

        frame_resultado = tk.Frame(pantalla4, bg="#55638F", bd=0, highlightthickness=1, highlightbackground="#434F74", relief="flat", width=450, height=430)
        frame_resultado.place(x=450, y=120)

        # 1.ID 
        lbl_id = tk.Label(frame_resultado, text=f"#TI\n{ticket_encontrado['ID']:03d}", bg="#5B132B", fg="White", font=("Segoe UI", 12, "bold"), width=6, height=3, bd=0, justify="center")
        lbl_id.place(x=30, y=25)

        # Fecha alineada en la esquina superior derecha
        lbl_fecha = tk.Label(frame_resultado, text=datos.get('Date'), bg="#55638F", fg="#000000", font=("century gothic", 12, "bold"))
        lbl_fecha.place(x=300, y=35)

        # 2.ISSUE 
        lbl_issue_title = tk.Label(frame_resultado, text="ISSUE:", bg="#55638F", fg="#000000", font=("century gothic", 12, "bold"))
        lbl_issue_title.place(x=30, y=110)

        lbl_issue = tk.Label(frame_resultado, text=ticket_encontrado['Issue'], bg="#55638F", fg="Black", font=("Segoe UI", 11), justify="left", anchor="nw", wraplength=390)
        lbl_issue.place(x=30, y=135, width=390, height=110)

        # 3.USER

        lbl_user_title = tk.Label(frame_resultado, text="USER:", bg="#55638F", fg="#000000", font=("century gothic", 12, "bold"))
        lbl_user_title.place(x=30, y=260)

        lbl_user = tk.Label(frame_resultado, text=ticket_encontrado['User'].upper(), bg="#55638F", fg="#B4ADAD", font=("century gothic", 12, "bold"))
        lbl_user.place(x=90, y=260)

        # 4.LÍNEA DIVISORIA
        line = tk.Frame(frame_resultado, bg="#BDBDBD", width=300, height=2)
        line.place(x=70, y=300)

        # 5.BOTONES

        #priority
        def selecionar_opcion2(boton_selecionado2, texto_selecionado2, color_selecionado2):
            boton_selecionado2.configure(text=f"{texto_selecionado2}", bg=color_selecionado2, activebackground=color_selecionado2)

        def mostrar_menu_priority_p4(boton_actual):
            x = boton_actual.winfo_rootx()
            y = boton_actual.winfo_rooty() + button_priority.winfo_height()
            menu_opciones_priority.post(x, y)

        prio_txt = ticket_encontrado['Priority'].capitalize()
        prio_color = "#00B40F" if prio_txt == "Low" else ("#FF8E0D" if prio_txt == "Medium" else "#FFD104")

        lbl_txt_prio = tk.Label(frame_resultado, text="Priority:", bg="#55638F", fg="White", font=("century gothic", 9, "bold"))
        lbl_txt_prio.place(x=30, y=320)

        button_priority = tk.Button(frame_resultado, text=prio_txt, bg=prio_color, fg="#000000", width=10, bd=0, font=("century gothic", 8, "bold"))
        button_priority.place(x=30, y=345)
        button_priority.configure(command=lambda: mostrar_menu_priority_p4(button_priority))

        menu_opciones_priority = tk.Menu(frame_resultado, tearoff=0, bg="white", fg="black", font=("century gothic", 8, "bold"))
        menu_opciones_priority.add_command(label="High", command=lambda: selecionar_opcion2(button_priority, "High", "#FFD104"))
        menu_opciones_priority.add_command(label="Medium", command=lambda: selecionar_opcion2(button_priority, "Medium", "#FF8E0D"))
        menu_opciones_priority.add_command(label="Low", command=lambda: selecionar_opcion2(button_priority, "Low", "#00B40F"))


      #status
        def selecionar_opcion(boton_selecionado, texto_selecionado, color_selecionado):
            boton_selecionado.configure(text=f"{texto_selecionado}", bg=color_selecionado, activebackground=color_selecionado)

        def mostrar_menu_status_p4(boton_actual2):
            x = boton_actual2.winfo_rootx()
            y = boton_actual2.winfo_rooty() + button_status.winfo_height()
            menu_opciones_status.post(x, y)

        lbl_txt_status = tk.Label(frame_resultado, text="Status:", bg="#55638F", fg="White", font=("century gothic", 9, "bold"))
        lbl_txt_status.place(x=175, y=320)

        button_status = tk.Button(frame_resultado, text="Resolved", bg="#00B40F", fg="Black", width=10, bd=0, font=("century gothic", 8, "bold"))
        button_status.place(x=175, y=345)
        button_status.configure(command=lambda: mostrar_menu_status_p4(button_status))

        menu_opciones_status = tk.Menu(frame_resultado, tearoff=0, bg="white", fg="black", font=("century gothic", 8, "bold"))
        menu_opciones_status.add_command(label="Pending", command=lambda: selecionar_opcion(button_status, "Pending", "#FFD104"))
        menu_opciones_status.add_command(label="In progress", command=lambda: selecionar_opcion(button_status, "In progress", "#FF8E0D"))
        menu_opciones_status.add_command(label="Resolved", command=lambda: selecionar_opcion(button_status, "Resolved", "#00B40F"))


        #DELETE

        def delete_ticket_p4(button_del):
            confirmacion = messagebox.askyesno("elimination", "Do you want to eliminate this ticket?")
            if confirmacion:
                id_a_borrar = ticket_encontrado['ID']
                
                backend1.eliminar_ticket_json(id_a_borrar)
                button_del.master.destroy()
                changescreen6()
            else:
                print("Eliminación cancelada")

        button_delete = tk.Button(frame_resultado, text="Delete", bg="#A70000", fg="#DFD8D8", width=10, bd=0, font=("century gothic", 8, "bold"), command=lambda: delete_ticket_p4(button_delete))
        button_delete.place(x=320, y=345)


        # Cambio de pantallas
        screen1.pack_forget()                      
        pantalla4.pack(fill="both", expand=True)   

        # Limpieza de buscador
        entry_search.delete(0, tk.END)
        entry_search.insert(0, "Insert your ticket ID...")
        root.focus()
    else:
        messagebox.showerror("Not Found", f"No ticket found with ID: {id_buscado}")

# Buscar mediante tecla "ENTER"
entry_search.bind("<Return>", cambiar_pantalla)



root.mainloop()