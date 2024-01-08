import requests
import tkinter as tk
from tkinter import messagebox

def obtener_info_pepamon():
    nombre_o_id = entry.get()
    url = f"http://localhost:5000/pepamones/nombre/{nombre_o_id.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        info = f"Nombre: {data['name'].capitalize()}\nID: {data['id']}\nTipo: {data['type'].capitalize()}"
        messagebox.showinfo("Información del Pepamón", info)
    else:
        messagebox.showerror("Error", "¡El Pepamón no fue encontrado!")

def agregar_pepamon():
    nombre = entry_nombre.get()
    tipo = entry_tipo.get()
    new_pepamon = {'name': nombre, 'type': tipo}

    url = "http://localhost:5000/pepamones"  # Reemplaza con la URL de tu propia API
    response = requests.post(url, json=new_pepamon)

    if response.status_code == 201:
        messagebox.showinfo("Éxito", f"¡Se agregó a {nombre.capitalize()}!")
    else:
        messagebox.showerror("Error", "No se pudo agregar el Pepamón.")

root = tk.Tk()
root.title("PepamónDex")
root.geometry("800x392")

# Cargar la imagen de fondo
background_image = tk.PhotoImage(file="mutante.png")
root.background_image = background_image  # Mantener una referencia global

# Establecer la imagen de fondo
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)  # Ajustar la imagen al tamaño de la ventana

# Crear la etiqueta, entrada y botón para obtener información del Pepamón
label = tk.Label(root, text="Ingrese el nombre o ID del Pepamón:", bg="white")
label.place(relx=0.3, rely=0.8)
entry = tk.Entry(root)
entry.place(relx=0.6, rely=0.8)
button = tk.Button(root, text="Obtener información", command=obtener_info_pepamon)
button.place(relx=0.45, rely=0.9)

# Crear la etiqueta, entrada y botón para agregar un nuevo Pepamón
label_nombre = tk.Label(root, text="Nombre del Pepamón:", bg="white")
label_nombre.place(relx=0.3, rely=0.5)
entry_nombre = tk.Entry(root)
entry_nombre.place(relx=0.5, rely=0.5)

label_tipo = tk.Label(root, text="Tipo del Pepamón:", bg="white")
label_tipo.place(relx=0.3, rely=0.6)
entry_tipo = tk.Entry(root)
entry_tipo.place(relx=0.5, rely=0.6)

button_agregar = tk.Button(root, text="Agregar Pepamón", command=agregar_pepamon)
button_agregar.place(relx=0.45, rely=0.7)

root.mainloop()