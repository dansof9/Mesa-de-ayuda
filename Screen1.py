import tkinter as tk
from backend1 import *
import backend1
 
#Creando la pantalla
root = tk.Tk()
root.title("Helpdesk")
root.geometry("800x600")
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
pantalla2 = tk.Frame(root, bg="#d3d3d3")
 
#solicitando el numero de ticket
ID = tk.Label(pantalla2, text="ticket number", bg="black", fg="white")
ID.pack(pady=20)

ID_input = tk.Entry(pantalla2)
ID_input.pack(pady=14)
 
#solcitando el nombre de usuario
user_name = tk.Label(pantalla2, text="User name:", bg="Black", fg="white")
user_name.pack(pady=15)
 
user_name_input = tk.Entry(pantalla2)
user_name_input.pack(pady=17)

#solicitando tipo de problema
problem = tk.Label(pantalla2, text="What's your problem?", bg="black", fg="white")
problem.pack(pady=5)
problem_input = tk.Entry(pantalla2)
problem_input.pack(pady=10)
 
Button_guardar = tk.Button(pantalla2,text="Guardar",command= lambda:(crear_new_ticket(ID_input.get(),user_name_input.get(),problem_input.get())),bg= "Black" , fg = "White")
Button_guardar.place(x=660,y=315)

 
#creando boton para regresar a ventana principal
def changescreen2():
    screen1.pack_forget()
    pantalla2.pack(fill="both", expand=True)
    button_back = tk.Button(pantalla2, text="←\n", bg="#d3d3d3", fg="black", command=lambda:changescreen1() )
    button_back.place(x=20, y=50)
 
#PANTALLA 3
pantalla3 = tk.Frame(root, bg="#d3d3d3")
 
#pantalla 3 continuacion ---
 
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

#Lugar donde se almacenan los tickets creados
def mostrar_tickets():
   

   for datos in backend1.obtener_tickets():
   
     texto = (
       "User: " + datos["User"],
       "ID: " + datos["ID"],
       "ISSUE: " + datos["Issue"]
   )

     my_tickets = tk.Label (pantalla3, text= texto)
     my_tickets.pack()

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
 
label_text3 = tk.Label(frame_user_tickets, text="Category", font=("Monserrat Black", 9, "bold"), anchor="center", height=2, width=20, bg="#55638F")
label_text3.place(x=472, y=0)
 
label_text4 = tk.Label(frame_user_tickets, text="Creation Date", font=("Monserrat Black", 9, "bold"), anchor="center", height=2, width=26, bg="#55638F")
label_text4.place(x=618, y=0)
 
label_text5 = tk.Label(frame_user_tickets, text="Channel", font=("Monserrat Black", 9, "bold"), anchor="center", height=2, width=20, bg="#55638F")
label_text5.place(x=806, y=0)
 
label_text5 = tk.Label(frame_user_tickets, text="Status", font=("Monserrat Black", 9, "bold"), anchor="center", height=2, width=28, bg="#55638F")
label_text5.place(x=952, y=0)
 
 
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

label_category = tk.Label(frame_ticket1, text="Access Control", bg="#DFD8D8", fg="#1F2937", font=("century gothic", 8, "bold"))
label_category.place(x=500, y=13)
 
label_icon_date = tk.Label(frame_ticket1, text="25/06/2026 9:14", bg="#DFD8D8", fg="#1F2937", font=("century gothic", 8, "bold"))
label_icon_date.place(x=666, y=13)

label_icon_channel = tk.PhotoImage(file="computer.png")
label_icon_channel = label_icon_channel.subsample(2,2)
label_channel1 = tk.Label(frame_ticket1, image=label_icon_channel, bg="#DFD8D8")
label_channel1.place(x=824, y=8)
 
label_channel = tk.Label(frame_ticket1, text="Website", bg="#DFD8D8", fg="#1F2937", font=("century gothic", 8, "bold"))
label_channel.place(x=860, y=13)

label_status = tk.Label(frame_ticket1, text="Open", bg="#55638F", fg="#DFD8D8", width=8, font=("century gothic", 8, "bold"))
label_status.place(x=1024, y=13)


frame_ticket2= tk.Label(frame_user_tickets, height=3, width=166, bg="#DFD8D8", bd=2, borderwidth=1, relief="groove")
frame_ticket2.place(x=0, y=79)

label_icon_wifi = tk.PhotoImage(file="wifi.png")
label_icon_wifi = label_icon_wifi.subsample(2,2)
label_wifi = tk.Label(frame_ticket2, image=label_icon_wifi, bg="#DFD8D8")
label_wifi.place(x=16, y=8)

label_id = tk.Label(frame_ticket2, text="#TI-000673", bg="#DFD8D8", fg="#1F2937", font=("century gothic", 8, "bold"))
label_id.place(x=56, y=13)

label_icon_problem2 = tk.Label(frame_ticket2, text="Send mail error", bg="#DFD8D8", fg="#1F2937", font=("century gothic", 8, "bold"))
label_icon_problem2.place(x=276, y=13)

label_icon_user2 = tk.PhotoImage(file="user.png")
label_icon_user2 = label_icon_user2.subsample(2,2)
label_user2 = tk.Label(frame_ticket2, image=label_icon_user2, bg="#DFD8D8")
label_user2.place(x=464, y=8)

label_category2 = tk.Label(frame_ticket2, text="Access Control", bg="#DFD8D8", fg="#1F2937", font=("century gothic", 8, "bold"))
label_category2.place(x=500, y=13)

label_icon_date2 = tk.Label(frame_ticket2, text="29/05/2026 11:14", bg="#DFD8D8", fg="#1F2937", font=("century gothic", 8, "bold"))
label_icon_date2.place(x=665, y=13)

label_icon_channel2 = tk.PhotoImage(file="computer.png")
label_icon_channel2 = label_icon_channel.subsample(1,1)
label_channel2 = tk.Label(frame_ticket2, image=label_icon_channel2, bg="#DFD8D8")
label_channel2.place(x=824, y=8)

label_channel2 = tk.Label(frame_ticket2, text="Website", bg="#DFD8D8", fg="#1F2937", font=("century gothic", 8, "bold"))
label_channel2.place(x=860, y=13)
                         
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
    if entry_search.get() == "How can we help you?...":
        entry_search.delete(0, tk.END)
def add_text(event):
    if entry_search.get() == "":
        entry_search.insert(0, "How can we help you?...")
entry_search.insert(0, "How can we help you?...")
entry_search.bind("<FocusIn>", remove_text)
entry_search.bind("<FocusOut>", add_text)
search_icon = tk.PhotoImage(file="search.png")
search_icon = search_icon.subsample(2, 2)
button_search = tk.Button(
    screen1,
    image=search_icon,
    bg="white",
    fg="white",
    borderwidth=0,
    cursor="hand2",
    relief="flat"
)
button_search.place(x=1050, y=56)
 
def log_in(event):
    button_search.config(bg="#B4B2B2")
def go_out(event):
    button_search.config(bg="White")
 
button_search.bind("<Enter>", log_in)
button_search.bind("<Leave>", go_out)
 
 
root.mainloop()
 
 