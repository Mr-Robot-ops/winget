import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess
import re
import math
import colorsys
import threading
import time

# Autor: Mr-Robot-ops
# Licence CC0
# Version 2.3

# Liste für die Anwendungsdaten
app_data = []

# Flag für die Sortierreihenfolge
sort_reverse = False

# Flag für das automatische einmalige Auswählen des "Hell"-Themas
auto_select_hell_theme = True

def list_upgradeable_apps():
    try:
        result = subprocess.run(["winget", "upgrade"], capture_output=True, text=True, check=True)
        app_treeview.delete(*app_treeview.get_children())  # Clear existing items
        
        app_info_lines = result.stdout.splitlines()
        
        app_data.clear()
        for line in app_info_lines[3:]:  # Skip the header lines
            app_info = re.split(r"\s{2,}", line.strip())
            if len(app_info) >= 5:
                app_name = app_info[0]
                app_id = app_info[1]
                app_version = app_info[2]
                app_available = app_info[3]
                app_source = app_info[4]
                app_data.append((app_name, app_id, app_version, app_available, app_source))
        
        # Zeige Anwendungen in ihrer ursprünglichen Reihenfolge an
        for app_info in app_data:
            app_treeview.insert("", tk.END, values=app_info)
    except subprocess.CalledProcessError as e:
        app_treeview.delete(*app_treeview.get_children())  # Clear existing items
        app_treeview.insert("", tk.END, values=("Fehler beim Abrufen der aktualisierbaren Anwendungen.", "", "", "", ""))

def sort_apps_by_name():
    global sort_reverse
    sort_reverse = not sort_reverse
    
    # Sortiere die Anwendungen nach dem modifizierten Namen und umgekehrt, wenn sort_reverse True ist
    app_data.sort(key=lambda x: (x[0].lower(), x[0]), reverse=sort_reverse)
    
    # Lösche vorhandene Einträge
    app_treeview.delete(*app_treeview.get_children())
    
    # Füge die sortierten Einträge hinzu
    for app_info in app_data:
        app_treeview.insert("", tk.END, values=app_info)

def upgrade_selected_apps():
    selected_items = app_treeview.selection()
    
    if not selected_items:
        result_label.config(text="Keine ausgewählten Anwendungen zum Aktualisieren.", fg="red")
        return
    
    try:
        for item in selected_items:
            app_id = app_treeview.item(item, "values")[1]
            print("Aktualisiere Anwendung (ID):", app_id)  # Debug-Ausgabe
            try:
                subprocess.run(["winget", "upgrade", "--source", "winget", app_id], check=True)
            except subprocess.CalledProcessError as e:
                # Behandle den Fehler für diese Anwendung, ohne die Schleife zu verlassen
                print(f"Fehler beim Aktualisieren der Anwendung (ID {app_id}): {e.stderr}")
        
        result_label.config(text="Ausgewählte Anwendungen wurden erfolgreich aktualisiert.", fg="green")
    except Exception as e:
        result_label.config(text=f"Fehler beim Aktualisieren der Anwendungen:\n{str(e)}", fg="red")

def set_theme(theme):
    root.tk_setPalette(background=theme_colors[theme]["background"], foreground=theme_colors[theme]["foreground"])
    app_treeview.tag_configure("selected", background=theme_colors[theme]["selection_background"], foreground=theme_colors[theme]["foreground"])
    update_selection_hint(theme)
    update_text_colors(theme)

def update_selection_hint(theme):
    if theme == "grau":
        selection_hint.config(text="Halten Sie die Shift-Taste gedrückt und klicken Sie die linke Maustaste, um mehrere Anwendungen auszuwählen.", fg="black")
    else:
        selection_hint.config(text="Halten Sie die Shift-Taste gedrückt und klicken Sie die linke Maustaste, um mehrere Anwendungen auszuwählen.", fg=theme_colors[theme]["foreground"])

def update_text_colors(theme):
    text_color = theme_colors[theme]["text_color"]
    list_button.config(fg=text_color)
    upgrade_button.config(fg=text_color)
    result_label.config(fg=text_color)
    selection_hint.config(fg=text_color)

def show_background_menu(event):
    background_menu.post(event.x_root, event.y_root)

def show_gradient_menu(event):
    gradient_menu.post(event.x_root, event.y_root)

def update_rainbow_gradient():
    while True:
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        radius = math.sqrt(width ** 2 + height ** 2)
        center_x = width / 2
        center_y = height / 2
        
        rainbow_image = Image.new("RGB", (width, height))
        
        for x in range(width):
            for y in range(height):
                angle = math.atan2(y - center_y, x - center_x)
                distance = math.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
                hue = (angle + math.pi) / (2 * math.pi)
                saturation = min(distance / radius, 1.0)
                lightness = 0.5
                
                # Hier können Sie die Farben basierend auf der aktuellen Zeit ändern
                hue_offset = time.time() % 10 / 10  # Ändern Sie die 10, um die Geschwindigkeit der Farbänderung anzupassen
                hue = (hue + hue_offset) % 1.0
                
                r, g, b = colorsys.hls_to_rgb(hue, lightness, saturation)
                r = int(r * 255)
                g = int(g * 255)
                b = int(b * 255)
                
                rainbow_image.putpixel((x, y), (r, g, b))
        
        gradient_photo = ImageTk.PhotoImage(rainbow_image)
        root_label.config(image=gradient_photo)
        root_label.image = gradient_photo
        
        time.sleep(0.1)  # Warten Sie 0,1 Sekunden, bevor Sie den Farbverlauf erneut aktualisieren

# Initialisieren Sie das Hauptfenster
root = tk.Tk()
root.title("Winget x 2.3 - Aktualisierung von Anwendungen")

# Erstellen Sie den Farbverlauf
root_label = tk.Label(root)
root_label.place(relwidth=1, relheight=1)

# Starten Sie die Funktion zum ersten Mal
update_rainbow_gradient_thread = threading.Thread(target=update_rainbow_gradient)
update_rainbow_gradient_thread.daemon = True
update_rainbow_gradient_thread.start()

list_button = tk.Button(root, text="Aktualisierbare Anwendungen auflisten", command=list_upgradeable_apps)
list_button.pack()

app_treeview = ttk.Treeview(root, columns=("Name", "ID", "Version", "Verfügbar", "Quelle"), selectmode="extended")
app_treeview.heading("#1", text="Name")
app_treeview.heading("#2", text="ID")
app_treeview.heading("#3", text="Version")
app_treeview.heading("#4", text="Verfügbar")
app_treeview.heading("#5", text="Quelle")
app_treeview.pack(fill=tk.BOTH, expand=True)

# Fügen Sie einen Klick-Handler für die Spalte "Name" hinzu
app_treeview.heading("#1", text="Name", command=sort_apps_by_name)

upgrade_button = tk.Button(root, text="Ausgewählte Anwendungen aktualisieren", command=upgrade_selected_apps)
upgrade_button.pack()

result_label = tk.Label(root, text="", fg="green")
result_label.pack()

selection_hint = tk.Label(root, text="", fg="gray")
selection_hint.pack()

# Kontextmenü für Hintergrundthemen
background_menu = tk.Menu(root, tearoff=0)
background_menu.add_command(label="Dunkel", command=lambda: set_theme("dunkel"))
background_menu.add_command(label="Hell", command=lambda: set_theme("hell"))
background_menu.add_command(label="Grau", command=lambda: set_theme("grau"))
background_menu.add_command(label="Blau", command=lambda: set_theme("blau"))

# Farbpaletten für verschiedene Themen
theme_colors = {
    "dunkel": {
        "background": "#000000",
        "foreground": "#ffffff",
        "selection_background": "#333333",
        "text_color": "#ffffff"
    },
    "hell": {
        "background": "#ffffff",
        "foreground": "#000000",
        "selection_background": "#e0e0e0",
        "text_color": "#000000"
    },
    "grau": {
        "background": "#888888",
        "foreground": "#000000",
        "selection_background": "#aaaaaa",
        "text_color": "#000000"
    },
    "blau": {
        "background": "#87CEEB",
        "foreground": "#006400",
        "selection_background": "#7FB069",
        "text_color": "#006400"
    }
}

if auto_select_hell_theme:
    set_theme("hell")  # Automatische Auswahl des "Hell"-Themas nach dem Start

root.bind("<Button-3>", show_background_menu)  # Rechtsklick öffnet das Menü

root.mainloop()
